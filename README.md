# anonymizer

Simple proxy to anonymize e-mails to remove a barrier to providing feedback.

# How to contribute

For instructions on how to setup your development environment, check `DEV_SETUP.md`. And to contribute,
just send us pull requests.

To run the tests, start the lamson server and the log app:
$ lamson start
$ lamson log

Then run the tests with:
$ nosetests

To check what routes are matching an email, run:
$ lamson routes -test email@address
