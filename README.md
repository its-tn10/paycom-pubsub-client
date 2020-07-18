# paycom-pubsub-client
A quick client implementation to demonstrate the capabilities of a Publisher-Subscriber Broker server built [here](https://github.com/its-tn10/paycom-pubsub-broker).

Utilizes Python 3.8+ and the asyncio library. Just run the run.py file and it's self-explanatory!

Commands list:
* **/CONNECT**: connect and authenticate as an existing user
* **/CREATE**: create a user account

* **/TOPICS**: lists the available topics (subscriber only)
* **/SUBSCRIBE**: subscribes to a topic (subscriber only)
* **/UNSUBSCRIBE**: unsubscribes a topic (subscriber only)

* **/NEWTOPIC**: creates a new topic (publisher only)
* **/PUBLISH**: publish a message to a topic (publisher only)
