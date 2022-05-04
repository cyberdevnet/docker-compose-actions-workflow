# docker-compose-actions-workflow

[![Actions Status](https://github.com/peter-evans/docker-compose-actions-workflow/workflows/docker-compose-actions-workflow/badge.svg)](https://github.com/peter-evans/docker-compose-actions-workflow/actions)

This is a GitHub Actions workflow example to demonstrate building and testing a multi-container stack using `docker-compose` and send a message to Slack.

This sample is based on the [Get started with Docker Compose](https://docs.docker.com/compose/gettingstarted/) documentation.

## GitHub Actions Workflow

**push.yml**

```yml
name: docker-compose-actions-workflow
on: push
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Build the stack
        run: docker-compose up -d
      - name: Test
        run: docker run --network container:fastapi appropriate/curl -s --retry 10 --retry-connrefused http://http://127.0.0.1:8081/
```

You can browse a run for this example [here](https://github.com/peter-evans/docker-compose-actions-workflow/actions/workflows/push.yml).

For more about testing containers before release see [Smoke Testing](https://github.com/peter-evans/smoke-testing).

## License

[MIT](LICENSE)
