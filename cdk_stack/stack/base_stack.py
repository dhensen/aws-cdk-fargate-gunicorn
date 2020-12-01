from aws_cdk import aws_ec2 as ec2
from aws_cdk import aws_ecs as ecs
from aws_cdk import aws_elasticloadbalancingv2 as elbv2
from aws_cdk import core


class BaseStack(core.NestedStack):
    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        vpc = ec2.Vpc.from_lookup(self, 'default-vpc', vpc_id='vpc-0ed3aa66')
        cluster = ecs.Cluster(self, "default-cluster", vpc=vpc)
        public_load_balancer = elbv2.ApplicationLoadBalancer(
            self,
            'default-alb',
            vpc=vpc,
            internet_facing=True,
            vpc_subnets=ec2.SubnetSelection(one_per_az=True,
                                            subnet_type=ec2.SubnetType.PUBLIC))

        self.vpc = vpc
        self.cluster = cluster
        self.public_load_balancer = public_load_balancer
