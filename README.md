# Conversational Commerce RASA POC

This is showing based off of a open source [boilerplate chatbot project](https://github.com/lappis-unb/rasa-ptbr-boilerplate/issues) developed at UnB's Lappis lab.

Read the [boilerplate's README](docs/README.md) for more information on how to run this project locally now.

## Scope

- ~~Hook up the RASA Bot engine to run with both Telegram and Twilio WhatsApp numbers~~
- Set up the Analytics and Logging component of the project so we can quickly iterate with data.
- Train an initial model with a ShoppingList intent and see the entities that are formed in Portuguese.

##  How to run and Demo video

### Setting up the devserver on AWS

Training and experimenting with machine learning models can be quite computer intensive.
Most models implemented on tensorflow are programmed to make use of GPU.
Follow these steps to set up a machine you can ssh into and pull this directory to experiment
on the models.

1. [Follow this guide](https://www.notion.so/marjorivtex/How-to-get-AWS-access-2e71b217c52d49369ce8bc86b6ec8109) to get access to AWS and VPN.
2. Install [Terraform CLI](https://learn.hashicorp.com/tutorials/terraform/aws-build) and [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html).

```
aws configure
terraform init
terraform validate
terraform apply
```

### Video showing training of a model locally

This is not the final video, just one showing the dev flow to add a story and train a model:
https://www.loom.com/share/a7ac3a1ad9734dfa94844209924e9169

Install the [Loom for Chrome Extension](https://www.loom.com/blog/loom-github-chrome-extension-integration) to see the video embeded.

## Notes

- Could not import name 'json' from 'engineio’ when running *make train*.
	- Solution was to upgrade RASA to 0.39
- Upgraded RASA from the boilerplate project to 2.5.x
- Upgraded RASA X to 0.39.x

### Future TODO
- Create a data training pipeline to get some training samples
- Abstract away the story flow component into React components state machine outside this repp
- Move the bot hub from endpoitn from running on this POC to a javacript webhook so we can connect to vtex io / storefront
- Change RabbitMQ to Redis Stream
