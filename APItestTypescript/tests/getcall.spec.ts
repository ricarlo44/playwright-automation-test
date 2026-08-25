import {test, expect} from '@playwright/test';

test("Test Get API", async ({request}) => {

   const resp = await request.get("https://jsonplaceholder.typicode.com/posts/1");
   
   const responseBody = await resp.body();
//console.log(responseBody.toString());
//console.log(resp);
//Get the response as JSON body
   const respjson = await resp.json();
// console.log(respjson);

  const respheaders = resp.headers();
  console.log(respheaders);
});