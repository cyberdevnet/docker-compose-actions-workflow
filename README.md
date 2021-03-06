# docker-compose-actions-workflow

[![Actions Status](https://github.com/cyberdevnet/docker-compose-actions-workflow/workflows/docker-compose-actions-workflow/badge.svg)](https://github.com/cyberdevnet/docker-compose-actions-workflow/actions)

This is a GitHub Actions workflow example to demonstrate building and testing a multi-container stack using `docker-compose` and send a message to a Slack channel.

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
        run: docker-compose -f dockerfiles/docker-compose.yml up -d
      - name: Test telnet mongodb
        run: docker run --network container:fastapi-action-workflow mikesplain/telnet mongodb 27017
      - name: Test simple GET
        run: docker run --network container:fastapi-action-workflow jwilder/dockerize -wait http://127.0.0.1:8000/ -timeout 120s -wait-retry-interval 5s
      - name: Test curl GET
        run: docker run --network container:fastapi-action-workflow appropriate/curl -X GET http://127.0.0.1:8000
      - name: Test curl POST
        run: >-
          docker run --network container:fastapi-action-workflow appropriate/curl  -X POST -H 'Content-type: application/json'
          --data '{"message":"This is a test from Github actions"}' http://127.0.0.1:8000/post
      - name: Test FastAPI docs
        run: docker run --network container:fastapi-action-workflow jwilder/dockerize -wait http://127.0.0.1:8000/docs -timeout 120s -wait-retry-interval 5s
  slack:
    needs: test
    runs-on: ubuntu-latest
    steps:
      - uses: 8398a7/action-slack@v3
        with:
          status: ${{ job.status }}
          fields: repo,message,commit,author,action,eventName,ref,workflow,job,took,pullRequest # selectable (default: repo,message)
        env:
          SLACK_WEBHOOK_URL: ${{ secrets.SLACK_WEBHOOK_URL }} # required
        if: always() # Pick up events even if the job fails or is canceled.}
```

## License

[MIT](LICENSE)
