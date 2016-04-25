# ChatOps + StackStorm tutorial pack

A small pack for showcasing ChatOps capabilities in StackStorm.

### Actions

1. `repeat.yaml`: a simple echo action to use with an alias.

2. `fail_on_odd.yaml`: a workflow failing every other minute; utilizes `chatops.post_message` to demonstrate notifications.

3. `fail_on_odd_silent.yaml`: same workflow sans `post_message` to launch with an alias and get the full result.

### Aliases

1. `noop.yaml`: a very simple no-op alias to demonstrate how aliases work in general.

2. `repeat.yaml`: an extended alias with most extra parameters in use.

3. `fail_on_odd_silent.yaml`: an alias for the `fail_on_odd_silent` workflow, outputting the whole result object. Meant to show how much variables and objects you can use in your Jinja template.

4. `repeat-14.yaml`: an alias with experimental 1.4 features: slack attachment API parameters and two-factor auth.

5. `mock-*.yaml`: aliases for showcasing ChatOps formatting (note: the syntax will change in the future).
