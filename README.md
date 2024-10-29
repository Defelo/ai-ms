# Bootstrap Academy AI Microservice

The official AI microservice of [Bootstrap Academy](https://bootstrap.academy/).

This microservice provides a foundational API endpoint for AI integrations, with an emphasis on extendibility. Currently, it uses OpenAI's GPT-4, but it can easily accommodate other models and providers.

If you would like to submit a bug report or feature request, or are looking for general information about the project or the publicly available instances, please refer to the [Bootstrap-Academy repository](https://github.com/Bootstrap-Academy/Bootstrap-Academy).

## Endpoints

### POST `/api/ai`

Accessible only to administrators with a valid API key. This endpoint takes in prompts and returns an AI-generated response.

#### Request Example

```json
{
  "system_prompt": "You are an assistant.",
  "user_prompt": "What's the weather today?"
}
```

#### Response Example

```json
{
  "output": "I am an AI model and do not have live weather data."
}
```

## Development Setup

1. Install [Python 3.10](https://python.org/), [Poetry](https://python-poetry.org/) and [poethepoet](https://pypi.org/project/poethepoet/).
2. Clone this repository and `cd` into it.
3. Run `poe setup` to install the dependencies.
4. Run `poe api` to start the microservice. You can find the automatically generated swagger documentation on http://localhost:8001/docs.

## Poetry Scripts

```bash
poe setup           # setup dependencies, .env file and pre-commit hook
poe api             # start api locally
poe test            # run unit tests
poe pre-commit      # run pre-commit checks
  poe lint          # run linter
    poe format      # run auto formatter
      poe isort     # sort imports
      poe black     # reformat code
    poe ruff        # check code style
    poe mypy        # check typing
    poe flake8      # check code style
  poe coverage      # run unit tests with coverage
poe alembic         # use alembic to manage database migrations
poe migrate         # run database migrations
poe env             # show settings from .env file
poe jwt             # generate a jwt with the given payload and ttl in seconds
poe check           # check course definitions
poe sync_skills     # push local skills to backend (deprecated)
```

## PyCharm configuration

Configure the Python interpreter:

- Open PyCharm and go to `Settings` ➔ `Project` ➔ `Python Interpreter`
- Open the menu `Python Interpreter` and click on `Show All...`
- Click on the plus symbol
- Click on `Poetry Environment`
- Select `Existing environment` (setup the environment first by running `poe setup`)
- Confirm with `OK`

Setup the run configuration:

- Click on `Add Configuration...` ➔ `Add new...` ➔ `Python`
- Change target from `Script path` to `Module name` and choose the `api` module
- Change the working directory to root path ➔ `Edit Configurations` ➔ `Working directory`
- In the `EnvFile` tab add your `.env` file
- Confirm with `OK`
