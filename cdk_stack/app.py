#!/usr/bin/env python3

from aws_cdk import core

from stack.base_stack import BaseStack
from stack.app_stack import AppStack

env_london = core.Environment(account="168481318803", region="eu-west-2")

app = core.App()

main_stack = core.Stack(app, 'main-stack', env=env_london)
base_stack = BaseStack(main_stack, "test-base-stack", env=env_london)
app_stack = AppStack(main_stack,
                     "test-app-stack",
                     cluster=base_stack.cluster,
                     public_load_balancer=base_stack.public_load_balancer, env=env_london)

app.synth()
