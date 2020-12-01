from aws_cdk import aws_ec2 as ec2
from aws_cdk import aws_ecs as ecs
from aws_cdk import aws_elasticloadbalancingv2 as elbv2
from aws_cdk import core
from aws_cdk import aws_ecs_patterns as ecs_patterns


class AppStack(core.NestedStack):
    def __init__(self, scope: core.Construct, id: str, cluster: ecs.Cluster,
                 public_load_balancer: elbv2.ApplicationLoadBalancer,
                 **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        asset_image: ecs.AssetImage = ecs.ContainerImage.from_asset('../app')

        ecs_patterns.ApplicationLoadBalancedFargateService(
            self,
            "MyFastApi",
            cluster=cluster,
            load_balancer=public_load_balancer,
            task_image_options=ecs_patterns.
            ApplicationLoadBalancedTaskImageOptions(
                image=asset_image,
                container_name='my-fast-api',
                container_port=8000,
                enable_logging=True,
            ))
