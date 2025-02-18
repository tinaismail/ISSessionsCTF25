# **KPMG In the Bin**
![](Assets/kpmg.png)
## Stage 1: Obtain Valid Auth Tokens

After navigating to the target URL, I'm greeted with a lovely homepage about construction container solutions. I navigate through the page and I spot a link to Developer Tools in the footer. That should be interesting. In the Developer Tools page, I see a button called Go to Admin Panel, but it appears that I don't have the proper authorization to access this page. I resolve to checking out the documentation more closely.

![](Assets/kpmg.gif)

In the API endpoints section, there is an endpoint to /auth/tokens/ which supposedly retrieves a list of active and expired tokens. I simply change my URL to direct to this endpoint and I am bombarded with a JSON file with 34 entries that appear to be JWTs.
![](Assets/tokens.png)
Active and expired authentication tokens obtained from the /auth/tokens endpoint

`JSON Web Tokens (JWTs) are token-based authentication used to access APIs. Insecure implementations can lead to serious vulnerabilities, with threat actors having the ability to forge tokens and hijack user sessions. [TryHackMe 'JWT Security' Room]`

I copy the raw data and paste it into CyberChef, converting the data from Base-64. This is because JWTs are Base-64 encoded consisting of 3 distinct components called the Header, Payload, and Signature. The signature is verifies the token's authenticity and uses the algorithm specified in the JWT's header. Scrolling through the decoded JWT tokens, I find a token that has the following decoded payload.

`{"sub":"1234567890","user":"admin","iat":1516239022}`

Exciting! This is the only token assigned to an admin user. However, I'm still given a 405 when attempting to access the /admin-panel endpoint, so let's analyze the JWT. Pulling it into JWT.io, it looks like the signature is invalid. We can't do much without a signing key, so let's look at the rest of the developer tools page.

In Developer Tools, the GraphQL Documentation section stands out. Clicking on the Access Full GraphQL Documentation button brings me to a page with available queries and mutations to interact with the API, and a static test of the endpointInfo query that conveniently retrieves a list of available endpoints.

`{
  "data": {
    "endpointInfo": "Available Endpoints: /graphql, /auth/tokens, /auth/customer-data"
  }
}`

Let's try sending a POST request to the /graphql endpoint. In the screenshot below, I specify the debugLog mutation to view the debug logs.
![](Assets/logs.png)
Debug log obtained from the /graphql endpoint

Copying the result into a text editor, I try to find any references to a secret key. To my delight, I find the following entry: 

`[2025-02-18 07:21:38] DEBUG - Encoded secret: bXV0YXRpb24geyBqd3RDb25maWcoa2V5OiAiU0VDUkVUX1JFUVVFU1QiKX0=. Don't forget to escape with slash.`

Noting the "=" at the end of the key, I fire up CyberChef for the second time and decode the secret using From Base-64. The following is the result: `mutation { jwtConfig(key: "SECRET_REQUEST")}`. 

Referencing the documentation again, I find the structure of this mutation and again send a POST request to the /graphql endpoint with the following result. Private Key: dynamic_secret_key_3490. Great! Now I can use this secret to sign the JWT, shown in the screenshot below. 
![](Assets/jwt.png)
Signing the JWT with the secret key

Again, I attempt to access the /admin-panel route, and again I am unsuccessful. However, I recall the hint in the challenge description above: You should be able to access a "protected" endpoint if you have valid tokens. If it's valid, proceed to the next stage.

So let's instead try to request the /protected endpoint.
![](Assets/protected.png)
Accessing the /protected endpoint

The message reads: Welcome to the protected endpoint!  Smuggling Secrets in the Bin Builder Yard.  The Container Bin Builder yard was always bustling with activity. Steel beams clanged, welding sparks flew, and massive containers were assembled one after another. It was a place of order and precision—or so it seemed. But hidden among the stacks of shipping containers, something was being smuggled.


## Stage 2: HTTP Smuggling

After verifying that the token I have obtained is indeed valid and correctly signed, I must now gain access to the /admin-panel endpoint. The message at the end of Stage 1 suggests something is to be smuggled. 

`The attacker causes part of their front-end request to be interpreted by the back-end server as the start of the next request. It is effectively prepended to the next request, and so can interfere with the way the application processes that request. This is a request smuggling attack, and it can have devastating results. [PortSwigger 'Request Smuggling']`

```
POST /protected HTTP/1.1
Host: issessionsctf-web-kpmg.chals.io
Content-Type: application/x-www-form-urlencoded
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwidXNlciI6ImFkbWluIiwiaWF0IjoxNTE2MjM5MDIyfQ.uOLLl9S4Mjg_wBi9KKWn_5ZJOyDBrlCWdR1xUAq-LJY
Content-Length: 215

0

GET /flag HTTP/1.1
Host: localhost
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwidXNlciI6ImFkbWluIiwiaWF0IjoxNTE2MjM5MDIyfQ.uOLLl9S4Mjg_wBi9KKWn_5ZJOyDBrlCWdR1xUAq-LJY
```
Obtain flag: **bhbureauctf{Sh1pp3d_4nd_D3l1v3r3d_Succ3ssfu11y___}**
