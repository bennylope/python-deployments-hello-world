# Hello World in FastAPI for example deployments

1. [Locally](#locally)
2. [Heroku](#heroku)
3. [Render](#render)
4. [Platform.sh](#platformsh)
5. [Railway](#railway)
6. [Fly.io](#flyio)

## Locally

Install:

    python -m pip install -r requirements.txt

Run (specifying port is optional):

    uvicorn app:app --port=8000


## Heroku

The app can be deployed to [Heroku](https://heroku.com) using free resources, however you will need to establish your
account first. Once you have an account, you can click the button here to deploy to Heroku:

1. Log into (or create) your Heroku account
2. Click this button [![Deploy to Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/bennylope/python-deployments-hello-world)
3. Enter a name for your app (it will need to be unique across all of Heroku)
4. Choose your region
5. Click "Deploy app"

Alternatively, fork this repository, create a Heroku app in your Heroku dashboard, then Git push to that repository.

1. Fork this repository in your GitHub account
1. Log into (or create) your Heroku account
2. Click "New" then select "Create new app"
3. Enter a name for your app (it will need to be unique across all of Heroku)
4. Choose your region and click Deploy
5. Select "Connect to GitHub", choose your fork and click "Connect"

## Render

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy)

There are two ways to quickly set up the Hello World app with [Render](https://render.com), as an individual web service or as a
services "blueprint". The "blueprint" allows you to take advantage of the `render.yaml` configuration file
included in the app source code. Both allow you to test this out for free, however the "blueprint" method
requires adding a credit card to your account.

### Individual web service

1. Log into (or create) your Render account
2. From the dashboard click the "New" button in the top navigation bar
3. Select "Web Service" from the list
4. Enter the *web* URL of the public GitHub repo, i.e. not ending in `.git` (see note below)
5. Click the repository link that appears under the URL input
6. On the next page give your web service a name
7. For "Start Command" add `uvicorn app:app --host=0.0.0.0`
8. Select the Plan if this is presented. If you have not added a credit card on file with your account
you will see only the "Free" option.
9. Click "Create Web Service" and wait a few minutes
10. 💥

Instead of a GitHub URL you can add a public GitLab URL _or_ you can connect the account to add a
private repository.

### Blueprint

1. Log into (or create) your Render account
2. From the dashboard click the "New" button in the top navigation bar
3. Select "Blueprint" from the list
4. Enter the *web* URL of the public GitHub repo, i.e. not ending in `.git` (see previous note)
5. Click the repository link that appears under the URL input
6. On the next page give your "Service Group" a name
7. Verify the git branch (the default repository branch should be selected by default)
8. Click "Apply" and wait a few minutes
9. 💥

In the case of the service group blueprint, the advantage is that you didn't need to enter
any configuration for the individual web service.

## Platform.sh

1. Log into (or create) your Platform.sh account
2. Add your public SSH key to your Platform.sh account
3. Create a new Project
4. Choose "Create from scratch"
5. Give your project a name
6. Choose the plan (should be able to do so on a free trial, but YMMV)
7. Copy the Git remote from Platform.sh console and add locally,
   `platform project:set-remote <project-id>` OR
   `git remote set-url platform <project-id>@git.<region-code>.platform.sh:<project-id>.git`
   e.g. `git remote set-url platform bat34w3o53aaa@git.us-4.platform.sh:bat34w3o53aaa.git`
7. Push to the new remote, `git push platform main`

## Railway

Deploying on [Railway](https://railway.app/) is pretty straightforward, with the only "gotcha" being that you need to take a separate step on the web console to expose your app to the Internet on a Railway domain.

1. Create an account on 
2. Install the command line `railway` tool (`brew` on Mac or using `npm`)
3. Log in locally (`railway login`)
4. Initialize the project (`railway init`)
5. Deploy (`railway up`)
6. Log into the web console, click through to the project, then into the service, then settings, then under Environment set up the domain

## Fly.io

Fly.io deployments are initiated from the command line using the `flyctl` tool (for those thinking ahead, yes, this can be done from continuous integration systems as well).
