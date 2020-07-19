---
title: mocha-github-reporter v1.0.0
date: 2017-03-11 04:00:00
tags: ["nodejs", "npm", "programming", "software", "testing", "library"]
---

Mocha stays very closer to me than any other test framework, I have worked with. I love reading and writing idiomatic code. The best thing about all the fancy libraries out there is that they help us write idiomatic code.

They drag us into their own world. They give some primitive structures and give us the tools. They help you think in a different way ( right way ), that makes writing code easier and more intuitive.

### CI Workflow

A lot of companies and projects employ [Continuous Integration](https://en.wikipedia.org/wiki/Continuous_integration) ( often mentioned as CI ). These [CI systems](https://github.com/ciandcd/awesome-ciandcd#online-build-system), enables running tests, generating coverage reports etc. whenever some code is merged in a project.

These tests run on different machine and is usually a one provided by a SaaS CI system. When tests fail or coverage is below expected, these CI systems notify it via their web dashboards, Messaging apps like [Slack](https://slack.com/), [Gitter](https://gitter.im/) etc.

![Web dashboard notification for test failures. ( CI System : [Shippable](https://app.shippable.com/) )](https://cdn-images-1.medium.com/max/2078/1*1JvQ9h1ua4TBHiBl-I4OsA.png)*Web dashboard notification for test failures. ( CI System : [Shippable](https://app.shippable.com/) )*

![Web Dashboard reports passing of tests](https://cdn-images-1.medium.com/max/2842/1*CxuloN6dl65GqeT1pjGOAQ.png)*Web Dashboard reports passing of tests*

### Github Issues

[Github](https://github.com/) issue tracker is a great tool to work on software projects. It helps in reporting, tracking and triaging bugs, feature requests etc.

A most commonly seen workflow looks like this. When one person merges some code to the master branch ( the final branch ), CI system triggers and reports the error in web dashboard. The project maintainer or someone else observes it and opens an issue in github and marks it with appropriate label. The person who broke the build or someone else merges the fix until the build becomes green and closes the github issue finally.

People usually ( at least me ) often go to the web dashboard of CI systems, only when the build fails and copy paste the failed test details in a github issue.

### Automating Github Issue Creation

I have seen code, that couples reporting the test results inside the mocha tests itself.

```javascript
// WARNING: Following code snippet is a bad practice.

describe('test suite', function () {
  // store failed tests for reporting
  var failedTests = [];

  it('test case 1', function () {
     // some test

  });

  it('test case 1', function () {
     // some test

  });

  after(function () {
     if (failedTests.length > 0) {
       // make HTTP call to create github issue

     }

  });

});
```

As you might guess, this after function gets copied to all the test case files and results in duplicated code all over.

After reading code like this somewhere, I started asking myself the some basic questions

1.What can be done to avoid such duplication ?

2. What is the right abstraction that separates the tests from how it is reported ?

After browsing through mocha docs, I happened to discover [mocha reporters](https://mochajs.org/#reporters).

### Mocha Reporters

Once the tests are complete, mocha reporters are interfaces that report the test results to the developer visually. They range from fancy formatted text output to html outputs.

So, this was the thing I was talking about in the beginning. Reporters is just a abstraction provided by mocha to present your test data.

I decided to quickly rollout a library that can be used as devDependency in a project.

### Meet mocha-github-reporter

Its a custom mocha reporter, that can be used to report mocha test results as a github issue from various CI systems.

Its published in [npm](https://www.npmjs.com/package/mocha-github-reporter) and its source code is available open on [github](https://github.com/scriptnull/mocha-github-reporter).

### Install

It can be installed as devDependency via npm

    $ npm install --save-dev mocha-github-reporter

### Usage

Setting it up should be straight forward. The required environment variables has to be set first.

* GITHUB_ACCESS_TOKEN— It can be generated [here](https://github.com/settings/tokens). Make sure that, you don’t expose this token and have it as a secure environment variable in your CI system.

* GITHUB_REPO_SLUG — Github repository where the issue has to be created for test results.

* REPORT_TITLE — Title for the issue to be created. It can use CI specific environment variables to be more relevant. For example: Mocha report for Build $BUILD_NUMBER

* REPORT_ALWAYS — By default, Github issue is created only when tests fail. Setting this variable to true will create a Github issue, even if all the tests passed.

* REPORT_FORMATTER — There are different formatters available inbuilt. We will be seeing them one by one down below.

Once the required environment variables are set, we just need to run mocha.

    $ mocha --reporter mocha-github-reporter tests/

### Formatters

Following formatters used by settingREPORT_FORMATTER environment variable.

**all-suites**

This is the default formatter and gives similar feel to default mocha reporter

![](https://cdn-images-1.medium.com/max/2752/1*cGiVhnYZlSdhWgvSfR0DIQ.png)

**all-suites-emoji**

Where is the fun, if we don’t have an emoji reporter ?

emoji can be configured via PASSED_EMOJI and FAILED_EMOJI environment variables.

![](https://cdn-images-1.medium.com/max/2752/1*jMOFzGvv7SK3I-rvfW4L3w.png)

**failed-checklist**

This is a very opinionated format. I have seen workflows, where people create checklist for failed tests and clear them off one by one.

![](https://cdn-images-1.medium.com/max/2752/1*pZuUKEYtawFcsAM9kKHELg.png)

That’s it. We have decoupled the code for reporting test results from the actual tests.

Thanks for taking time to read this. Please free to share your suggestions and thoughts around this.

### Quick Links

* Github — [https://github.com/scriptnull/mocha-github-reporter](https://github.com/scriptnull/mocha-github-reporter)

* npm — [https://www.npmjs.com/package/mocha-github-reporter](https://www.npmjs.com/package/mocha-github-reporter)
