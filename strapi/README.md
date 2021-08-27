# Strapi Headless CMS
Strapi is a pre-baked CMS that can be used with any kind of static / dynamic web pages.

## Prerequisites

- [nodejs](https://nodejs.org/en/download/)
- yarn
```
# nodejs need to be installed first
npm i -g yarn
```
- heroku cli (if you want to do a manual deployment)
```
# macOS
brew tap heroku/brew && brew install heroku
```

## How to use?

- [Create new content types](https://strapi.io/documentation/user-docs/latest/content-types-builder/introduction-to-content-types-builder.html)

- [Roles and permissions management](https://strapi.io/documentation/user-docs/latest/users-roles-permissions/introduction-to-users-roles-permissions.html)

- [Strapi Docs](https://strapi.io/documentation/user-docs/latest/getting-started/introduction.html)

Please contact [@vtno](https://github.com/vtno), [@georgically](https://github.com/georgically) or [@jean](https://github.com/jean)  to get access to the Strapi admin panel.

# How to add new content type ?

Start development server by running

```
yarn develop
```

Strapi should be accessible via http://localhost:1337/admin
If you access it for the first time you need to create an account.

Then click go to content type builder
![2021-08-27 at 22 41](https://user-images.githubusercontent.com/2187352/131180668-a04018f5-6edc-4f5d-9efd-218b1d764e87.png)

Click create new single type
![2021-08-27 at 22 44](https://user-images.githubusercontent.com/2187352/131180800-253bb289-e2e2-4895-a7c0-194c929c718f.png)

Then add your page name as the `display name` and add 2 fields for the content type:

- markdown_content_th
- markdown_content_en

Then commit and push the code. When the code is merged, the changes will be applied on https://pyconth-strapi.herokuapp.com/admin/

Go their and allow the APIs to be accessed by going to https://pyconth-strapi.herokuapp.com/admin/settings/users-permissions/roles then click on `public`:
![2021-08-27 at 23 26](https://user-images.githubusercontent.com/2187352/131184844-09cb64c9-50a5-4add-b039-4a0c746edd50.png)

Tick the `find` checkbox and click save:
![2021-08-27 at 23 27](https://user-images.githubusercontent.com/2187352/131185019-4f721ba4-d54d-4c06-a658-3e4022fe1b0e.png)

Then you're done. Try out the API by running:
```
curl https://pyconth-strapi.herokuapp.com/<content-type>
# e.g
curl https://pyconth-strapi.herokuapp.com/faq
curl https://pyconth-strapi.herokuapp.com/about
```

## Manual Deployment
At the root dir of the project

```
make strapi/deploy
```

For more detail please see: [strapi heroku deployment](https://strapi.io/documentation/developer-docs/latest/setup-deployment-guides/deployment/hosting-guides/heroku.html)

Please contact [@vtno](https://github.com/vtno) to get access to the Heroku app.
