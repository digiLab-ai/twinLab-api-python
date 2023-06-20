# Python twinLab API

This is how one can use the `twinLab API` via [Python](https://www.python.org/).

The [api.py](./api.py) file wraps the `twinLab API` in functions, which you can use in your own code.
The snippets in the [examples](./examples) directory demonstrate how these might be used.

> Note: Because of the way that Python handles imports an api.py symbolic link is placed in the examples directory.

First, you need to set up the environment variables in the top-level [`.env`](.env) file.
You can copy the [`.env.example`](.env.example) file as a template:

```shell
cp .env.example .env
open .env
```

If you are running locally, you need to set the `TWINLAB_USERNAME` and `TWINLAB_SECRET` variables.
If you are running through RapidAPI then you need to set the `TWINLAB_KEY` and `TWINLAB_HOST` variables.

## Quick Start

```shell
poetry install
```

## Examples

You can then run the example examples in the [examples](./examples) directory:

```shell
poetry run python examples/<event_name>.py ...
```

## Get user information
```shell
poetry run python examples/get_user.py
```

## Get version information
```shell
poetry run python examples/get_versions.py
```

## List datasets
```shell
poetry run python examples/list_datasets.py
```

## Upload dataset
```shell
poetry run python examples/upload_dataset.py <path/to/dataset.csv> <dataset_id>
poetry run python examples/upload_dataset.py resources/datasets/pollution.csv pollution
```

## View dataset
```shell
poetry run python examples/view_dataset.py <dataset_id>
poetry run python examples/view_dataset.py pollution
```

## Summarise a dataset
```shell
poetry run python examples/summarise_dataset.py <dataset_id>
poetry run python examples/summarise_dataset.py pollution
```

## List campaigns
```shell
poetry run python examples/list_campaigns.py
```

## Train campaign
```shell
poetry run python examples/train_campaign.py <path/to/parameters.json> <campaign_id> <processor>
poetry run python examples/train_campaign.py resources/campaigns/pollution/parameters.json pollution-campaign cpu
```

## Get the campaign status
```shell

```

## Summarise campaign
```shell
poetry run python examples/summarise_campaign.py <campaign_id>
poetry run python examples/summarise_campaign.py pollution-campaign
```

## Predict using a trained campaign
```shell
poetry run python examples/use_campaign.py <path/to/inputs.csv> <campaign_id> <method> <processor>
poetry run python examples/use_campaign.py resources/campaigns/pollution/eval.csv pollution-campaign predict cpu
```

## Delete campaign
```shell
poetry run python examples/delete_campaign.py <campaign_id>
poetry run python examples/delete_campaign.py pollution-campaign
```

## Delete dataset
```shell
poetry run python examples/delete_dataset.py <dataset_id>
poetry run python examples/delete_dataset.py pollution
```