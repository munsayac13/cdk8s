from pkgutil import extend_path
__path__ = extend_path(__path__, __name__)

import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

import typeguard
from importlib.metadata import version as _metadata_package_version
TYPEGUARD_MAJOR_VERSION = int(_metadata_package_version('typeguard').split('.')[0])

def check_type(argname: str, value: object, expected_type: typing.Any) -> typing.Any:
    if TYPEGUARD_MAJOR_VERSION <= 2:
        return typeguard.check_type(argname=argname, value=value, expected_type=expected_type) # type:ignore
    else:
        if isinstance(value, jsii._reference_map.InterfaceDynamicProxy): # pyright: ignore [reportAttributeAccessIssue]
           pass
        else:
            if TYPEGUARD_MAJOR_VERSION == 3:
                typeguard.config.collection_check_strategy = typeguard.CollectionCheckStrategy.ALL_ITEMS # type:ignore
                typeguard.check_type(value=value, expected_type=expected_type) # type:ignore
            else:
                typeguard.check_type(value=value, expected_type=expected_type, collection_check_strategy=typeguard.CollectionCheckStrategy.ALL_ITEMS) # type:ignore

from ._jsii import *

import constructs as _constructs_77d1e7e8


@jsii.data_type(
    jsii_type="external-secrets.ExternalSecretsAffinity",
    jsii_struct_bases=[],
    name_mapping={"additional_values": "additionalValues"},
)
class ExternalSecretsAffinity:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: ExternalSecretsAffinity
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bcfdeb8435e2b021e54a939e07980eeadb785975e74e8e6fce1e6182f6f995fa)
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_values is not None:
            self._values["additional_values"] = additional_values

    @builtins.property
    def additional_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: ExternalSecretsAffinity#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ExternalSecretsAffinity(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="external-secrets.ExternalSecretsCertController",
    jsii_struct_bases=[],
    name_mapping={
        "additional_values": "additionalValues",
        "affinity": "affinity",
        "create": "create",
        "deployment_annotations": "deploymentAnnotations",
        "extra_args": "extraArgs",
        "extra_env": "extraEnv",
        "extra_volume_mounts": "extraVolumeMounts",
        "extra_volumes": "extraVolumes",
        "fullname_override": "fullnameOverride",
        "host_network": "hostNetwork",
        "image": "image",
        "image_pull_secrets": "imagePullSecrets",
        "log": "log",
        "metrics": "metrics",
        "name_override": "nameOverride",
        "node_selector": "nodeSelector",
        "pod_annotations": "podAnnotations",
        "pod_disruption_budget": "podDisruptionBudget",
        "pod_labels": "podLabels",
        "pod_security_context": "podSecurityContext",
        "priority_class_name": "priorityClassName",
        "rbac": "rbac",
        "readiness_probe": "readinessProbe",
        "replica_count": "replicaCount",
        "requeue_interval": "requeueInterval",
        "resources": "resources",
        "revision_history_limit": "revisionHistoryLimit",
        "security_context": "securityContext",
        "service_account": "serviceAccount",
        "tolerations": "tolerations",
        "topology_spread_constraints": "topologySpreadConstraints",
    },
)
class ExternalSecretsCertController:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        affinity: typing.Optional[typing.Union["ExternalSecretsCertControllerAffinity", typing.Dict[builtins.str, typing.Any]]] = None,
        create: typing.Optional[builtins.bool] = None,
        deployment_annotations: typing.Optional[typing.Union["ExternalSecretsCertControllerDeploymentAnnotations", typing.Dict[builtins.str, typing.Any]]] = None,
        extra_args: typing.Optional[typing.Union["ExternalSecretsCertControllerExtraArgs", typing.Dict[builtins.str, typing.Any]]] = None,
        extra_env: typing.Optional[typing.Sequence[typing.Any]] = None,
        extra_volume_mounts: typing.Optional[typing.Sequence[typing.Any]] = None,
        extra_volumes: typing.Optional[typing.Sequence[typing.Any]] = None,
        fullname_override: typing.Optional[builtins.str] = None,
        host_network: typing.Optional[builtins.bool] = None,
        image: typing.Optional[typing.Union["ExternalSecretsCertControllerImage", typing.Dict[builtins.str, typing.Any]]] = None,
        image_pull_secrets: typing.Optional[typing.Sequence[typing.Any]] = None,
        log: typing.Optional[typing.Union["ExternalSecretsCertControllerLog", typing.Dict[builtins.str, typing.Any]]] = None,
        metrics: typing.Optional[typing.Union["ExternalSecretsCertControllerMetrics", typing.Dict[builtins.str, typing.Any]]] = None,
        name_override: typing.Optional[builtins.str] = None,
        node_selector: typing.Optional[typing.Union["ExternalSecretsCertControllerNodeSelector", typing.Dict[builtins.str, typing.Any]]] = None,
        pod_annotations: typing.Optional[typing.Union["ExternalSecretsCertControllerPodAnnotations", typing.Dict[builtins.str, typing.Any]]] = None,
        pod_disruption_budget: typing.Optional[typing.Union["ExternalSecretsCertControllerPodDisruptionBudget", typing.Dict[builtins.str, typing.Any]]] = None,
        pod_labels: typing.Optional[typing.Union["ExternalSecretsCertControllerPodLabels", typing.Dict[builtins.str, typing.Any]]] = None,
        pod_security_context: typing.Optional[typing.Union["ExternalSecretsCertControllerPodSecurityContext", typing.Dict[builtins.str, typing.Any]]] = None,
        priority_class_name: typing.Optional[builtins.str] = None,
        rbac: typing.Optional[typing.Union["ExternalSecretsCertControllerRbac", typing.Dict[builtins.str, typing.Any]]] = None,
        readiness_probe: typing.Optional[typing.Union["ExternalSecretsCertControllerReadinessProbe", typing.Dict[builtins.str, typing.Any]]] = None,
        replica_count: typing.Optional[jsii.Number] = None,
        requeue_interval: typing.Optional[builtins.str] = None,
        resources: typing.Optional[typing.Union["ExternalSecretsCertControllerResources", typing.Dict[builtins.str, typing.Any]]] = None,
        revision_history_limit: typing.Optional[jsii.Number] = None,
        security_context: typing.Optional[typing.Union["ExternalSecretsCertControllerSecurityContext", typing.Dict[builtins.str, typing.Any]]] = None,
        service_account: typing.Optional[typing.Union["ExternalSecretsCertControllerServiceAccount", typing.Dict[builtins.str, typing.Any]]] = None,
        tolerations: typing.Optional[typing.Sequence[typing.Any]] = None,
        topology_spread_constraints: typing.Optional[typing.Sequence[typing.Any]] = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.
        :param affinity: 
        :param create: 
        :param deployment_annotations: 
        :param extra_args: 
        :param extra_env: 
        :param extra_volume_mounts: 
        :param extra_volumes: 
        :param fullname_override: 
        :param host_network: 
        :param image: 
        :param image_pull_secrets: 
        :param log: 
        :param metrics: 
        :param name_override: 
        :param node_selector: 
        :param pod_annotations: 
        :param pod_disruption_budget: 
        :param pod_labels: 
        :param pod_security_context: 
        :param priority_class_name: 
        :param rbac: 
        :param readiness_probe: 
        :param replica_count: 
        :param requeue_interval: 
        :param resources: 
        :param revision_history_limit: 
        :param security_context: 
        :param service_account: 
        :param tolerations: 
        :param topology_spread_constraints: 

        :schema: ExternalSecretsCertController
        '''
        if isinstance(affinity, dict):
            affinity = ExternalSecretsCertControllerAffinity(**affinity)
        if isinstance(deployment_annotations, dict):
            deployment_annotations = ExternalSecretsCertControllerDeploymentAnnotations(**deployment_annotations)
        if isinstance(extra_args, dict):
            extra_args = ExternalSecretsCertControllerExtraArgs(**extra_args)
        if isinstance(image, dict):
            image = ExternalSecretsCertControllerImage(**image)
        if isinstance(log, dict):
            log = ExternalSecretsCertControllerLog(**log)
        if isinstance(metrics, dict):
            metrics = ExternalSecretsCertControllerMetrics(**metrics)
        if isinstance(node_selector, dict):
            node_selector = ExternalSecretsCertControllerNodeSelector(**node_selector)
        if isinstance(pod_annotations, dict):
            pod_annotations = ExternalSecretsCertControllerPodAnnotations(**pod_annotations)
        if isinstance(pod_disruption_budget, dict):
            pod_disruption_budget = ExternalSecretsCertControllerPodDisruptionBudget(**pod_disruption_budget)
        if isinstance(pod_labels, dict):
            pod_labels = ExternalSecretsCertControllerPodLabels(**pod_labels)
        if isinstance(pod_security_context, dict):
            pod_security_context = ExternalSecretsCertControllerPodSecurityContext(**pod_security_context)
        if isinstance(rbac, dict):
            rbac = ExternalSecretsCertControllerRbac(**rbac)
        if isinstance(readiness_probe, dict):
            readiness_probe = ExternalSecretsCertControllerReadinessProbe(**readiness_probe)
        if isinstance(resources, dict):
            resources = ExternalSecretsCertControllerResources(**resources)
        if isinstance(security_context, dict):
            security_context = ExternalSecretsCertControllerSecurityContext(**security_context)
        if isinstance(service_account, dict):
            service_account = ExternalSecretsCertControllerServiceAccount(**service_account)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__687fa9c52b549d2ea7722211c58720c96e30f3932231ff2a88ca777a9bc82ca1)
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
            check_type(argname="argument affinity", value=affinity, expected_type=type_hints["affinity"])
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
            check_type(argname="argument deployment_annotations", value=deployment_annotations, expected_type=type_hints["deployment_annotations"])
            check_type(argname="argument extra_args", value=extra_args, expected_type=type_hints["extra_args"])
            check_type(argname="argument extra_env", value=extra_env, expected_type=type_hints["extra_env"])
            check_type(argname="argument extra_volume_mounts", value=extra_volume_mounts, expected_type=type_hints["extra_volume_mounts"])
            check_type(argname="argument extra_volumes", value=extra_volumes, expected_type=type_hints["extra_volumes"])
            check_type(argname="argument fullname_override", value=fullname_override, expected_type=type_hints["fullname_override"])
            check_type(argname="argument host_network", value=host_network, expected_type=type_hints["host_network"])
            check_type(argname="argument image", value=image, expected_type=type_hints["image"])
            check_type(argname="argument image_pull_secrets", value=image_pull_secrets, expected_type=type_hints["image_pull_secrets"])
            check_type(argname="argument log", value=log, expected_type=type_hints["log"])
            check_type(argname="argument metrics", value=metrics, expected_type=type_hints["metrics"])
            check_type(argname="argument name_override", value=name_override, expected_type=type_hints["name_override"])
            check_type(argname="argument node_selector", value=node_selector, expected_type=type_hints["node_selector"])
            check_type(argname="argument pod_annotations", value=pod_annotations, expected_type=type_hints["pod_annotations"])
            check_type(argname="argument pod_disruption_budget", value=pod_disruption_budget, expected_type=type_hints["pod_disruption_budget"])
            check_type(argname="argument pod_labels", value=pod_labels, expected_type=type_hints["pod_labels"])
            check_type(argname="argument pod_security_context", value=pod_security_context, expected_type=type_hints["pod_security_context"])
            check_type(argname="argument priority_class_name", value=priority_class_name, expected_type=type_hints["priority_class_name"])
            check_type(argname="argument rbac", value=rbac, expected_type=type_hints["rbac"])
            check_type(argname="argument readiness_probe", value=readiness_probe, expected_type=type_hints["readiness_probe"])
            check_type(argname="argument replica_count", value=replica_count, expected_type=type_hints["replica_count"])
            check_type(argname="argument requeue_interval", value=requeue_interval, expected_type=type_hints["requeue_interval"])
            check_type(argname="argument resources", value=resources, expected_type=type_hints["resources"])
            check_type(argname="argument revision_history_limit", value=revision_history_limit, expected_type=type_hints["revision_history_limit"])
            check_type(argname="argument security_context", value=security_context, expected_type=type_hints["security_context"])
            check_type(argname="argument service_account", value=service_account, expected_type=type_hints["service_account"])
            check_type(argname="argument tolerations", value=tolerations, expected_type=type_hints["tolerations"])
            check_type(argname="argument topology_spread_constraints", value=topology_spread_constraints, expected_type=type_hints["topology_spread_constraints"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_values is not None:
            self._values["additional_values"] = additional_values
        if affinity is not None:
            self._values["affinity"] = affinity
        if create is not None:
            self._values["create"] = create
        if deployment_annotations is not None:
            self._values["deployment_annotations"] = deployment_annotations
        if extra_args is not None:
            self._values["extra_args"] = extra_args
        if extra_env is not None:
            self._values["extra_env"] = extra_env
        if extra_volume_mounts is not None:
            self._values["extra_volume_mounts"] = extra_volume_mounts
        if extra_volumes is not None:
            self._values["extra_volumes"] = extra_volumes
        if fullname_override is not None:
            self._values["fullname_override"] = fullname_override
        if host_network is not None:
            self._values["host_network"] = host_network
        if image is not None:
            self._values["image"] = image
        if image_pull_secrets is not None:
            self._values["image_pull_secrets"] = image_pull_secrets
        if log is not None:
            self._values["log"] = log
        if metrics is not None:
            self._values["metrics"] = metrics
        if name_override is not None:
            self._values["name_override"] = name_override
        if node_selector is not None:
            self._values["node_selector"] = node_selector
        if pod_annotations is not None:
            self._values["pod_annotations"] = pod_annotations
        if pod_disruption_budget is not None:
            self._values["pod_disruption_budget"] = pod_disruption_budget
        if pod_labels is not None:
            self._values["pod_labels"] = pod_labels
        if pod_security_context is not None:
            self._values["pod_security_context"] = pod_security_context
        if priority_class_name is not None:
            self._values["priority_class_name"] = priority_class_name
        if rbac is not None:
            self._values["rbac"] = rbac
        if readiness_probe is not None:
            self._values["readiness_probe"] = readiness_probe
        if replica_count is not None:
            self._values["replica_count"] = replica_count
        if requeue_interval is not None:
            self._values["requeue_interval"] = requeue_interval
        if resources is not None:
            self._values["resources"] = resources
        if revision_history_limit is not None:
            self._values["revision_history_limit"] = revision_history_limit
        if security_context is not None:
            self._values["security_context"] = security_context
        if service_account is not None:
            self._values["service_account"] = service_account
        if tolerations is not None:
            self._values["tolerations"] = tolerations
        if topology_spread_constraints is not None:
            self._values["topology_spread_constraints"] = topology_spread_constraints

    @builtins.property
    def additional_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: ExternalSecretsCertController#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def affinity(self) -> typing.Optional["ExternalSecretsCertControllerAffinity"]:
        '''
        :schema: ExternalSecretsCertController#affinity
        '''
        result = self._values.get("affinity")
        return typing.cast(typing.Optional["ExternalSecretsCertControllerAffinity"], result)

    @builtins.property
    def create(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: ExternalSecretsCertController#create
        '''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def deployment_annotations(
        self,
    ) -> typing.Optional["ExternalSecretsCertControllerDeploymentAnnotations"]:
        '''
        :schema: ExternalSecretsCertController#deploymentAnnotations
        '''
        result = self._values.get("deployment_annotations")
        return typing.cast(typing.Optional["ExternalSecretsCertControllerDeploymentAnnotations"], result)

    @builtins.property
    def extra_args(self) -> typing.Optional["ExternalSecretsCertControllerExtraArgs"]:
        '''
        :schema: ExternalSecretsCertController#extraArgs
        '''
        result = self._values.get("extra_args")
        return typing.cast(typing.Optional["ExternalSecretsCertControllerExtraArgs"], result)

    @builtins.property
    def extra_env(self) -> typing.Optional[typing.List[typing.Any]]:
        '''
        :schema: ExternalSecretsCertController#extraEnv
        '''
        result = self._values.get("extra_env")
        return typing.cast(typing.Optional[typing.List[typing.Any]], result)

    @builtins.property
    def extra_volume_mounts(self) -> typing.Optional[typing.List[typing.Any]]:
        '''
        :schema: ExternalSecretsCertController#extraVolumeMounts
        '''
        result = self._values.get("extra_volume_mounts")
        return typing.cast(typing.Optional[typing.List[typing.Any]], result)

    @builtins.property
    def extra_volumes(self) -> typing.Optional[typing.List[typing.Any]]:
        '''
        :schema: ExternalSecretsCertController#extraVolumes
        '''
        result = self._values.get("extra_volumes")
        return typing.cast(typing.Optional[typing.List[typing.Any]], result)

    @builtins.property
    def fullname_override(self) -> typing.Optional[builtins.str]:
        '''
        :schema: ExternalSecretsCertController#fullnameOverride
        '''
        result = self._values.get("fullname_override")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def host_network(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: ExternalSecretsCertController#hostNetwork
        '''
        result = self._values.get("host_network")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def image(self) -> typing.Optional["ExternalSecretsCertControllerImage"]:
        '''
        :schema: ExternalSecretsCertController#image
        '''
        result = self._values.get("image")
        return typing.cast(typing.Optional["ExternalSecretsCertControllerImage"], result)

    @builtins.property
    def image_pull_secrets(self) -> typing.Optional[typing.List[typing.Any]]:
        '''
        :schema: ExternalSecretsCertController#imagePullSecrets
        '''
        result = self._values.get("image_pull_secrets")
        return typing.cast(typing.Optional[typing.List[typing.Any]], result)

    @builtins.property
    def log(self) -> typing.Optional["ExternalSecretsCertControllerLog"]:
        '''
        :schema: ExternalSecretsCertController#log
        '''
        result = self._values.get("log")
        return typing.cast(typing.Optional["ExternalSecretsCertControllerLog"], result)

    @builtins.property
    def metrics(self) -> typing.Optional["ExternalSecretsCertControllerMetrics"]:
        '''
        :schema: ExternalSecretsCertController#metrics
        '''
        result = self._values.get("metrics")
        return typing.cast(typing.Optional["ExternalSecretsCertControllerMetrics"], result)

    @builtins.property
    def name_override(self) -> typing.Optional[builtins.str]:
        '''
        :schema: ExternalSecretsCertController#nameOverride
        '''
        result = self._values.get("name_override")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def node_selector(
        self,
    ) -> typing.Optional["ExternalSecretsCertControllerNodeSelector"]:
        '''
        :schema: ExternalSecretsCertController#nodeSelector
        '''
        result = self._values.get("node_selector")
        return typing.cast(typing.Optional["ExternalSecretsCertControllerNodeSelector"], result)

    @builtins.property
    def pod_annotations(
        self,
    ) -> typing.Optional["ExternalSecretsCertControllerPodAnnotations"]:
        '''
        :schema: ExternalSecretsCertController#podAnnotations
        '''
        result = self._values.get("pod_annotations")
        return typing.cast(typing.Optional["ExternalSecretsCertControllerPodAnnotations"], result)

    @builtins.property
    def pod_disruption_budget(
        self,
    ) -> typing.Optional["ExternalSecretsCertControllerPodDisruptionBudget"]:
        '''
        :schema: ExternalSecretsCertController#podDisruptionBudget
        '''
        result = self._values.get("pod_disruption_budget")
        return typing.cast(typing.Optional["ExternalSecretsCertControllerPodDisruptionBudget"], result)

    @builtins.property
    def pod_labels(self) -> typing.Optional["ExternalSecretsCertControllerPodLabels"]:
        '''
        :schema: ExternalSecretsCertController#podLabels
        '''
        result = self._values.get("pod_labels")
        return typing.cast(typing.Optional["ExternalSecretsCertControllerPodLabels"], result)

    @builtins.property
    def pod_security_context(
        self,
    ) -> typing.Optional["ExternalSecretsCertControllerPodSecurityContext"]:
        '''
        :schema: ExternalSecretsCertController#podSecurityContext
        '''
        result = self._values.get("pod_security_context")
        return typing.cast(typing.Optional["ExternalSecretsCertControllerPodSecurityContext"], result)

    @builtins.property
    def priority_class_name(self) -> typing.Optional[builtins.str]:
        '''
        :schema: ExternalSecretsCertController#priorityClassName
        '''
        result = self._values.get("priority_class_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def rbac(self) -> typing.Optional["ExternalSecretsCertControllerRbac"]:
        '''
        :schema: ExternalSecretsCertController#rbac
        '''
        result = self._values.get("rbac")
        return typing.cast(typing.Optional["ExternalSecretsCertControllerRbac"], result)

    @builtins.property
    def readiness_probe(
        self,
    ) -> typing.Optional["ExternalSecretsCertControllerReadinessProbe"]:
        '''
        :schema: ExternalSecretsCertController#readinessProbe
        '''
        result = self._values.get("readiness_probe")
        return typing.cast(typing.Optional["ExternalSecretsCertControllerReadinessProbe"], result)

    @builtins.property
    def replica_count(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: ExternalSecretsCertController#replicaCount
        '''
        result = self._values.get("replica_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def requeue_interval(self) -> typing.Optional[builtins.str]:
        '''
        :schema: ExternalSecretsCertController#requeueInterval
        '''
        result = self._values.get("requeue_interval")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def resources(self) -> typing.Optional["ExternalSecretsCertControllerResources"]:
        '''
        :schema: ExternalSecretsCertController#resources
        '''
        result = self._values.get("resources")
        return typing.cast(typing.Optional["ExternalSecretsCertControllerResources"], result)

    @builtins.property
    def revision_history_limit(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: ExternalSecretsCertController#revisionHistoryLimit
        '''
        result = self._values.get("revision_history_limit")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def security_context(
        self,
    ) -> typing.Optional["ExternalSecretsCertControllerSecurityContext"]:
        '''
        :schema: ExternalSecretsCertController#securityContext
        '''
        result = self._values.get("security_context")
        return typing.cast(typing.Optional["ExternalSecretsCertControllerSecurityContext"], result)

    @builtins.property
    def service_account(
        self,
    ) -> typing.Optional["ExternalSecretsCertControllerServiceAccount"]:
        '''
        :schema: ExternalSecretsCertController#serviceAccount
        '''
        result = self._values.get("service_account")
        return typing.cast(typing.Optional["ExternalSecretsCertControllerServiceAccount"], result)

    @builtins.property
    def tolerations(self) -> typing.Optional[typing.List[typing.Any]]:
        '''
        :schema: ExternalSecretsCertController#tolerations
        '''
        result = self._values.get("tolerations")
        return typing.cast(typing.Optional[typing.List[typing.Any]], result)

    @builtins.property
    def topology_spread_constraints(self) -> typing.Optional[typing.List[typing.Any]]:
        '''
        :schema: ExternalSecretsCertController#topologySpreadConstraints
        '''
        result = self._values.get("topology_spread_constraints")
        return typing.cast(typing.Optional[typing.List[typing.Any]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ExternalSecretsCertController(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="external-secrets.ExternalSecretsCertControllerAffinity",
    jsii_struct_bases=[],
    name_mapping={"additional_values": "additionalValues"},
)
class ExternalSecretsCertControllerAffinity:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: ExternalSecretsCertControllerAffinity
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__92aec26eca28fe021d3520067a9f493e0c4718c13ca457f03a69b7fb2543aa81)
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_values is not None:
            self._values["additional_values"] = additional_values

    @builtins.property
    def additional_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: ExternalSecretsCertControllerAffinity#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ExternalSecretsCertControllerAffinity(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="external-secrets.ExternalSecretsCertControllerDeploymentAnnotations",
    jsii_struct_bases=[],
    name_mapping={"additional_values": "additionalValues"},
)
class ExternalSecretsCertControllerDeploymentAnnotations:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: ExternalSecretsCertControllerDeploymentAnnotations
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ca5a465d793b784a4bff4a4e74edc07ec32a1b1a07a17b00534a5f8f9728041a)
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_values is not None:
            self._values["additional_values"] = additional_values

    @builtins.property
    def additional_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: ExternalSecretsCertControllerDeploymentAnnotations#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ExternalSecretsCertControllerDeploymentAnnotations(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="external-secrets.ExternalSecretsCertControllerExtraArgs",
    jsii_struct_bases=[],
    name_mapping={"additional_values": "additionalValues"},
)
class ExternalSecretsCertControllerExtraArgs:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: ExternalSecretsCertControllerExtraArgs
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0f394daf0ace638c0c7721cdb76ab265c1e7b471cafebe66913c662bd596a2cf)
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_values is not None:
            self._values["additional_values"] = additional_values

    @builtins.property
    def additional_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: ExternalSecretsCertControllerExtraArgs#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ExternalSecretsCertControllerExtraArgs(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="external-secrets.ExternalSecretsCertControllerImage",
    jsii_struct_bases=[],
    name_mapping={
        "additional_values": "additionalValues",
        "flavour": "flavour",
        "pull_policy": "pullPolicy",
        "repository": "repository",
        "tag": "tag",
    },
)
class ExternalSecretsCertControllerImage:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        flavour: typing.Optional[builtins.str] = None,
        pull_policy: typing.Optional[builtins.str] = None,
        repository: typing.Optional[builtins.str] = None,
        tag: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.
        :param flavour: 
        :param pull_policy: 
        :param repository: 
        :param tag: 

        :schema: ExternalSecretsCertControllerImage
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__14ba0d28445356231ef5bd71adea29d3f103d881919bf62e49ce3a3a0a4054de)
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
            check_type(argname="argument flavour", value=flavour, expected_type=type_hints["flavour"])
            check_type(argname="argument pull_policy", value=pull_policy, expected_type=type_hints["pull_policy"])
            check_type(argname="argument repository", value=repository, expected_type=type_hints["repository"])
            check_type(argname="argument tag", value=tag, expected_type=type_hints["tag"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_values is not None:
            self._values["additional_values"] = additional_values
        if flavour is not None:
            self._values["flavour"] = flavour
        if pull_policy is not None:
            self._values["pull_policy"] = pull_policy
        if repository is not None:
            self._values["repository"] = repository
        if tag is not None:
            self._values["tag"] = tag

    @builtins.property
    def additional_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: ExternalSecretsCertControllerImage#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def flavour(self) -> typing.Optional[builtins.str]:
        '''
        :schema: ExternalSecretsCertControllerImage#flavour
        '''
        result = self._values.get("flavour")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def pull_policy(self) -> typing.Optional[builtins.str]:
        '''
        :schema: ExternalSecretsCertControllerImage#pullPolicy
        '''
        result = self._values.get("pull_policy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def repository(self) -> typing.Optional[builtins.str]:
        '''
        :schema: ExternalSecretsCertControllerImage#repository
        '''
        result = self._values.get("repository")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tag(self) -> typing.Optional[builtins.str]:
        '''
        :schema: ExternalSecretsCertControllerImage#tag
        '''
        result = self._values.get("tag")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ExternalSecretsCertControllerImage(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="external-secrets.ExternalSecretsCertControllerLog",
    jsii_struct_bases=[],
    name_mapping={
        "additional_values": "additionalValues",
        "level": "level",
        "time_encoding": "timeEncoding",
    },
)
class ExternalSecretsCertControllerLog:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        level: typing.Optional[builtins.str] = None,
        time_encoding: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.
        :param level: 
        :param time_encoding: 

        :schema: ExternalSecretsCertControllerLog
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__82dc057cfbf2674634b0c80ba1efa2057f00af186bb2ffe966e1dd0bb46f2748)
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
            check_type(argname="argument level", value=level, expected_type=type_hints["level"])
            check_type(argname="argument time_encoding", value=time_encoding, expected_type=type_hints["time_encoding"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_values is not None:
            self._values["additional_values"] = additional_values
        if level is not None:
            self._values["level"] = level
        if time_encoding is not None:
            self._values["time_encoding"] = time_encoding

    @builtins.property
    def additional_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: ExternalSecretsCertControllerLog#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def level(self) -> typing.Optional[builtins.str]:
        '''
        :schema: ExternalSecretsCertControllerLog#level
        '''
        result = self._values.get("level")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def time_encoding(self) -> typing.Optional[builtins.str]:
        '''
        :schema: ExternalSecretsCertControllerLog#timeEncoding
        '''
        result = self._values.get("time_encoding")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ExternalSecretsCertControllerLog(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="external-secrets.ExternalSecretsCertControllerMetrics",
    jsii_struct_bases=[],
    name_mapping={
        "additional_values": "additionalValues",
        "listen": "listen",
        "service": "service",
    },
)
class ExternalSecretsCertControllerMetrics:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        listen: typing.Optional[typing.Union["ExternalSecretsCertControllerMetricsListen", typing.Dict[builtins.str, typing.Any]]] = None,
        service: typing.Optional[typing.Union["ExternalSecretsCertControllerMetricsService", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.
        :param listen: 
        :param service: 

        :schema: ExternalSecretsCertControllerMetrics
        '''
        if isinstance(listen, dict):
            listen = ExternalSecretsCertControllerMetricsListen(**listen)
        if isinstance(service, dict):
            service = ExternalSecretsCertControllerMetricsService(**service)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8d68b0ea54d72ae51b7032ecbf4457e20d383493383f5a6b46bf585b6d59ba3d)
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
            check_type(argname="argument listen", value=listen, expected_type=type_hints["listen"])
            check_type(argname="argument service", value=service, expected_type=type_hints["service"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_values is not None:
            self._values["additional_values"] = additional_values
        if listen is not None:
            self._values["listen"] = listen
        if service is not None:
            self._values["service"] = service

    @builtins.property
    def additional_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: ExternalSecretsCertControllerMetrics#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def listen(self) -> typing.Optional["ExternalSecretsCertControllerMetricsListen"]:
        '''
        :schema: ExternalSecretsCertControllerMetrics#listen
        '''
        result = self._values.get("listen")
        return typing.cast(typing.Optional["ExternalSecretsCertControllerMetricsListen"], result)

    @builtins.property
    def service(self) -> typing.Optional["ExternalSecretsCertControllerMetricsService"]:
        '''
        :schema: ExternalSecretsCertControllerMetrics#service
        '''
        result = self._values.get("service")
        return typing.cast(typing.Optional["ExternalSecretsCertControllerMetricsService"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ExternalSecretsCertControllerMetrics(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="external-secrets.ExternalSecretsCertControllerMetricsListen",
    jsii_struct_bases=[],
    name_mapping={"additional_values": "additionalValues", "port": "port"},
)
class ExternalSecretsCertControllerMetricsListen:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        port: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.
        :param port: 

        :schema: ExternalSecretsCertControllerMetricsListen
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__051c18e4a965e7dde24a4186ea68b3f4a73c5058fe2e3c5f5b35610ec3d026c7)
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_values is not None:
            self._values["additional_values"] = additional_values
        if port is not None:
            self._values["port"] = port

    @builtins.property
    def additional_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: ExternalSecretsCertControllerMetricsListen#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def port(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: ExternalSecretsCertControllerMetricsListen#port
        '''
        result = self._values.get("port")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ExternalSecretsCertControllerMetricsListen(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="external-secrets.ExternalSecretsCertControllerMetricsService",
    jsii_struct_bases=[],
    name_mapping={
        "additional_values": "additionalValues",
        "annotations": "annotations",
        "enabled": "enabled",
        "port": "port",
    },
)
class ExternalSecretsCertControllerMetricsService:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        annotations: typing.Optional[typing.Union["ExternalSecretsCertControllerMetricsServiceAnnotations", typing.Dict[builtins.str, typing.Any]]] = None,
        enabled: typing.Optional[builtins.bool] = None,
        port: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.
        :param annotations: 
        :param enabled: 
        :param port: 

        :schema: ExternalSecretsCertControllerMetricsService
        '''
        if isinstance(annotations, dict):
            annotations = ExternalSecretsCertControllerMetricsServiceAnnotations(**annotations)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ea17ecb6401ce6b3f6752afb09a4c75617bacfea8b082dc20a556facfe41a72f)
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
            check_type(argname="argument annotations", value=annotations, expected_type=type_hints["annotations"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_values is not None:
            self._values["additional_values"] = additional_values
        if annotations is not None:
            self._values["annotations"] = annotations
        if enabled is not None:
            self._values["enabled"] = enabled
        if port is not None:
            self._values["port"] = port

    @builtins.property
    def additional_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: ExternalSecretsCertControllerMetricsService#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def annotations(
        self,
    ) -> typing.Optional["ExternalSecretsCertControllerMetricsServiceAnnotations"]:
        '''
        :schema: ExternalSecretsCertControllerMetricsService#annotations
        '''
        result = self._values.get("annotations")
        return typing.cast(typing.Optional["ExternalSecretsCertControllerMetricsServiceAnnotations"], result)

    @builtins.property
    def enabled(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: ExternalSecretsCertControllerMetricsService#enabled
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def port(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: ExternalSecretsCertControllerMetricsService#port
        '''
        result = self._values.get("port")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ExternalSecretsCertControllerMetricsService(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="external-secrets.ExternalSecretsCertControllerMetricsServiceAnnotations",
    jsii_struct_bases=[],
    name_mapping={"additional_values": "additionalValues"},
)
class ExternalSecretsCertControllerMetricsServiceAnnotations:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: ExternalSecretsCertControllerMetricsServiceAnnotations
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0bdfcc298f1c6aeaccfd729329be0ffd7e2ba4e24ffa1ab692075b83f1d4cf45)
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_values is not None:
            self._values["additional_values"] = additional_values

    @builtins.property
    def additional_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: ExternalSecretsCertControllerMetricsServiceAnnotations#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ExternalSecretsCertControllerMetricsServiceAnnotations(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="external-secrets.ExternalSecretsCertControllerNodeSelector",
    jsii_struct_bases=[],
    name_mapping={"additional_values": "additionalValues"},
)
class ExternalSecretsCertControllerNodeSelector:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: ExternalSecretsCertControllerNodeSelector
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2b8697752ad3d83476ff076921e0af7e0af04eb916f94c14996baee6e9a110d5)
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_values is not None:
            self._values["additional_values"] = additional_values

    @builtins.property
    def additional_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: ExternalSecretsCertControllerNodeSelector#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ExternalSecretsCertControllerNodeSelector(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="external-secrets.ExternalSecretsCertControllerPodAnnotations",
    jsii_struct_bases=[],
    name_mapping={"additional_values": "additionalValues"},
)
class ExternalSecretsCertControllerPodAnnotations:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: ExternalSecretsCertControllerPodAnnotations
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__205d9ec70d860e25aaa8da4626eb9732de613079701ade6ab1284fcb1a8ce4aa)
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_values is not None:
            self._values["additional_values"] = additional_values

    @builtins.property
    def additional_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: ExternalSecretsCertControllerPodAnnotations#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ExternalSecretsCertControllerPodAnnotations(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="external-secrets.ExternalSecretsCertControllerPodDisruptionBudget",
    jsii_struct_bases=[],
    name_mapping={
        "additional_values": "additionalValues",
        "enabled": "enabled",
        "min_available": "minAvailable",
    },
)
class ExternalSecretsCertControllerPodDisruptionBudget:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        enabled: typing.Optional[builtins.bool] = None,
        min_available: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.
        :param enabled: 
        :param min_available: 

        :schema: ExternalSecretsCertControllerPodDisruptionBudget
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9f710a6a96baa670c0031b764fd856afbbab8cac398923321aa7e269fe77daab)
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument min_available", value=min_available, expected_type=type_hints["min_available"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_values is not None:
            self._values["additional_values"] = additional_values
        if enabled is not None:
            self._values["enabled"] = enabled
        if min_available is not None:
            self._values["min_available"] = min_available

    @builtins.property
    def additional_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: ExternalSecretsCertControllerPodDisruptionBudget#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def enabled(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: ExternalSecretsCertControllerPodDisruptionBudget#enabled
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def min_available(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: ExternalSecretsCertControllerPodDisruptionBudget#minAvailable
        '''
        result = self._values.get("min_available")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ExternalSecretsCertControllerPodDisruptionBudget(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="external-secrets.ExternalSecretsCertControllerPodLabels",
    jsii_struct_bases=[],
    name_mapping={"additional_values": "additionalValues"},
)
class ExternalSecretsCertControllerPodLabels:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: ExternalSecretsCertControllerPodLabels
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7d77078db44cc4baf4e164a3fa045686091c37c6eff54146fb9988d78b37009a)
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_values is not None:
            self._values["additional_values"] = additional_values

    @builtins.property
    def additional_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: ExternalSecretsCertControllerPodLabels#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ExternalSecretsCertControllerPodLabels(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="external-secrets.ExternalSecretsCertControllerPodSecurityContext",
    jsii_struct_bases=[],
    name_mapping={"additional_values": "additionalValues", "enabled": "enabled"},
)
class ExternalSecretsCertControllerPodSecurityContext:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        enabled: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.
        :param enabled: 

        :schema: ExternalSecretsCertControllerPodSecurityContext
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6a2e36ddf3525a42c97be28e7e9cad07f7d487b2063c757d34a7e14e9beed540)
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_values is not None:
            self._values["additional_values"] = additional_values
        if enabled is not None:
            self._values["enabled"] = enabled

    @builtins.property
    def additional_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: ExternalSecretsCertControllerPodSecurityContext#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def enabled(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: ExternalSecretsCertControllerPodSecurityContext#enabled
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ExternalSecretsCertControllerPodSecurityContext(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="external-secrets.ExternalSecretsCertControllerRbac",
    jsii_struct_bases=[],
    name_mapping={"additional_values": "additionalValues", "create": "create"},
)
class ExternalSecretsCertControllerRbac:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        create: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.
        :param create: 

        :schema: ExternalSecretsCertControllerRbac
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1a51024eeffffbada0935443bb68ec72a709471513b3845628f93d7a23539f84)
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_values is not None:
            self._values["additional_values"] = additional_values
        if create is not None:
            self._values["create"] = create

    @builtins.property
    def additional_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: ExternalSecretsCertControllerRbac#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def create(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: ExternalSecretsCertControllerRbac#create
        '''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ExternalSecretsCertControllerRbac(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="external-secrets.ExternalSecretsCertControllerReadinessProbe",
    jsii_struct_bases=[],
    name_mapping={
        "additional_values": "additionalValues",
        "address": "address",
        "port": "port",
    },
)
class ExternalSecretsCertControllerReadinessProbe:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        address: typing.Optional[builtins.str] = None,
        port: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.
        :param address: 
        :param port: 

        :schema: ExternalSecretsCertControllerReadinessProbe
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__398dc3a22a319435302aaa283fdbde20b169b285abd7506b0c41744c31adc652)
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
            check_type(argname="argument address", value=address, expected_type=type_hints["address"])
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_values is not None:
            self._values["additional_values"] = additional_values
        if address is not None:
            self._values["address"] = address
        if port is not None:
            self._values["port"] = port

    @builtins.property
    def additional_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: ExternalSecretsCertControllerReadinessProbe#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def address(self) -> typing.Optional[builtins.str]:
        '''
        :schema: ExternalSecretsCertControllerReadinessProbe#address
        '''
        result = self._values.get("address")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def port(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: ExternalSecretsCertControllerReadinessProbe#port
        '''
        result = self._values.get("port")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ExternalSecretsCertControllerReadinessProbe(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="external-secrets.ExternalSecretsCertControllerResources",
    jsii_struct_bases=[],
    name_mapping={"additional_values": "additionalValues"},
)
class ExternalSecretsCertControllerResources:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: ExternalSecretsCertControllerResources
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__192f9fc09348d1fd178fb6819f9f949092c082e71c08c7a02c90ee0fd5c50809)
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_values is not None:
            self._values["additional_values"] = additional_values

    @builtins.property
    def additional_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: ExternalSecretsCertControllerResources#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ExternalSecretsCertControllerResources(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="external-secrets.ExternalSecretsCertControllerSecurityContext",
    jsii_struct_bases=[],
    name_mapping={
        "additional_values": "additionalValues",
        "allow_privilege_escalation": "allowPrivilegeEscalation",
        "capabilities": "capabilities",
        "enabled": "enabled",
        "read_only_root_filesystem": "readOnlyRootFilesystem",
        "run_as_non_root": "runAsNonRoot",
        "run_as_user": "runAsUser",
        "seccomp_profile": "seccompProfile",
    },
)
class ExternalSecretsCertControllerSecurityContext:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        allow_privilege_escalation: typing.Optional[builtins.bool] = None,
        capabilities: typing.Optional[typing.Union["ExternalSecretsCertControllerSecurityContextCapabilities", typing.Dict[builtins.str, typing.Any]]] = None,
        enabled: typing.Optional[builtins.bool] = None,
        read_only_root_filesystem: typing.Optional[builtins.bool] = None,
        run_as_non_root: typing.Optional[builtins.bool] = None,
        run_as_user: typing.Optional[jsii.Number] = None,
        seccomp_profile: typing.Optional[typing.Union["ExternalSecretsCertControllerSecurityContextSeccompProfile", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.
        :param allow_privilege_escalation: 
        :param capabilities: 
        :param enabled: 
        :param read_only_root_filesystem: 
        :param run_as_non_root: 
        :param run_as_user: 
        :param seccomp_profile: 

        :schema: ExternalSecretsCertControllerSecurityContext
        '''
        if isinstance(capabilities, dict):
            capabilities = ExternalSecretsCertControllerSecurityContextCapabilities(**capabilities)
        if isinstance(seccomp_profile, dict):
            seccomp_profile = ExternalSecretsCertControllerSecurityContextSeccompProfile(**seccomp_profile)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9999c12c8f58865c079ecdd1fa8d31ad09f6cac13a1e7ae44c1b819d4c9b0cfe)
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
            check_type(argname="argument allow_privilege_escalation", value=allow_privilege_escalation, expected_type=type_hints["allow_privilege_escalation"])
            check_type(argname="argument capabilities", value=capabilities, expected_type=type_hints["capabilities"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument read_only_root_filesystem", value=read_only_root_filesystem, expected_type=type_hints["read_only_root_filesystem"])
            check_type(argname="argument run_as_non_root", value=run_as_non_root, expected_type=type_hints["run_as_non_root"])
            check_type(argname="argument run_as_user", value=run_as_user, expected_type=type_hints["run_as_user"])
            check_type(argname="argument seccomp_profile", value=seccomp_profile, expected_type=type_hints["seccomp_profile"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_values is not None:
            self._values["additional_values"] = additional_values
        if allow_privilege_escalation is not None:
            self._values["allow_privilege_escalation"] = allow_privilege_escalation
        if capabilities is not None:
            self._values["capabilities"] = capabilities
        if enabled is not None:
            self._values["enabled"] = enabled
        if read_only_root_filesystem is not None:
            self._values["read_only_root_filesystem"] = read_only_root_filesystem
        if run_as_non_root is not None:
            self._values["run_as_non_root"] = run_as_non_root
        if run_as_user is not None:
            self._values["run_as_user"] = run_as_user
        if seccomp_profile is not None:
            self._values["seccomp_profile"] = seccomp_profile

    @builtins.property
    def additional_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: ExternalSecretsCertControllerSecurityContext#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def allow_privilege_escalation(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: ExternalSecretsCertControllerSecurityContext#allowPrivilegeEscalation
        '''
        result = self._values.get("allow_privilege_escalation")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def capabilities(
        self,
    ) -> typing.Optional["ExternalSecretsCertControllerSecurityContextCapabilities"]:
        '''
        :schema: ExternalSecretsCertControllerSecurityContext#capabilities
        '''
        result = self._values.get("capabilities")
        return typing.cast(typing.Optional["ExternalSecretsCertControllerSecurityContextCapabilities"], result)

    @builtins.property
    def enabled(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: ExternalSecretsCertControllerSecurityContext#enabled
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def read_only_root_filesystem(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: ExternalSecretsCertControllerSecurityContext#readOnlyRootFilesystem
        '''
        result = self._values.get("read_only_root_filesystem")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def run_as_non_root(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: ExternalSecretsCertControllerSecurityContext#runAsNonRoot
        '''
        result = self._values.get("run_as_non_root")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def run_as_user(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: ExternalSecretsCertControllerSecurityContext#runAsUser
        '''
        result = self._values.get("run_as_user")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def seccomp_profile(
        self,
    ) -> typing.Optional["ExternalSecretsCertControllerSecurityContextSeccompProfile"]:
        '''
        :schema: ExternalSecretsCertControllerSecurityContext#seccompProfile
        '''
        result = self._values.get("seccomp_profile")
        return typing.cast(typing.Optional["ExternalSecretsCertControllerSecurityContextSeccompProfile"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ExternalSecretsCertControllerSecurityContext(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="external-secrets.ExternalSecretsCertControllerSecurityContextCapabilities",
    jsii_struct_bases=[],
    name_mapping={"additional_values": "additionalValues", "drop": "drop"},
)
class ExternalSecretsCertControllerSecurityContextCapabilities:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        drop: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.
        :param drop: 

        :schema: ExternalSecretsCertControllerSecurityContextCapabilities
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a5f240720f28e8a202f349a14d84a56866f833b9403fb7e6220e1b9d12ca2c5e)
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
            check_type(argname="argument drop", value=drop, expected_type=type_hints["drop"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_values is not None:
            self._values["additional_values"] = additional_values
        if drop is not None:
            self._values["drop"] = drop

    @builtins.property
    def additional_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: ExternalSecretsCertControllerSecurityContextCapabilities#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def drop(self) -> typing.Optional[typing.List[builtins.str]]:
        '''
        :schema: ExternalSecretsCertControllerSecurityContextCapabilities#drop
        '''
        result = self._values.get("drop")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ExternalSecretsCertControllerSecurityContextCapabilities(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="external-secrets.ExternalSecretsCertControllerSecurityContextSeccompProfile",
    jsii_struct_bases=[],
    name_mapping={"additional_values": "additionalValues", "type": "type"},
)
class ExternalSecretsCertControllerSecurityContextSeccompProfile:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.
        :param type: 

        :schema: ExternalSecretsCertControllerSecurityContextSeccompProfile
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9e089a636a080275eb5e1ed4e26a8ce6ccc55b08aa9753cf2261882ab20558a1)
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_values is not None:
            self._values["additional_values"] = additional_values
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def additional_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: ExternalSecretsCertControllerSecurityContextSeccompProfile#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: ExternalSecretsCertControllerSecurityContextSeccompProfile#type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ExternalSecretsCertControllerSecurityContextSeccompProfile(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="external-secrets.ExternalSecretsCertControllerServiceAccount",
    jsii_struct_bases=[],
    name_mapping={
        "additional_values": "additionalValues",
        "annotations": "annotations",
        "automount": "automount",
        "create": "create",
        "extra_labels": "extraLabels",
        "name": "name",
    },
)
class ExternalSecretsCertControllerServiceAccount:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        annotations: typing.Optional[typing.Union["ExternalSecretsCertControllerServiceAccountAnnotations", typing.Dict[builtins.str, typing.Any]]] = None,
        automount: typing.Optional[builtins.bool] = None,
        create: typing.Optional[builtins.bool] = None,
        extra_labels: typing.Optional[typing.Union["ExternalSecretsCertControllerServiceAccountExtraLabels", typing.Dict[builtins.str, typing.Any]]] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.
        :param annotations: 
        :param automount: 
        :param create: 
        :param extra_labels: 
        :param name: 

        :schema: ExternalSecretsCertControllerServiceAccount
        '''
        if isinstance(annotations, dict):
            annotations = ExternalSecretsCertControllerServiceAccountAnnotations(**annotations)
        if isinstance(extra_labels, dict):
            extra_labels = ExternalSecretsCertControllerServiceAccountExtraLabels(**extra_labels)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b4972b31afd41cffd9741a674f157bbe97f49e359624a2bcb0eae302ea03c29c)
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
            check_type(argname="argument annotations", value=annotations, expected_type=type_hints["annotations"])
            check_type(argname="argument automount", value=automount, expected_type=type_hints["automount"])
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
            check_type(argname="argument extra_labels", value=extra_labels, expected_type=type_hints["extra_labels"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_values is not None:
            self._values["additional_values"] = additional_values
        if annotations is not None:
            self._values["annotations"] = annotations
        if automount is not None:
            self._values["automount"] = automount
        if create is not None:
            self._values["create"] = create
        if extra_labels is not None:
            self._values["extra_labels"] = extra_labels
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def additional_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: ExternalSecretsCertControllerServiceAccount#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def annotations(
        self,
    ) -> typing.Optional["ExternalSecretsCertControllerServiceAccountAnnotations"]:
        '''
        :schema: ExternalSecretsCertControllerServiceAccount#annotations
        '''
        result = self._values.get("annotations")
        return typing.cast(typing.Optional["ExternalSecretsCertControllerServiceAccountAnnotations"], result)

    @builtins.property
    def automount(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: ExternalSecretsCertControllerServiceAccount#automount
        '''
        result = self._values.get("automount")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def create(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: ExternalSecretsCertControllerServiceAccount#create
        '''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def extra_labels(
        self,
    ) -> typing.Optional["ExternalSecretsCertControllerServiceAccountExtraLabels"]:
        '''
        :schema: ExternalSecretsCertControllerServiceAccount#extraLabels
        '''
        result = self._values.get("extra_labels")
        return typing.cast(typing.Optional["ExternalSecretsCertControllerServiceAccountExtraLabels"], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''
        :schema: ExternalSecretsCertControllerServiceAccount#name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ExternalSecretsCertControllerServiceAccount(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="external-secrets.ExternalSecretsCertControllerServiceAccountAnnotations",
    jsii_struct_bases=[],
    name_mapping={"additional_values": "additionalValues"},
)
class ExternalSecretsCertControllerServiceAccountAnnotations:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: ExternalSecretsCertControllerServiceAccountAnnotations
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__575e01b5f959f58c95296eb3aff49b63316732f733f0172ab2d0a2a2f86831ad)
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_values is not None:
            self._values["additional_values"] = additional_values

    @builtins.property
    def additional_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: ExternalSecretsCertControllerServiceAccountAnnotations#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ExternalSecretsCertControllerServiceAccountAnnotations(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="external-secrets.ExternalSecretsCertControllerServiceAccountExtraLabels",
    jsii_struct_bases=[],
    name_mapping={"additional_values": "additionalValues"},
)
class ExternalSecretsCertControllerServiceAccountExtraLabels:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: ExternalSecretsCertControllerServiceAccountExtraLabels
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4ab5ab6fd1e0fe86e0d53eec8b2f5a675da09244a356fae515bdc37f99d5f8ec)
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_values is not None:
            self._values["additional_values"] = additional_values

    @builtins.property
    def additional_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: ExternalSecretsCertControllerServiceAccountExtraLabels#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ExternalSecretsCertControllerServiceAccountExtraLabels(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="external-secrets.ExternalSecretsCommonLabels",
    jsii_struct_bases=[],
    name_mapping={"additional_values": "additionalValues"},
)
class ExternalSecretsCommonLabels:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: ExternalSecretsCommonLabels
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dca8f6b7ab4c4518b1b227594f33732ca006a71897da4776c51dc5c5449c9a7a)
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_values is not None:
            self._values["additional_values"] = additional_values

    @builtins.property
    def additional_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: ExternalSecretsCommonLabels#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ExternalSecretsCommonLabels(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="external-secrets.ExternalSecretsCrds",
    jsii_struct_bases=[],
    name_mapping={
        "additional_values": "additionalValues",
        "annotations": "annotations",
        "conversion": "conversion",
        "create_cluster_external_secret": "createClusterExternalSecret",
        "create_cluster_generator": "createClusterGenerator",
        "create_cluster_push_secret": "createClusterPushSecret",
        "create_cluster_secret_store": "createClusterSecretStore",
        "create_push_secret": "createPushSecret",
    },
)
class ExternalSecretsCrds:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        annotations: typing.Optional[typing.Union["ExternalSecretsCrdsAnnotations", typing.Dict[builtins.str, typing.Any]]] = None,
        conversion: typing.Optional[typing.Union["ExternalSecretsCrdsConversion", typing.Dict[builtins.str, typing.Any]]] = None,
        create_cluster_external_secret: typing.Optional[builtins.bool] = None,
        create_cluster_generator: typing.Optional[builtins.bool] = None,
        create_cluster_push_secret: typing.Optional[builtins.bool] = None,
        create_cluster_secret_store: typing.Optional[builtins.bool] = None,
        create_push_secret: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.
        :param annotations: 
        :param conversion: 
        :param create_cluster_external_secret: 
        :param create_cluster_generator: 
        :param create_cluster_push_secret: 
        :param create_cluster_secret_store: 
        :param create_push_secret: 

        :schema: ExternalSecretsCrds
        '''
        if isinstance(annotations, dict):
            annotations = ExternalSecretsCrdsAnnotations(**annotations)
        if isinstance(conversion, dict):
            conversion = ExternalSecretsCrdsConversion(**conversion)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5a26a6d4526d16e791fd27b21085a63f44608ba2c680efefd407a86721ec0802)
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
            check_type(argname="argument annotations", value=annotations, expected_type=type_hints["annotations"])
            check_type(argname="argument conversion", value=conversion, expected_type=type_hints["conversion"])
            check_type(argname="argument create_cluster_external_secret", value=create_cluster_external_secret, expected_type=type_hints["create_cluster_external_secret"])
            check_type(argname="argument create_cluster_generator", value=create_cluster_generator, expected_type=type_hints["create_cluster_generator"])
            check_type(argname="argument create_cluster_push_secret", value=create_cluster_push_secret, expected_type=type_hints["create_cluster_push_secret"])
            check_type(argname="argument create_cluster_secret_store", value=create_cluster_secret_store, expected_type=type_hints["create_cluster_secret_store"])
            check_type(argname="argument create_push_secret", value=create_push_secret, expected_type=type_hints["create_push_secret"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_values is not None:
            self._values["additional_values"] = additional_values
        if annotations is not None:
            self._values["annotations"] = annotations
        if conversion is not None:
            self._values["conversion"] = conversion
        if create_cluster_external_secret is not None:
            self._values["create_cluster_external_secret"] = create_cluster_external_secret
        if create_cluster_generator is not None:
            self._values["create_cluster_generator"] = create_cluster_generator
        if create_cluster_push_secret is not None:
            self._values["create_cluster_push_secret"] = create_cluster_push_secret
        if create_cluster_secret_store is not None:
            self._values["create_cluster_secret_store"] = create_cluster_secret_store
        if create_push_secret is not None:
            self._values["create_push_secret"] = create_push_secret

    @builtins.property
    def additional_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: ExternalSecretsCrds#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def annotations(self) -> typing.Optional["ExternalSecretsCrdsAnnotations"]:
        '''
        :schema: ExternalSecretsCrds#annotations
        '''
        result = self._values.get("annotations")
        return typing.cast(typing.Optional["ExternalSecretsCrdsAnnotations"], result)

    @builtins.property
    def conversion(self) -> typing.Optional["ExternalSecretsCrdsConversion"]:
        '''
        :schema: ExternalSecretsCrds#conversion
        '''
        result = self._values.get("conversion")
        return typing.cast(typing.Optional["ExternalSecretsCrdsConversion"], result)

    @builtins.property
    def create_cluster_external_secret(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: ExternalSecretsCrds#createClusterExternalSecret
        '''
        result = self._values.get("create_cluster_external_secret")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def create_cluster_generator(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: ExternalSecretsCrds#createClusterGenerator
        '''
        result = self._values.get("create_cluster_generator")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def create_cluster_push_secret(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: ExternalSecretsCrds#createClusterPushSecret
        '''
        result = self._values.get("create_cluster_push_secret")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def create_cluster_secret_store(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: ExternalSecretsCrds#createClusterSecretStore
        '''
        result = self._values.get("create_cluster_secret_store")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def create_push_secret(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: ExternalSecretsCrds#createPushSecret
        '''
        result = self._values.get("create_push_secret")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ExternalSecretsCrds(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="external-secrets.ExternalSecretsCrdsAnnotations",
    jsii_struct_bases=[],
    name_mapping={"additional_values": "additionalValues"},
)
class ExternalSecretsCrdsAnnotations:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: ExternalSecretsCrdsAnnotations
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b0d9737373fddb1d64d7436c03a41d3d44bd36f27fb9186150771a05fc89613f)
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_values is not None:
            self._values["additional_values"] = additional_values

    @builtins.property
    def additional_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: ExternalSecretsCrdsAnnotations#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ExternalSecretsCrdsAnnotations(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="external-secrets.ExternalSecretsCrdsConversion",
    jsii_struct_bases=[],
    name_mapping={"additional_values": "additionalValues", "enabled": "enabled"},
)
class ExternalSecretsCrdsConversion:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        enabled: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.
        :param enabled: 

        :schema: ExternalSecretsCrdsConversion
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4bcc0937b6df670047d2bda5e145435f0257ee29f88717833f9832df002e3352)
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_values is not None:
            self._values["additional_values"] = additional_values
        if enabled is not None:
            self._values["enabled"] = enabled

    @builtins.property
    def additional_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: ExternalSecretsCrdsConversion#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def enabled(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: ExternalSecretsCrdsConversion#enabled
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ExternalSecretsCrdsConversion(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="external-secrets.ExternalSecretsDeploymentAnnotations",
    jsii_struct_bases=[],
    name_mapping={"additional_values": "additionalValues"},
)
class ExternalSecretsDeploymentAnnotations:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: ExternalSecretsDeploymentAnnotations
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c2a4cb5f88d701e40538308b09ccee6d8fa71c36f90bba265b2ba48614768784)
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_values is not None:
            self._values["additional_values"] = additional_values

    @builtins.property
    def additional_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: ExternalSecretsDeploymentAnnotations#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ExternalSecretsDeploymentAnnotations(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="external-secrets.ExternalSecretsDnsConfig",
    jsii_struct_bases=[],
    name_mapping={"additional_values": "additionalValues"},
)
class ExternalSecretsDnsConfig:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: ExternalSecretsDnsConfig
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__20701acb3a2f0fe4fcf6d75acfe310c5c35ed96a6110fd13aa3d3e5d7b48bdaa)
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_values is not None:
            self._values["additional_values"] = additional_values

    @builtins.property
    def additional_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: ExternalSecretsDnsConfig#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ExternalSecretsDnsConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="external-secrets.ExternalSecretsExtraArgs",
    jsii_struct_bases=[],
    name_mapping={"additional_values": "additionalValues"},
)
class ExternalSecretsExtraArgs:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: ExternalSecretsExtraArgs
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b797807a10ed8a58934fc83fa400d991e7b3f7f4148bb9716e8509a56dc6ed0d)
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_values is not None:
            self._values["additional_values"] = additional_values

    @builtins.property
    def additional_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: ExternalSecretsExtraArgs#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ExternalSecretsExtraArgs(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="external-secrets.ExternalSecretsGrafanaDashboard",
    jsii_struct_bases=[],
    name_mapping={
        "additional_values": "additionalValues",
        "annotations": "annotations",
        "enabled": "enabled",
        "sidecar_label": "sidecarLabel",
        "sidecar_label_value": "sidecarLabelValue",
    },
)
class ExternalSecretsGrafanaDashboard:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        annotations: typing.Optional[typing.Union["ExternalSecretsGrafanaDashboardAnnotations", typing.Dict[builtins.str, typing.Any]]] = None,
        enabled: typing.Optional[builtins.bool] = None,
        sidecar_label: typing.Optional[builtins.str] = None,
        sidecar_label_value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.
        :param annotations: 
        :param enabled: 
        :param sidecar_label: 
        :param sidecar_label_value: 

        :schema: ExternalSecretsGrafanaDashboard
        '''
        if isinstance(annotations, dict):
            annotations = ExternalSecretsGrafanaDashboardAnnotations(**annotations)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a7b46c0d66b8ca221762ec7b29a4d8ffa5bc08ba901d85bb104ca052534afb83)
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
            check_type(argname="argument annotations", value=annotations, expected_type=type_hints["annotations"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument sidecar_label", value=sidecar_label, expected_type=type_hints["sidecar_label"])
            check_type(argname="argument sidecar_label_value", value=sidecar_label_value, expected_type=type_hints["sidecar_label_value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_values is not None:
            self._values["additional_values"] = additional_values
        if annotations is not None:
            self._values["annotations"] = annotations
        if enabled is not None:
            self._values["enabled"] = enabled
        if sidecar_label is not None:
            self._values["sidecar_label"] = sidecar_label
        if sidecar_label_value is not None:
            self._values["sidecar_label_value"] = sidecar_label_value

    @builtins.property
    def additional_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: ExternalSecretsGrafanaDashboard#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def annotations(
        self,
    ) -> typing.Optional["ExternalSecretsGrafanaDashboardAnnotations"]:
        '''
        :schema: ExternalSecretsGrafanaDashboard#annotations
        '''
        result = self._values.get("annotations")
        return typing.cast(typing.Optional["ExternalSecretsGrafanaDashboardAnnotations"], result)

    @builtins.property
    def enabled(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: ExternalSecretsGrafanaDashboard#enabled
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def sidecar_label(self) -> typing.Optional[builtins.str]:
        '''
        :schema: ExternalSecretsGrafanaDashboard#sidecarLabel
        '''
        result = self._values.get("sidecar_label")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sidecar_label_value(self) -> typing.Optional[builtins.str]:
        '''
        :schema: ExternalSecretsGrafanaDashboard#sidecarLabelValue
        '''
        result = self._values.get("sidecar_label_value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ExternalSecretsGrafanaDashboard(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="external-secrets.ExternalSecretsGrafanaDashboardAnnotations",
    jsii_struct_bases=[],
    name_mapping={"additional_values": "additionalValues"},
)
class ExternalSecretsGrafanaDashboardAnnotations:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: ExternalSecretsGrafanaDashboardAnnotations
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e09c283fc52ae2b9b15745432386941fa9244522505c84efd5d21e445d45a9fd)
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_values is not None:
            self._values["additional_values"] = additional_values

    @builtins.property
    def additional_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: ExternalSecretsGrafanaDashboardAnnotations#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ExternalSecretsGrafanaDashboardAnnotations(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="external-secrets.ExternalSecretsImage",
    jsii_struct_bases=[],
    name_mapping={
        "additional_values": "additionalValues",
        "flavour": "flavour",
        "pull_policy": "pullPolicy",
        "repository": "repository",
        "tag": "tag",
    },
)
class ExternalSecretsImage:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        flavour: typing.Optional[builtins.str] = None,
        pull_policy: typing.Optional[builtins.str] = None,
        repository: typing.Optional[builtins.str] = None,
        tag: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.
        :param flavour: 
        :param pull_policy: 
        :param repository: 
        :param tag: 

        :schema: ExternalSecretsImage
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ea161ef1bed9451f11a5a337b1424fbb62c4f0fd634410c915b70ecc55989424)
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
            check_type(argname="argument flavour", value=flavour, expected_type=type_hints["flavour"])
            check_type(argname="argument pull_policy", value=pull_policy, expected_type=type_hints["pull_policy"])
            check_type(argname="argument repository", value=repository, expected_type=type_hints["repository"])
            check_type(argname="argument tag", value=tag, expected_type=type_hints["tag"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_values is not None:
            self._values["additional_values"] = additional_values
        if flavour is not None:
            self._values["flavour"] = flavour
        if pull_policy is not None:
            self._values["pull_policy"] = pull_policy
        if repository is not None:
            self._values["repository"] = repository
        if tag is not None:
            self._values["tag"] = tag

    @builtins.property
    def additional_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: ExternalSecretsImage#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def flavour(self) -> typing.Optional[builtins.str]:
        '''
        :schema: ExternalSecretsImage#flavour
        '''
        result = self._values.get("flavour")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def pull_policy(self) -> typing.Optional[builtins.str]:
        '''
        :schema: ExternalSecretsImage#pullPolicy
        '''
        result = self._values.get("pull_policy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def repository(self) -> typing.Optional[builtins.str]:
        '''
        :schema: ExternalSecretsImage#repository
        '''
        result = self._values.get("repository")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tag(self) -> typing.Optional[builtins.str]:
        '''
        :schema: ExternalSecretsImage#tag
        '''
        result = self._values.get("tag")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ExternalSecretsImage(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="external-secrets.ExternalSecretsLog",
    jsii_struct_bases=[],
    name_mapping={
        "additional_values": "additionalValues",
        "level": "level",
        "time_encoding": "timeEncoding",
    },
)
class ExternalSecretsLog:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        level: typing.Optional[builtins.str] = None,
        time_encoding: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.
        :param level: 
        :param time_encoding: 

        :schema: ExternalSecretsLog
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4ab228c4ae140ddde5462f48ff62422199ea281422684df15c2d2eab4f0a21bf)
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
            check_type(argname="argument level", value=level, expected_type=type_hints["level"])
            check_type(argname="argument time_encoding", value=time_encoding, expected_type=type_hints["time_encoding"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_values is not None:
            self._values["additional_values"] = additional_values
        if level is not None:
            self._values["level"] = level
        if time_encoding is not None:
            self._values["time_encoding"] = time_encoding

    @builtins.property
    def additional_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: ExternalSecretsLog#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def level(self) -> typing.Optional[builtins.str]:
        '''
        :schema: ExternalSecretsLog#level
        '''
        result = self._values.get("level")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def time_encoding(self) -> typing.Optional[builtins.str]:
        '''
        :schema: ExternalSecretsLog#timeEncoding
        '''
        result = self._values.get("time_encoding")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ExternalSecretsLog(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="external-secrets.ExternalSecretsMetrics",
    jsii_struct_bases=[],
    name_mapping={
        "additional_values": "additionalValues",
        "listen": "listen",
        "service": "service",
    },
)
class ExternalSecretsMetrics:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        listen: typing.Optional[typing.Union["ExternalSecretsMetricsListen", typing.Dict[builtins.str, typing.Any]]] = None,
        service: typing.Optional[typing.Union["ExternalSecretsMetricsService", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.
        :param listen: 
        :param service: 

        :schema: ExternalSecretsMetrics
        '''
        if isinstance(listen, dict):
            listen = ExternalSecretsMetricsListen(**listen)
        if isinstance(service, dict):
            service = ExternalSecretsMetricsService(**service)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e21294305bff98bfcd2bd0bcee45154f480f43218712e3e8683b85567cf16b96)
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
            check_type(argname="argument listen", value=listen, expected_type=type_hints["listen"])
            check_type(argname="argument service", value=service, expected_type=type_hints["service"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_values is not None:
            self._values["additional_values"] = additional_values
        if listen is not None:
            self._values["listen"] = listen
        if service is not None:
            self._values["service"] = service

    @builtins.property
    def additional_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: ExternalSecretsMetrics#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def listen(self) -> typing.Optional["ExternalSecretsMetricsListen"]:
        '''
        :schema: ExternalSecretsMetrics#listen
        '''
        result = self._values.get("listen")
        return typing.cast(typing.Optional["ExternalSecretsMetricsListen"], result)

    @builtins.property
    def service(self) -> typing.Optional["ExternalSecretsMetricsService"]:
        '''
        :schema: ExternalSecretsMetrics#service
        '''
        result = self._values.get("service")
        return typing.cast(typing.Optional["ExternalSecretsMetricsService"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ExternalSecretsMetrics(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="external-secrets.ExternalSecretsMetricsListen",
    jsii_struct_bases=[],
    name_mapping={"additional_values": "additionalValues", "port": "port"},
)
class ExternalSecretsMetricsListen:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        port: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.
        :param port: 

        :schema: ExternalSecretsMetricsListen
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__65bf3137db5396f1735b3ccee527b21147ce0c31b627ac26fae0e3e3827bc8b9)
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_values is not None:
            self._values["additional_values"] = additional_values
        if port is not None:
            self._values["port"] = port

    @builtins.property
    def additional_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: ExternalSecretsMetricsListen#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def port(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: ExternalSecretsMetricsListen#port
        '''
        result = self._values.get("port")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ExternalSecretsMetricsListen(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="external-secrets.ExternalSecretsMetricsService",
    jsii_struct_bases=[],
    name_mapping={
        "additional_values": "additionalValues",
        "annotations": "annotations",
        "enabled": "enabled",
        "port": "port",
    },
)
class ExternalSecretsMetricsService:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        annotations: typing.Optional[typing.Union["ExternalSecretsMetricsServiceAnnotations", typing.Dict[builtins.str, typing.Any]]] = None,
        enabled: typing.Optional[builtins.bool] = None,
        port: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.
        :param annotations: 
        :param enabled: 
        :param port: 

        :schema: ExternalSecretsMetricsService
        '''
        if isinstance(annotations, dict):
            annotations = ExternalSecretsMetricsServiceAnnotations(**annotations)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7d86a139402a143ddb6374d70de48243e7a729b1d2a69d75cc6d3b9f8281cdfb)
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
            check_type(argname="argument annotations", value=annotations, expected_type=type_hints["annotations"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_values is not None:
            self._values["additional_values"] = additional_values
        if annotations is not None:
            self._values["annotations"] = annotations
        if enabled is not None:
            self._values["enabled"] = enabled
        if port is not None:
            self._values["port"] = port

    @builtins.property
    def additional_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: ExternalSecretsMetricsService#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def annotations(
        self,
    ) -> typing.Optional["ExternalSecretsMetricsServiceAnnotations"]:
        '''
        :schema: ExternalSecretsMetricsService#annotations
        '''
        result = self._values.get("annotations")
        return typing.cast(typing.Optional["ExternalSecretsMetricsServiceAnnotations"], result)

    @builtins.property
    def enabled(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: ExternalSecretsMetricsService#enabled
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def port(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: ExternalSecretsMetricsService#port
        '''
        result = self._values.get("port")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ExternalSecretsMetricsService(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="external-secrets.ExternalSecretsMetricsServiceAnnotations",
    jsii_struct_bases=[],
    name_mapping={"additional_values": "additionalValues"},
)
class ExternalSecretsMetricsServiceAnnotations:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: ExternalSecretsMetricsServiceAnnotations
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ab645bb0bc8839ce7e5adfc45b3084c0da5b39dc3ba68c51bc5608ac79dbfa44)
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_values is not None:
            self._values["additional_values"] = additional_values

    @builtins.property
    def additional_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: ExternalSecretsMetricsServiceAnnotations#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ExternalSecretsMetricsServiceAnnotations(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="external-secrets.ExternalSecretsNodeSelector",
    jsii_struct_bases=[],
    name_mapping={"additional_values": "additionalValues"},
)
class ExternalSecretsNodeSelector:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: ExternalSecretsNodeSelector
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bbf479cb99c2e9319a339fdce977c7f9fa1833909f58397258532e7fbf83121c)
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_values is not None:
            self._values["additional_values"] = additional_values

    @builtins.property
    def additional_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: ExternalSecretsNodeSelector#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ExternalSecretsNodeSelector(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="external-secrets.ExternalSecretsPodAnnotations",
    jsii_struct_bases=[],
    name_mapping={"additional_values": "additionalValues"},
)
class ExternalSecretsPodAnnotations:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: ExternalSecretsPodAnnotations
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__50b7a00e061ae6d380a98719ffcb8ee1fa52482db8bc79fae953628f2a2b11a6)
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_values is not None:
            self._values["additional_values"] = additional_values

    @builtins.property
    def additional_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: ExternalSecretsPodAnnotations#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ExternalSecretsPodAnnotations(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="external-secrets.ExternalSecretsPodDisruptionBudget",
    jsii_struct_bases=[],
    name_mapping={
        "additional_values": "additionalValues",
        "enabled": "enabled",
        "min_available": "minAvailable",
    },
)
class ExternalSecretsPodDisruptionBudget:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        enabled: typing.Optional[builtins.bool] = None,
        min_available: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.
        :param enabled: 
        :param min_available: 

        :schema: ExternalSecretsPodDisruptionBudget
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f52d2bde3e75aff7b2b961a97dffdc8a38ec0706c41650ef7f5c98ed23574cc6)
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument min_available", value=min_available, expected_type=type_hints["min_available"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_values is not None:
            self._values["additional_values"] = additional_values
        if enabled is not None:
            self._values["enabled"] = enabled
        if min_available is not None:
            self._values["min_available"] = min_available

    @builtins.property
    def additional_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: ExternalSecretsPodDisruptionBudget#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def enabled(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: ExternalSecretsPodDisruptionBudget#enabled
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def min_available(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: ExternalSecretsPodDisruptionBudget#minAvailable
        '''
        result = self._values.get("min_available")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ExternalSecretsPodDisruptionBudget(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="external-secrets.ExternalSecretsPodLabels",
    jsii_struct_bases=[],
    name_mapping={"additional_values": "additionalValues"},
)
class ExternalSecretsPodLabels:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: ExternalSecretsPodLabels
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a9def16ae49f564838a775bb2346070b162811690200f43faeb790c105af1568)
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_values is not None:
            self._values["additional_values"] = additional_values

    @builtins.property
    def additional_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: ExternalSecretsPodLabels#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ExternalSecretsPodLabels(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="external-secrets.ExternalSecretsPodSecurityContext",
    jsii_struct_bases=[],
    name_mapping={"additional_values": "additionalValues", "enabled": "enabled"},
)
class ExternalSecretsPodSecurityContext:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        enabled: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.
        :param enabled: 

        :schema: ExternalSecretsPodSecurityContext
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__707d879de51daea67b7728241a4a0704769a1936ace9c3c4358768f91a94e585)
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_values is not None:
            self._values["additional_values"] = additional_values
        if enabled is not None:
            self._values["enabled"] = enabled

    @builtins.property
    def additional_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: ExternalSecretsPodSecurityContext#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def enabled(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: ExternalSecretsPodSecurityContext#enabled
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ExternalSecretsPodSecurityContext(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="external-secrets.ExternalSecretsPodSpecExtra",
    jsii_struct_bases=[],
    name_mapping={"additional_values": "additionalValues"},
)
class ExternalSecretsPodSpecExtra:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: ExternalSecretsPodSpecExtra
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__149bb64fea876c68dfd3722c41e5a78477357250c93ff827058212b555c2a4dc)
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_values is not None:
            self._values["additional_values"] = additional_values

    @builtins.property
    def additional_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: ExternalSecretsPodSpecExtra#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ExternalSecretsPodSpecExtra(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="external-secrets.ExternalSecretsRbac",
    jsii_struct_bases=[],
    name_mapping={
        "additional_values": "additionalValues",
        "aggregate_to_edit": "aggregateToEdit",
        "aggregate_to_view": "aggregateToView",
        "create": "create",
        "servicebindings": "servicebindings",
    },
)
class ExternalSecretsRbac:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        aggregate_to_edit: typing.Optional[builtins.bool] = None,
        aggregate_to_view: typing.Optional[builtins.bool] = None,
        create: typing.Optional[builtins.bool] = None,
        servicebindings: typing.Optional[typing.Union["ExternalSecretsRbacServicebindings", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.
        :param aggregate_to_edit: 
        :param aggregate_to_view: 
        :param create: 
        :param servicebindings: 

        :schema: ExternalSecretsRbac
        '''
        if isinstance(servicebindings, dict):
            servicebindings = ExternalSecretsRbacServicebindings(**servicebindings)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7d9b2ef0e1734ddc974aeb44b3a6b46864befcfb32833a89d80bf47f3791074a)
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
            check_type(argname="argument aggregate_to_edit", value=aggregate_to_edit, expected_type=type_hints["aggregate_to_edit"])
            check_type(argname="argument aggregate_to_view", value=aggregate_to_view, expected_type=type_hints["aggregate_to_view"])
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
            check_type(argname="argument servicebindings", value=servicebindings, expected_type=type_hints["servicebindings"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_values is not None:
            self._values["additional_values"] = additional_values
        if aggregate_to_edit is not None:
            self._values["aggregate_to_edit"] = aggregate_to_edit
        if aggregate_to_view is not None:
            self._values["aggregate_to_view"] = aggregate_to_view
        if create is not None:
            self._values["create"] = create
        if servicebindings is not None:
            self._values["servicebindings"] = servicebindings

    @builtins.property
    def additional_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: ExternalSecretsRbac#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def aggregate_to_edit(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: ExternalSecretsRbac#aggregateToEdit
        '''
        result = self._values.get("aggregate_to_edit")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def aggregate_to_view(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: ExternalSecretsRbac#aggregateToView
        '''
        result = self._values.get("aggregate_to_view")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def create(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: ExternalSecretsRbac#create
        '''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def servicebindings(self) -> typing.Optional["ExternalSecretsRbacServicebindings"]:
        '''
        :schema: ExternalSecretsRbac#servicebindings
        '''
        result = self._values.get("servicebindings")
        return typing.cast(typing.Optional["ExternalSecretsRbacServicebindings"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ExternalSecretsRbac(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="external-secrets.ExternalSecretsRbacServicebindings",
    jsii_struct_bases=[],
    name_mapping={"additional_values": "additionalValues", "create": "create"},
)
class ExternalSecretsRbacServicebindings:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        create: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.
        :param create: 

        :schema: ExternalSecretsRbacServicebindings
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3e5f50624e6803778810d6f884262051daff1bf9337c98e22d6c376d2fd0dd49)
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_values is not None:
            self._values["additional_values"] = additional_values
        if create is not None:
            self._values["create"] = create

    @builtins.property
    def additional_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: ExternalSecretsRbacServicebindings#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def create(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: ExternalSecretsRbacServicebindings#create
        '''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ExternalSecretsRbacServicebindings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="external-secrets.ExternalSecretsResources",
    jsii_struct_bases=[],
    name_mapping={"additional_values": "additionalValues"},
)
class ExternalSecretsResources:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: ExternalSecretsResources
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6368948474ab3d8e9d6fa5e7aef356e4b64a22007e23519ba21b152f6f439d3b)
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_values is not None:
            self._values["additional_values"] = additional_values

    @builtins.property
    def additional_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: ExternalSecretsResources#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ExternalSecretsResources(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="external-secrets.ExternalSecretsSecurityContext",
    jsii_struct_bases=[],
    name_mapping={
        "additional_values": "additionalValues",
        "allow_privilege_escalation": "allowPrivilegeEscalation",
        "capabilities": "capabilities",
        "enabled": "enabled",
        "read_only_root_filesystem": "readOnlyRootFilesystem",
        "run_as_non_root": "runAsNonRoot",
        "run_as_user": "runAsUser",
        "seccomp_profile": "seccompProfile",
    },
)
class ExternalSecretsSecurityContext:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        allow_privilege_escalation: typing.Optional[builtins.bool] = None,
        capabilities: typing.Optional[typing.Union["ExternalSecretsSecurityContextCapabilities", typing.Dict[builtins.str, typing.Any]]] = None,
        enabled: typing.Optional[builtins.bool] = None,
        read_only_root_filesystem: typing.Optional[builtins.bool] = None,
        run_as_non_root: typing.Optional[builtins.bool] = None,
        run_as_user: typing.Optional[jsii.Number] = None,
        seccomp_profile: typing.Optional[typing.Union["ExternalSecretsSecurityContextSeccompProfile", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.
        :param allow_privilege_escalation: 
        :param capabilities: 
        :param enabled: 
        :param read_only_root_filesystem: 
        :param run_as_non_root: 
        :param run_as_user: 
        :param seccomp_profile: 

        :schema: ExternalSecretsSecurityContext
        '''
        if isinstance(capabilities, dict):
            capabilities = ExternalSecretsSecurityContextCapabilities(**capabilities)
        if isinstance(seccomp_profile, dict):
            seccomp_profile = ExternalSecretsSecurityContextSeccompProfile(**seccomp_profile)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7b1981a823a7bc3e612f61be4b7ab79ef1a01468d28e4c003268d56b906a0f67)
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
            check_type(argname="argument allow_privilege_escalation", value=allow_privilege_escalation, expected_type=type_hints["allow_privilege_escalation"])
            check_type(argname="argument capabilities", value=capabilities, expected_type=type_hints["capabilities"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument read_only_root_filesystem", value=read_only_root_filesystem, expected_type=type_hints["read_only_root_filesystem"])
            check_type(argname="argument run_as_non_root", value=run_as_non_root, expected_type=type_hints["run_as_non_root"])
            check_type(argname="argument run_as_user", value=run_as_user, expected_type=type_hints["run_as_user"])
            check_type(argname="argument seccomp_profile", value=seccomp_profile, expected_type=type_hints["seccomp_profile"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_values is not None:
            self._values["additional_values"] = additional_values
        if allow_privilege_escalation is not None:
            self._values["allow_privilege_escalation"] = allow_privilege_escalation
        if capabilities is not None:
            self._values["capabilities"] = capabilities
        if enabled is not None:
            self._values["enabled"] = enabled
        if read_only_root_filesystem is not None:
            self._values["read_only_root_filesystem"] = read_only_root_filesystem
        if run_as_non_root is not None:
            self._values["run_as_non_root"] = run_as_non_root
        if run_as_user is not None:
            self._values["run_as_user"] = run_as_user
        if seccomp_profile is not None:
            self._values["seccomp_profile"] = seccomp_profile

    @builtins.property
    def additional_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: ExternalSecretsSecurityContext#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def allow_privilege_escalation(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: ExternalSecretsSecurityContext#allowPrivilegeEscalation
        '''
        result = self._values.get("allow_privilege_escalation")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def capabilities(
        self,
    ) -> typing.Optional["ExternalSecretsSecurityContextCapabilities"]:
        '''
        :schema: ExternalSecretsSecurityContext#capabilities
        '''
        result = self._values.get("capabilities")
        return typing.cast(typing.Optional["ExternalSecretsSecurityContextCapabilities"], result)

    @builtins.property
    def enabled(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: ExternalSecretsSecurityContext#enabled
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def read_only_root_filesystem(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: ExternalSecretsSecurityContext#readOnlyRootFilesystem
        '''
        result = self._values.get("read_only_root_filesystem")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def run_as_non_root(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: ExternalSecretsSecurityContext#runAsNonRoot
        '''
        result = self._values.get("run_as_non_root")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def run_as_user(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: ExternalSecretsSecurityContext#runAsUser
        '''
        result = self._values.get("run_as_user")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def seccomp_profile(
        self,
    ) -> typing.Optional["ExternalSecretsSecurityContextSeccompProfile"]:
        '''
        :schema: ExternalSecretsSecurityContext#seccompProfile
        '''
        result = self._values.get("seccomp_profile")
        return typing.cast(typing.Optional["ExternalSecretsSecurityContextSeccompProfile"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ExternalSecretsSecurityContext(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="external-secrets.ExternalSecretsSecurityContextCapabilities",
    jsii_struct_bases=[],
    name_mapping={"additional_values": "additionalValues", "drop": "drop"},
)
class ExternalSecretsSecurityContextCapabilities:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        drop: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.
        :param drop: 

        :schema: ExternalSecretsSecurityContextCapabilities
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__451d08701ab9cf031ac5233dbb3f790c6271ba377752517c96bc28439af3c8a4)
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
            check_type(argname="argument drop", value=drop, expected_type=type_hints["drop"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_values is not None:
            self._values["additional_values"] = additional_values
        if drop is not None:
            self._values["drop"] = drop

    @builtins.property
    def additional_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: ExternalSecretsSecurityContextCapabilities#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def drop(self) -> typing.Optional[typing.List[builtins.str]]:
        '''
        :schema: ExternalSecretsSecurityContextCapabilities#drop
        '''
        result = self._values.get("drop")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ExternalSecretsSecurityContextCapabilities(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="external-secrets.ExternalSecretsSecurityContextSeccompProfile",
    jsii_struct_bases=[],
    name_mapping={"additional_values": "additionalValues", "type": "type"},
)
class ExternalSecretsSecurityContextSeccompProfile:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.
        :param type: 

        :schema: ExternalSecretsSecurityContextSeccompProfile
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0619ec5aded402e56bb6ed22f96683f1782db58dc8c1add12d1120372ae103f8)
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_values is not None:
            self._values["additional_values"] = additional_values
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def additional_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: ExternalSecretsSecurityContextSeccompProfile#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: ExternalSecretsSecurityContextSeccompProfile#type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ExternalSecretsSecurityContextSeccompProfile(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="external-secrets.ExternalSecretsService",
    jsii_struct_bases=[],
    name_mapping={
        "additional_values": "additionalValues",
        "ip_families": "ipFamilies",
        "ip_family_policy": "ipFamilyPolicy",
    },
)
class ExternalSecretsService:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        ip_families: typing.Optional[typing.Sequence[typing.Any]] = None,
        ip_family_policy: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.
        :param ip_families: 
        :param ip_family_policy: 

        :schema: ExternalSecretsService
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8248d48ea0ac184028c7d5cb6cf9a18a9dd79454cf2bff151e44c1d58ef360eb)
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
            check_type(argname="argument ip_families", value=ip_families, expected_type=type_hints["ip_families"])
            check_type(argname="argument ip_family_policy", value=ip_family_policy, expected_type=type_hints["ip_family_policy"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_values is not None:
            self._values["additional_values"] = additional_values
        if ip_families is not None:
            self._values["ip_families"] = ip_families
        if ip_family_policy is not None:
            self._values["ip_family_policy"] = ip_family_policy

    @builtins.property
    def additional_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: ExternalSecretsService#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def ip_families(self) -> typing.Optional[typing.List[typing.Any]]:
        '''
        :schema: ExternalSecretsService#ipFamilies
        '''
        result = self._values.get("ip_families")
        return typing.cast(typing.Optional[typing.List[typing.Any]], result)

    @builtins.property
    def ip_family_policy(self) -> typing.Optional[builtins.str]:
        '''
        :schema: ExternalSecretsService#ipFamilyPolicy
        '''
        result = self._values.get("ip_family_policy")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ExternalSecretsService(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="external-secrets.ExternalSecretsServiceAccount",
    jsii_struct_bases=[],
    name_mapping={
        "additional_values": "additionalValues",
        "annotations": "annotations",
        "automount": "automount",
        "create": "create",
        "extra_labels": "extraLabels",
        "name": "name",
    },
)
class ExternalSecretsServiceAccount:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        annotations: typing.Optional[typing.Union["ExternalSecretsServiceAccountAnnotations", typing.Dict[builtins.str, typing.Any]]] = None,
        automount: typing.Optional[builtins.bool] = None,
        create: typing.Optional[builtins.bool] = None,
        extra_labels: typing.Optional[typing.Union["ExternalSecretsServiceAccountExtraLabels", typing.Dict[builtins.str, typing.Any]]] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.
        :param annotations: 
        :param automount: 
        :param create: 
        :param extra_labels: 
        :param name: 

        :schema: ExternalSecretsServiceAccount
        '''
        if isinstance(annotations, dict):
            annotations = ExternalSecretsServiceAccountAnnotations(**annotations)
        if isinstance(extra_labels, dict):
            extra_labels = ExternalSecretsServiceAccountExtraLabels(**extra_labels)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__411b410172ce4bf5ecc4fa0049d970f979ea37b57f146fe2c2ce1537f4108c20)
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
            check_type(argname="argument annotations", value=annotations, expected_type=type_hints["annotations"])
            check_type(argname="argument automount", value=automount, expected_type=type_hints["automount"])
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
            check_type(argname="argument extra_labels", value=extra_labels, expected_type=type_hints["extra_labels"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_values is not None:
            self._values["additional_values"] = additional_values
        if annotations is not None:
            self._values["annotations"] = annotations
        if automount is not None:
            self._values["automount"] = automount
        if create is not None:
            self._values["create"] = create
        if extra_labels is not None:
            self._values["extra_labels"] = extra_labels
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def additional_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: ExternalSecretsServiceAccount#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def annotations(
        self,
    ) -> typing.Optional["ExternalSecretsServiceAccountAnnotations"]:
        '''
        :schema: ExternalSecretsServiceAccount#annotations
        '''
        result = self._values.get("annotations")
        return typing.cast(typing.Optional["ExternalSecretsServiceAccountAnnotations"], result)

    @builtins.property
    def automount(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: ExternalSecretsServiceAccount#automount
        '''
        result = self._values.get("automount")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def create(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: ExternalSecretsServiceAccount#create
        '''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def extra_labels(
        self,
    ) -> typing.Optional["ExternalSecretsServiceAccountExtraLabels"]:
        '''
        :schema: ExternalSecretsServiceAccount#extraLabels
        '''
        result = self._values.get("extra_labels")
        return typing.cast(typing.Optional["ExternalSecretsServiceAccountExtraLabels"], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''
        :schema: ExternalSecretsServiceAccount#name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ExternalSecretsServiceAccount(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="external-secrets.ExternalSecretsServiceAccountAnnotations",
    jsii_struct_bases=[],
    name_mapping={"additional_values": "additionalValues"},
)
class ExternalSecretsServiceAccountAnnotations:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: ExternalSecretsServiceAccountAnnotations
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__646b8dbb27cbb9fd60d736f4001eece582a9561b1ac29fe4f04674ca32ce18fe)
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_values is not None:
            self._values["additional_values"] = additional_values

    @builtins.property
    def additional_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: ExternalSecretsServiceAccountAnnotations#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ExternalSecretsServiceAccountAnnotations(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="external-secrets.ExternalSecretsServiceAccountExtraLabels",
    jsii_struct_bases=[],
    name_mapping={"additional_values": "additionalValues"},
)
class ExternalSecretsServiceAccountExtraLabels:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: ExternalSecretsServiceAccountExtraLabels
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__64fc74da162d9ec51ecc2f7069d506bb9512a1b72246850ccd57ad06617a99c3)
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_values is not None:
            self._values["additional_values"] = additional_values

    @builtins.property
    def additional_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: ExternalSecretsServiceAccountExtraLabels#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ExternalSecretsServiceAccountExtraLabels(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="external-secrets.ExternalSecretsServiceMonitor",
    jsii_struct_bases=[],
    name_mapping={
        "additional_labels": "additionalLabels",
        "additional_values": "additionalValues",
        "enabled": "enabled",
        "honor_labels": "honorLabels",
        "interval": "interval",
        "metric_relabelings": "metricRelabelings",
        "namespace": "namespace",
        "relabelings": "relabelings",
        "scrape_timeout": "scrapeTimeout",
    },
)
class ExternalSecretsServiceMonitor:
    def __init__(
        self,
        *,
        additional_labels: typing.Optional[typing.Union["ExternalSecretsServiceMonitorAdditionalLabels", typing.Dict[builtins.str, typing.Any]]] = None,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        enabled: typing.Optional[builtins.bool] = None,
        honor_labels: typing.Optional[builtins.bool] = None,
        interval: typing.Optional[builtins.str] = None,
        metric_relabelings: typing.Optional[typing.Sequence[typing.Any]] = None,
        namespace: typing.Optional[builtins.str] = None,
        relabelings: typing.Optional[typing.Sequence[typing.Any]] = None,
        scrape_timeout: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param additional_labels: 
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.
        :param enabled: 
        :param honor_labels: 
        :param interval: 
        :param metric_relabelings: 
        :param namespace: 
        :param relabelings: 
        :param scrape_timeout: 

        :schema: ExternalSecretsServiceMonitor
        '''
        if isinstance(additional_labels, dict):
            additional_labels = ExternalSecretsServiceMonitorAdditionalLabels(**additional_labels)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__25751ef29bc9239a97465557615fada6ca8ec60914ca7553f3dd570520278fcb)
            check_type(argname="argument additional_labels", value=additional_labels, expected_type=type_hints["additional_labels"])
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument honor_labels", value=honor_labels, expected_type=type_hints["honor_labels"])
            check_type(argname="argument interval", value=interval, expected_type=type_hints["interval"])
            check_type(argname="argument metric_relabelings", value=metric_relabelings, expected_type=type_hints["metric_relabelings"])
            check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
            check_type(argname="argument relabelings", value=relabelings, expected_type=type_hints["relabelings"])
            check_type(argname="argument scrape_timeout", value=scrape_timeout, expected_type=type_hints["scrape_timeout"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_labels is not None:
            self._values["additional_labels"] = additional_labels
        if additional_values is not None:
            self._values["additional_values"] = additional_values
        if enabled is not None:
            self._values["enabled"] = enabled
        if honor_labels is not None:
            self._values["honor_labels"] = honor_labels
        if interval is not None:
            self._values["interval"] = interval
        if metric_relabelings is not None:
            self._values["metric_relabelings"] = metric_relabelings
        if namespace is not None:
            self._values["namespace"] = namespace
        if relabelings is not None:
            self._values["relabelings"] = relabelings
        if scrape_timeout is not None:
            self._values["scrape_timeout"] = scrape_timeout

    @builtins.property
    def additional_labels(
        self,
    ) -> typing.Optional["ExternalSecretsServiceMonitorAdditionalLabels"]:
        '''
        :schema: ExternalSecretsServiceMonitor#additionalLabels
        '''
        result = self._values.get("additional_labels")
        return typing.cast(typing.Optional["ExternalSecretsServiceMonitorAdditionalLabels"], result)

    @builtins.property
    def additional_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: ExternalSecretsServiceMonitor#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def enabled(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: ExternalSecretsServiceMonitor#enabled
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def honor_labels(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: ExternalSecretsServiceMonitor#honorLabels
        '''
        result = self._values.get("honor_labels")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def interval(self) -> typing.Optional[builtins.str]:
        '''
        :schema: ExternalSecretsServiceMonitor#interval
        '''
        result = self._values.get("interval")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def metric_relabelings(self) -> typing.Optional[typing.List[typing.Any]]:
        '''
        :schema: ExternalSecretsServiceMonitor#metricRelabelings
        '''
        result = self._values.get("metric_relabelings")
        return typing.cast(typing.Optional[typing.List[typing.Any]], result)

    @builtins.property
    def namespace(self) -> typing.Optional[builtins.str]:
        '''
        :schema: ExternalSecretsServiceMonitor#namespace
        '''
        result = self._values.get("namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def relabelings(self) -> typing.Optional[typing.List[typing.Any]]:
        '''
        :schema: ExternalSecretsServiceMonitor#relabelings
        '''
        result = self._values.get("relabelings")
        return typing.cast(typing.Optional[typing.List[typing.Any]], result)

    @builtins.property
    def scrape_timeout(self) -> typing.Optional[builtins.str]:
        '''
        :schema: ExternalSecretsServiceMonitor#scrapeTimeout
        '''
        result = self._values.get("scrape_timeout")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ExternalSecretsServiceMonitor(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="external-secrets.ExternalSecretsServiceMonitorAdditionalLabels",
    jsii_struct_bases=[],
    name_mapping={"additional_values": "additionalValues"},
)
class ExternalSecretsServiceMonitorAdditionalLabels:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: ExternalSecretsServiceMonitorAdditionalLabels
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ffbe12387c140c1117fd65bccb0ecd74555f0d8c1a69616c14a101fdc513d382)
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_values is not None:
            self._values["additional_values"] = additional_values

    @builtins.property
    def additional_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: ExternalSecretsServiceMonitorAdditionalLabels#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ExternalSecretsServiceMonitorAdditionalLabels(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="external-secrets.ExternalSecretsWebhook",
    jsii_struct_bases=[],
    name_mapping={
        "additional_values": "additionalValues",
        "affinity": "affinity",
        "annotations": "annotations",
        "cert_check_interval": "certCheckInterval",
        "cert_dir": "certDir",
        "cert_manager": "certManager",
        "create": "create",
        "deployment_annotations": "deploymentAnnotations",
        "extra_args": "extraArgs",
        "extra_env": "extraEnv",
        "extra_volume_mounts": "extraVolumeMounts",
        "extra_volumes": "extraVolumes",
        "failure_policy": "failurePolicy",
        "fullname_override": "fullnameOverride",
        "host_network": "hostNetwork",
        "image": "image",
        "image_pull_secrets": "imagePullSecrets",
        "log": "log",
        "lookahead_interval": "lookaheadInterval",
        "metrics": "metrics",
        "name_override": "nameOverride",
        "node_selector": "nodeSelector",
        "pod_annotations": "podAnnotations",
        "pod_disruption_budget": "podDisruptionBudget",
        "pod_labels": "podLabels",
        "pod_security_context": "podSecurityContext",
        "port": "port",
        "priority_class_name": "priorityClassName",
        "rbac": "rbac",
        "readiness_probe": "readinessProbe",
        "replica_count": "replicaCount",
        "resources": "resources",
        "revision_history_limit": "revisionHistoryLimit",
        "secret_annotations": "secretAnnotations",
        "security_context": "securityContext",
        "service": "service",
        "service_account": "serviceAccount",
        "tolerations": "tolerations",
        "topology_spread_constraints": "topologySpreadConstraints",
    },
)
class ExternalSecretsWebhook:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        affinity: typing.Optional[typing.Union["ExternalSecretsWebhookAffinity", typing.Dict[builtins.str, typing.Any]]] = None,
        annotations: typing.Optional[typing.Union["ExternalSecretsWebhookAnnotations", typing.Dict[builtins.str, typing.Any]]] = None,
        cert_check_interval: typing.Optional[builtins.str] = None,
        cert_dir: typing.Optional[builtins.str] = None,
        cert_manager: typing.Optional[typing.Union["ExternalSecretsWebhookCertManager", typing.Dict[builtins.str, typing.Any]]] = None,
        create: typing.Optional[builtins.bool] = None,
        deployment_annotations: typing.Optional[typing.Union["ExternalSecretsWebhookDeploymentAnnotations", typing.Dict[builtins.str, typing.Any]]] = None,
        extra_args: typing.Optional[typing.Union["ExternalSecretsWebhookExtraArgs", typing.Dict[builtins.str, typing.Any]]] = None,
        extra_env: typing.Optional[typing.Sequence[typing.Any]] = None,
        extra_volume_mounts: typing.Optional[typing.Sequence[typing.Any]] = None,
        extra_volumes: typing.Optional[typing.Sequence[typing.Any]] = None,
        failure_policy: typing.Optional[builtins.str] = None,
        fullname_override: typing.Optional[builtins.str] = None,
        host_network: typing.Optional[builtins.bool] = None,
        image: typing.Optional[typing.Union["ExternalSecretsWebhookImage", typing.Dict[builtins.str, typing.Any]]] = None,
        image_pull_secrets: typing.Optional[typing.Sequence[typing.Any]] = None,
        log: typing.Optional[typing.Union["ExternalSecretsWebhookLog", typing.Dict[builtins.str, typing.Any]]] = None,
        lookahead_interval: typing.Optional[builtins.str] = None,
        metrics: typing.Optional[typing.Union["ExternalSecretsWebhookMetrics", typing.Dict[builtins.str, typing.Any]]] = None,
        name_override: typing.Optional[builtins.str] = None,
        node_selector: typing.Optional[typing.Union["ExternalSecretsWebhookNodeSelector", typing.Dict[builtins.str, typing.Any]]] = None,
        pod_annotations: typing.Optional[typing.Union["ExternalSecretsWebhookPodAnnotations", typing.Dict[builtins.str, typing.Any]]] = None,
        pod_disruption_budget: typing.Optional[typing.Union["ExternalSecretsWebhookPodDisruptionBudget", typing.Dict[builtins.str, typing.Any]]] = None,
        pod_labels: typing.Optional[typing.Union["ExternalSecretsWebhookPodLabels", typing.Dict[builtins.str, typing.Any]]] = None,
        pod_security_context: typing.Optional[typing.Union["ExternalSecretsWebhookPodSecurityContext", typing.Dict[builtins.str, typing.Any]]] = None,
        port: typing.Optional[jsii.Number] = None,
        priority_class_name: typing.Optional[builtins.str] = None,
        rbac: typing.Optional[typing.Union["ExternalSecretsWebhookRbac", typing.Dict[builtins.str, typing.Any]]] = None,
        readiness_probe: typing.Optional[typing.Union["ExternalSecretsWebhookReadinessProbe", typing.Dict[builtins.str, typing.Any]]] = None,
        replica_count: typing.Optional[jsii.Number] = None,
        resources: typing.Optional[typing.Union["ExternalSecretsWebhookResources", typing.Dict[builtins.str, typing.Any]]] = None,
        revision_history_limit: typing.Optional[jsii.Number] = None,
        secret_annotations: typing.Optional[typing.Union["ExternalSecretsWebhookSecretAnnotations", typing.Dict[builtins.str, typing.Any]]] = None,
        security_context: typing.Optional[typing.Union["ExternalSecretsWebhookSecurityContext", typing.Dict[builtins.str, typing.Any]]] = None,
        service: typing.Optional[typing.Union["ExternalSecretsWebhookService", typing.Dict[builtins.str, typing.Any]]] = None,
        service_account: typing.Optional[typing.Union["ExternalSecretsWebhookServiceAccount", typing.Dict[builtins.str, typing.Any]]] = None,
        tolerations: typing.Optional[typing.Sequence[typing.Any]] = None,
        topology_spread_constraints: typing.Optional[typing.Sequence[typing.Any]] = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.
        :param affinity: 
        :param annotations: 
        :param cert_check_interval: 
        :param cert_dir: 
        :param cert_manager: 
        :param create: 
        :param deployment_annotations: 
        :param extra_args: 
        :param extra_env: 
        :param extra_volume_mounts: 
        :param extra_volumes: 
        :param failure_policy: 
        :param fullname_override: 
        :param host_network: 
        :param image: 
        :param image_pull_secrets: 
        :param log: 
        :param lookahead_interval: 
        :param metrics: 
        :param name_override: 
        :param node_selector: 
        :param pod_annotations: 
        :param pod_disruption_budget: 
        :param pod_labels: 
        :param pod_security_context: 
        :param port: 
        :param priority_class_name: 
        :param rbac: 
        :param readiness_probe: 
        :param replica_count: 
        :param resources: 
        :param revision_history_limit: 
        :param secret_annotations: 
        :param security_context: 
        :param service: 
        :param service_account: 
        :param tolerations: 
        :param topology_spread_constraints: 

        :schema: ExternalSecretsWebhook
        '''
        if isinstance(affinity, dict):
            affinity = ExternalSecretsWebhookAffinity(**affinity)
        if isinstance(annotations, dict):
            annotations = ExternalSecretsWebhookAnnotations(**annotations)
        if isinstance(cert_manager, dict):
            cert_manager = ExternalSecretsWebhookCertManager(**cert_manager)
        if isinstance(deployment_annotations, dict):
            deployment_annotations = ExternalSecretsWebhookDeploymentAnnotations(**deployment_annotations)
        if isinstance(extra_args, dict):
            extra_args = ExternalSecretsWebhookExtraArgs(**extra_args)
        if isinstance(image, dict):
            image = ExternalSecretsWebhookImage(**image)
        if isinstance(log, dict):
            log = ExternalSecretsWebhookLog(**log)
        if isinstance(metrics, dict):
            metrics = ExternalSecretsWebhookMetrics(**metrics)
        if isinstance(node_selector, dict):
            node_selector = ExternalSecretsWebhookNodeSelector(**node_selector)
        if isinstance(pod_annotations, dict):
            pod_annotations = ExternalSecretsWebhookPodAnnotations(**pod_annotations)
        if isinstance(pod_disruption_budget, dict):
            pod_disruption_budget = ExternalSecretsWebhookPodDisruptionBudget(**pod_disruption_budget)
        if isinstance(pod_labels, dict):
            pod_labels = ExternalSecretsWebhookPodLabels(**pod_labels)
        if isinstance(pod_security_context, dict):
            pod_security_context = ExternalSecretsWebhookPodSecurityContext(**pod_security_context)
        if isinstance(rbac, dict):
            rbac = ExternalSecretsWebhookRbac(**rbac)
        if isinstance(readiness_probe, dict):
            readiness_probe = ExternalSecretsWebhookReadinessProbe(**readiness_probe)
        if isinstance(resources, dict):
            resources = ExternalSecretsWebhookResources(**resources)
        if isinstance(secret_annotations, dict):
            secret_annotations = ExternalSecretsWebhookSecretAnnotations(**secret_annotations)
        if isinstance(security_context, dict):
            security_context = ExternalSecretsWebhookSecurityContext(**security_context)
        if isinstance(service, dict):
            service = ExternalSecretsWebhookService(**service)
        if isinstance(service_account, dict):
            service_account = ExternalSecretsWebhookServiceAccount(**service_account)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1bb990e5f92a626f64522d860d089a7ecfadd7ef797be3108a230f5875a33fa9)
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
            check_type(argname="argument affinity", value=affinity, expected_type=type_hints["affinity"])
            check_type(argname="argument annotations", value=annotations, expected_type=type_hints["annotations"])
            check_type(argname="argument cert_check_interval", value=cert_check_interval, expected_type=type_hints["cert_check_interval"])
            check_type(argname="argument cert_dir", value=cert_dir, expected_type=type_hints["cert_dir"])
            check_type(argname="argument cert_manager", value=cert_manager, expected_type=type_hints["cert_manager"])
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
            check_type(argname="argument deployment_annotations", value=deployment_annotations, expected_type=type_hints["deployment_annotations"])
            check_type(argname="argument extra_args", value=extra_args, expected_type=type_hints["extra_args"])
            check_type(argname="argument extra_env", value=extra_env, expected_type=type_hints["extra_env"])
            check_type(argname="argument extra_volume_mounts", value=extra_volume_mounts, expected_type=type_hints["extra_volume_mounts"])
            check_type(argname="argument extra_volumes", value=extra_volumes, expected_type=type_hints["extra_volumes"])
            check_type(argname="argument failure_policy", value=failure_policy, expected_type=type_hints["failure_policy"])
            check_type(argname="argument fullname_override", value=fullname_override, expected_type=type_hints["fullname_override"])
            check_type(argname="argument host_network", value=host_network, expected_type=type_hints["host_network"])
            check_type(argname="argument image", value=image, expected_type=type_hints["image"])
            check_type(argname="argument image_pull_secrets", value=image_pull_secrets, expected_type=type_hints["image_pull_secrets"])
            check_type(argname="argument log", value=log, expected_type=type_hints["log"])
            check_type(argname="argument lookahead_interval", value=lookahead_interval, expected_type=type_hints["lookahead_interval"])
            check_type(argname="argument metrics", value=metrics, expected_type=type_hints["metrics"])
            check_type(argname="argument name_override", value=name_override, expected_type=type_hints["name_override"])
            check_type(argname="argument node_selector", value=node_selector, expected_type=type_hints["node_selector"])
            check_type(argname="argument pod_annotations", value=pod_annotations, expected_type=type_hints["pod_annotations"])
            check_type(argname="argument pod_disruption_budget", value=pod_disruption_budget, expected_type=type_hints["pod_disruption_budget"])
            check_type(argname="argument pod_labels", value=pod_labels, expected_type=type_hints["pod_labels"])
            check_type(argname="argument pod_security_context", value=pod_security_context, expected_type=type_hints["pod_security_context"])
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
            check_type(argname="argument priority_class_name", value=priority_class_name, expected_type=type_hints["priority_class_name"])
            check_type(argname="argument rbac", value=rbac, expected_type=type_hints["rbac"])
            check_type(argname="argument readiness_probe", value=readiness_probe, expected_type=type_hints["readiness_probe"])
            check_type(argname="argument replica_count", value=replica_count, expected_type=type_hints["replica_count"])
            check_type(argname="argument resources", value=resources, expected_type=type_hints["resources"])
            check_type(argname="argument revision_history_limit", value=revision_history_limit, expected_type=type_hints["revision_history_limit"])
            check_type(argname="argument secret_annotations", value=secret_annotations, expected_type=type_hints["secret_annotations"])
            check_type(argname="argument security_context", value=security_context, expected_type=type_hints["security_context"])
            check_type(argname="argument service", value=service, expected_type=type_hints["service"])
            check_type(argname="argument service_account", value=service_account, expected_type=type_hints["service_account"])
            check_type(argname="argument tolerations", value=tolerations, expected_type=type_hints["tolerations"])
            check_type(argname="argument topology_spread_constraints", value=topology_spread_constraints, expected_type=type_hints["topology_spread_constraints"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_values is not None:
            self._values["additional_values"] = additional_values
        if affinity is not None:
            self._values["affinity"] = affinity
        if annotations is not None:
            self._values["annotations"] = annotations
        if cert_check_interval is not None:
            self._values["cert_check_interval"] = cert_check_interval
        if cert_dir is not None:
            self._values["cert_dir"] = cert_dir
        if cert_manager is not None:
            self._values["cert_manager"] = cert_manager
        if create is not None:
            self._values["create"] = create
        if deployment_annotations is not None:
            self._values["deployment_annotations"] = deployment_annotations
        if extra_args is not None:
            self._values["extra_args"] = extra_args
        if extra_env is not None:
            self._values["extra_env"] = extra_env
        if extra_volume_mounts is not None:
            self._values["extra_volume_mounts"] = extra_volume_mounts
        if extra_volumes is not None:
            self._values["extra_volumes"] = extra_volumes
        if failure_policy is not None:
            self._values["failure_policy"] = failure_policy
        if fullname_override is not None:
            self._values["fullname_override"] = fullname_override
        if host_network is not None:
            self._values["host_network"] = host_network
        if image is not None:
            self._values["image"] = image
        if image_pull_secrets is not None:
            self._values["image_pull_secrets"] = image_pull_secrets
        if log is not None:
            self._values["log"] = log
        if lookahead_interval is not None:
            self._values["lookahead_interval"] = lookahead_interval
        if metrics is not None:
            self._values["metrics"] = metrics
        if name_override is not None:
            self._values["name_override"] = name_override
        if node_selector is not None:
            self._values["node_selector"] = node_selector
        if pod_annotations is not None:
            self._values["pod_annotations"] = pod_annotations
        if pod_disruption_budget is not None:
            self._values["pod_disruption_budget"] = pod_disruption_budget
        if pod_labels is not None:
            self._values["pod_labels"] = pod_labels
        if pod_security_context is not None:
            self._values["pod_security_context"] = pod_security_context
        if port is not None:
            self._values["port"] = port
        if priority_class_name is not None:
            self._values["priority_class_name"] = priority_class_name
        if rbac is not None:
            self._values["rbac"] = rbac
        if readiness_probe is not None:
            self._values["readiness_probe"] = readiness_probe
        if replica_count is not None:
            self._values["replica_count"] = replica_count
        if resources is not None:
            self._values["resources"] = resources
        if revision_history_limit is not None:
            self._values["revision_history_limit"] = revision_history_limit
        if secret_annotations is not None:
            self._values["secret_annotations"] = secret_annotations
        if security_context is not None:
            self._values["security_context"] = security_context
        if service is not None:
            self._values["service"] = service
        if service_account is not None:
            self._values["service_account"] = service_account
        if tolerations is not None:
            self._values["tolerations"] = tolerations
        if topology_spread_constraints is not None:
            self._values["topology_spread_constraints"] = topology_spread_constraints

    @builtins.property
    def additional_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: ExternalSecretsWebhook#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def affinity(self) -> typing.Optional["ExternalSecretsWebhookAffinity"]:
        '''
        :schema: ExternalSecretsWebhook#affinity
        '''
        result = self._values.get("affinity")
        return typing.cast(typing.Optional["ExternalSecretsWebhookAffinity"], result)

    @builtins.property
    def annotations(self) -> typing.Optional["ExternalSecretsWebhookAnnotations"]:
        '''
        :schema: ExternalSecretsWebhook#annotations
        '''
        result = self._values.get("annotations")
        return typing.cast(typing.Optional["ExternalSecretsWebhookAnnotations"], result)

    @builtins.property
    def cert_check_interval(self) -> typing.Optional[builtins.str]:
        '''
        :schema: ExternalSecretsWebhook#certCheckInterval
        '''
        result = self._values.get("cert_check_interval")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cert_dir(self) -> typing.Optional[builtins.str]:
        '''
        :schema: ExternalSecretsWebhook#certDir
        '''
        result = self._values.get("cert_dir")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cert_manager(self) -> typing.Optional["ExternalSecretsWebhookCertManager"]:
        '''
        :schema: ExternalSecretsWebhook#certManager
        '''
        result = self._values.get("cert_manager")
        return typing.cast(typing.Optional["ExternalSecretsWebhookCertManager"], result)

    @builtins.property
    def create(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: ExternalSecretsWebhook#create
        '''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def deployment_annotations(
        self,
    ) -> typing.Optional["ExternalSecretsWebhookDeploymentAnnotations"]:
        '''
        :schema: ExternalSecretsWebhook#deploymentAnnotations
        '''
        result = self._values.get("deployment_annotations")
        return typing.cast(typing.Optional["ExternalSecretsWebhookDeploymentAnnotations"], result)

    @builtins.property
    def extra_args(self) -> typing.Optional["ExternalSecretsWebhookExtraArgs"]:
        '''
        :schema: ExternalSecretsWebhook#extraArgs
        '''
        result = self._values.get("extra_args")
        return typing.cast(typing.Optional["ExternalSecretsWebhookExtraArgs"], result)

    @builtins.property
    def extra_env(self) -> typing.Optional[typing.List[typing.Any]]:
        '''
        :schema: ExternalSecretsWebhook#extraEnv
        '''
        result = self._values.get("extra_env")
        return typing.cast(typing.Optional[typing.List[typing.Any]], result)

    @builtins.property
    def extra_volume_mounts(self) -> typing.Optional[typing.List[typing.Any]]:
        '''
        :schema: ExternalSecretsWebhook#extraVolumeMounts
        '''
        result = self._values.get("extra_volume_mounts")
        return typing.cast(typing.Optional[typing.List[typing.Any]], result)

    @builtins.property
    def extra_volumes(self) -> typing.Optional[typing.List[typing.Any]]:
        '''
        :schema: ExternalSecretsWebhook#extraVolumes
        '''
        result = self._values.get("extra_volumes")
        return typing.cast(typing.Optional[typing.List[typing.Any]], result)

    @builtins.property
    def failure_policy(self) -> typing.Optional[builtins.str]:
        '''
        :schema: ExternalSecretsWebhook#failurePolicy
        '''
        result = self._values.get("failure_policy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def fullname_override(self) -> typing.Optional[builtins.str]:
        '''
        :schema: ExternalSecretsWebhook#fullnameOverride
        '''
        result = self._values.get("fullname_override")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def host_network(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: ExternalSecretsWebhook#hostNetwork
        '''
        result = self._values.get("host_network")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def image(self) -> typing.Optional["ExternalSecretsWebhookImage"]:
        '''
        :schema: ExternalSecretsWebhook#image
        '''
        result = self._values.get("image")
        return typing.cast(typing.Optional["ExternalSecretsWebhookImage"], result)

    @builtins.property
    def image_pull_secrets(self) -> typing.Optional[typing.List[typing.Any]]:
        '''
        :schema: ExternalSecretsWebhook#imagePullSecrets
        '''
        result = self._values.get("image_pull_secrets")
        return typing.cast(typing.Optional[typing.List[typing.Any]], result)

    @builtins.property
    def log(self) -> typing.Optional["ExternalSecretsWebhookLog"]:
        '''
        :schema: ExternalSecretsWebhook#log
        '''
        result = self._values.get("log")
        return typing.cast(typing.Optional["ExternalSecretsWebhookLog"], result)

    @builtins.property
    def lookahead_interval(self) -> typing.Optional[builtins.str]:
        '''
        :schema: ExternalSecretsWebhook#lookaheadInterval
        '''
        result = self._values.get("lookahead_interval")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def metrics(self) -> typing.Optional["ExternalSecretsWebhookMetrics"]:
        '''
        :schema: ExternalSecretsWebhook#metrics
        '''
        result = self._values.get("metrics")
        return typing.cast(typing.Optional["ExternalSecretsWebhookMetrics"], result)

    @builtins.property
    def name_override(self) -> typing.Optional[builtins.str]:
        '''
        :schema: ExternalSecretsWebhook#nameOverride
        '''
        result = self._values.get("name_override")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def node_selector(self) -> typing.Optional["ExternalSecretsWebhookNodeSelector"]:
        '''
        :schema: ExternalSecretsWebhook#nodeSelector
        '''
        result = self._values.get("node_selector")
        return typing.cast(typing.Optional["ExternalSecretsWebhookNodeSelector"], result)

    @builtins.property
    def pod_annotations(
        self,
    ) -> typing.Optional["ExternalSecretsWebhookPodAnnotations"]:
        '''
        :schema: ExternalSecretsWebhook#podAnnotations
        '''
        result = self._values.get("pod_annotations")
        return typing.cast(typing.Optional["ExternalSecretsWebhookPodAnnotations"], result)

    @builtins.property
    def pod_disruption_budget(
        self,
    ) -> typing.Optional["ExternalSecretsWebhookPodDisruptionBudget"]:
        '''
        :schema: ExternalSecretsWebhook#podDisruptionBudget
        '''
        result = self._values.get("pod_disruption_budget")
        return typing.cast(typing.Optional["ExternalSecretsWebhookPodDisruptionBudget"], result)

    @builtins.property
    def pod_labels(self) -> typing.Optional["ExternalSecretsWebhookPodLabels"]:
        '''
        :schema: ExternalSecretsWebhook#podLabels
        '''
        result = self._values.get("pod_labels")
        return typing.cast(typing.Optional["ExternalSecretsWebhookPodLabels"], result)

    @builtins.property
    def pod_security_context(
        self,
    ) -> typing.Optional["ExternalSecretsWebhookPodSecurityContext"]:
        '''
        :schema: ExternalSecretsWebhook#podSecurityContext
        '''
        result = self._values.get("pod_security_context")
        return typing.cast(typing.Optional["ExternalSecretsWebhookPodSecurityContext"], result)

    @builtins.property
    def port(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: ExternalSecretsWebhook#port
        '''
        result = self._values.get("port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def priority_class_name(self) -> typing.Optional[builtins.str]:
        '''
        :schema: ExternalSecretsWebhook#priorityClassName
        '''
        result = self._values.get("priority_class_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def rbac(self) -> typing.Optional["ExternalSecretsWebhookRbac"]:
        '''
        :schema: ExternalSecretsWebhook#rbac
        '''
        result = self._values.get("rbac")
        return typing.cast(typing.Optional["ExternalSecretsWebhookRbac"], result)

    @builtins.property
    def readiness_probe(
        self,
    ) -> typing.Optional["ExternalSecretsWebhookReadinessProbe"]:
        '''
        :schema: ExternalSecretsWebhook#readinessProbe
        '''
        result = self._values.get("readiness_probe")
        return typing.cast(typing.Optional["ExternalSecretsWebhookReadinessProbe"], result)

    @builtins.property
    def replica_count(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: ExternalSecretsWebhook#replicaCount
        '''
        result = self._values.get("replica_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def resources(self) -> typing.Optional["ExternalSecretsWebhookResources"]:
        '''
        :schema: ExternalSecretsWebhook#resources
        '''
        result = self._values.get("resources")
        return typing.cast(typing.Optional["ExternalSecretsWebhookResources"], result)

    @builtins.property
    def revision_history_limit(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: ExternalSecretsWebhook#revisionHistoryLimit
        '''
        result = self._values.get("revision_history_limit")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def secret_annotations(
        self,
    ) -> typing.Optional["ExternalSecretsWebhookSecretAnnotations"]:
        '''
        :schema: ExternalSecretsWebhook#secretAnnotations
        '''
        result = self._values.get("secret_annotations")
        return typing.cast(typing.Optional["ExternalSecretsWebhookSecretAnnotations"], result)

    @builtins.property
    def security_context(
        self,
    ) -> typing.Optional["ExternalSecretsWebhookSecurityContext"]:
        '''
        :schema: ExternalSecretsWebhook#securityContext
        '''
        result = self._values.get("security_context")
        return typing.cast(typing.Optional["ExternalSecretsWebhookSecurityContext"], result)

    @builtins.property
    def service(self) -> typing.Optional["ExternalSecretsWebhookService"]:
        '''
        :schema: ExternalSecretsWebhook#service
        '''
        result = self._values.get("service")
        return typing.cast(typing.Optional["ExternalSecretsWebhookService"], result)

    @builtins.property
    def service_account(
        self,
    ) -> typing.Optional["ExternalSecretsWebhookServiceAccount"]:
        '''
        :schema: ExternalSecretsWebhook#serviceAccount
        '''
        result = self._values.get("service_account")
        return typing.cast(typing.Optional["ExternalSecretsWebhookServiceAccount"], result)

    @builtins.property
    def tolerations(self) -> typing.Optional[typing.List[typing.Any]]:
        '''
        :schema: ExternalSecretsWebhook#tolerations
        '''
        result = self._values.get("tolerations")
        return typing.cast(typing.Optional[typing.List[typing.Any]], result)

    @builtins.property
    def topology_spread_constraints(self) -> typing.Optional[typing.List[typing.Any]]:
        '''
        :schema: ExternalSecretsWebhook#topologySpreadConstraints
        '''
        result = self._values.get("topology_spread_constraints")
        return typing.cast(typing.Optional[typing.List[typing.Any]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ExternalSecretsWebhook(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="external-secrets.ExternalSecretsWebhookAffinity",
    jsii_struct_bases=[],
    name_mapping={"additional_values": "additionalValues"},
)
class ExternalSecretsWebhookAffinity:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: ExternalSecretsWebhookAffinity
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__89a8a0e74170554046a3491f02d39c02763ddaf56a77009d238a1cc6d569894d)
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_values is not None:
            self._values["additional_values"] = additional_values

    @builtins.property
    def additional_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: ExternalSecretsWebhookAffinity#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ExternalSecretsWebhookAffinity(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="external-secrets.ExternalSecretsWebhookAnnotations",
    jsii_struct_bases=[],
    name_mapping={"additional_values": "additionalValues"},
)
class ExternalSecretsWebhookAnnotations:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: ExternalSecretsWebhookAnnotations
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e1b432a637e0b87983a9b7143a32813a5a59b090a01b96b6b6a17dff1193b9f5)
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_values is not None:
            self._values["additional_values"] = additional_values

    @builtins.property
    def additional_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: ExternalSecretsWebhookAnnotations#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ExternalSecretsWebhookAnnotations(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="external-secrets.ExternalSecretsWebhookCertManager",
    jsii_struct_bases=[],
    name_mapping={
        "add_injector_annotations": "addInjectorAnnotations",
        "additional_values": "additionalValues",
        "cert": "cert",
        "enabled": "enabled",
    },
)
class ExternalSecretsWebhookCertManager:
    def __init__(
        self,
        *,
        add_injector_annotations: typing.Optional[builtins.bool] = None,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        cert: typing.Optional[typing.Union["ExternalSecretsWebhookCertManagerCert", typing.Dict[builtins.str, typing.Any]]] = None,
        enabled: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param add_injector_annotations: 
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.
        :param cert: 
        :param enabled: 

        :schema: ExternalSecretsWebhookCertManager
        '''
        if isinstance(cert, dict):
            cert = ExternalSecretsWebhookCertManagerCert(**cert)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b23a50719f15d3b10dd519b3c305ec876c637234f5accb798f206fedd2234c9b)
            check_type(argname="argument add_injector_annotations", value=add_injector_annotations, expected_type=type_hints["add_injector_annotations"])
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
            check_type(argname="argument cert", value=cert, expected_type=type_hints["cert"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if add_injector_annotations is not None:
            self._values["add_injector_annotations"] = add_injector_annotations
        if additional_values is not None:
            self._values["additional_values"] = additional_values
        if cert is not None:
            self._values["cert"] = cert
        if enabled is not None:
            self._values["enabled"] = enabled

    @builtins.property
    def add_injector_annotations(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: ExternalSecretsWebhookCertManager#addInjectorAnnotations
        '''
        result = self._values.get("add_injector_annotations")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def additional_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: ExternalSecretsWebhookCertManager#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def cert(self) -> typing.Optional["ExternalSecretsWebhookCertManagerCert"]:
        '''
        :schema: ExternalSecretsWebhookCertManager#cert
        '''
        result = self._values.get("cert")
        return typing.cast(typing.Optional["ExternalSecretsWebhookCertManagerCert"], result)

    @builtins.property
    def enabled(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: ExternalSecretsWebhookCertManager#enabled
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ExternalSecretsWebhookCertManager(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="external-secrets.ExternalSecretsWebhookCertManagerCert",
    jsii_struct_bases=[],
    name_mapping={
        "additional_values": "additionalValues",
        "annotations": "annotations",
        "create": "create",
        "duration": "duration",
        "issuer_ref": "issuerRef",
        "renew_before": "renewBefore",
        "revision_history_limit": "revisionHistoryLimit",
    },
)
class ExternalSecretsWebhookCertManagerCert:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        annotations: typing.Optional[typing.Union["ExternalSecretsWebhookCertManagerCertAnnotations", typing.Dict[builtins.str, typing.Any]]] = None,
        create: typing.Optional[builtins.bool] = None,
        duration: typing.Optional[builtins.str] = None,
        issuer_ref: typing.Optional[typing.Union["ExternalSecretsWebhookCertManagerCertIssuerRef", typing.Dict[builtins.str, typing.Any]]] = None,
        renew_before: typing.Optional[builtins.str] = None,
        revision_history_limit: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.
        :param annotations: 
        :param create: 
        :param duration: 
        :param issuer_ref: 
        :param renew_before: 
        :param revision_history_limit: 

        :schema: ExternalSecretsWebhookCertManagerCert
        '''
        if isinstance(annotations, dict):
            annotations = ExternalSecretsWebhookCertManagerCertAnnotations(**annotations)
        if isinstance(issuer_ref, dict):
            issuer_ref = ExternalSecretsWebhookCertManagerCertIssuerRef(**issuer_ref)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__84731106ab6916ee25148ef175097b58c44701d23736c35914488a18c85349c0)
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
            check_type(argname="argument annotations", value=annotations, expected_type=type_hints["annotations"])
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
            check_type(argname="argument duration", value=duration, expected_type=type_hints["duration"])
            check_type(argname="argument issuer_ref", value=issuer_ref, expected_type=type_hints["issuer_ref"])
            check_type(argname="argument renew_before", value=renew_before, expected_type=type_hints["renew_before"])
            check_type(argname="argument revision_history_limit", value=revision_history_limit, expected_type=type_hints["revision_history_limit"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_values is not None:
            self._values["additional_values"] = additional_values
        if annotations is not None:
            self._values["annotations"] = annotations
        if create is not None:
            self._values["create"] = create
        if duration is not None:
            self._values["duration"] = duration
        if issuer_ref is not None:
            self._values["issuer_ref"] = issuer_ref
        if renew_before is not None:
            self._values["renew_before"] = renew_before
        if revision_history_limit is not None:
            self._values["revision_history_limit"] = revision_history_limit

    @builtins.property
    def additional_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: ExternalSecretsWebhookCertManagerCert#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def annotations(
        self,
    ) -> typing.Optional["ExternalSecretsWebhookCertManagerCertAnnotations"]:
        '''
        :schema: ExternalSecretsWebhookCertManagerCert#annotations
        '''
        result = self._values.get("annotations")
        return typing.cast(typing.Optional["ExternalSecretsWebhookCertManagerCertAnnotations"], result)

    @builtins.property
    def create(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: ExternalSecretsWebhookCertManagerCert#create
        '''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def duration(self) -> typing.Optional[builtins.str]:
        '''
        :schema: ExternalSecretsWebhookCertManagerCert#duration
        '''
        result = self._values.get("duration")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def issuer_ref(
        self,
    ) -> typing.Optional["ExternalSecretsWebhookCertManagerCertIssuerRef"]:
        '''
        :schema: ExternalSecretsWebhookCertManagerCert#issuerRef
        '''
        result = self._values.get("issuer_ref")
        return typing.cast(typing.Optional["ExternalSecretsWebhookCertManagerCertIssuerRef"], result)

    @builtins.property
    def renew_before(self) -> typing.Optional[builtins.str]:
        '''
        :schema: ExternalSecretsWebhookCertManagerCert#renewBefore
        '''
        result = self._values.get("renew_before")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def revision_history_limit(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: ExternalSecretsWebhookCertManagerCert#revisionHistoryLimit
        '''
        result = self._values.get("revision_history_limit")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ExternalSecretsWebhookCertManagerCert(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="external-secrets.ExternalSecretsWebhookCertManagerCertAnnotations",
    jsii_struct_bases=[],
    name_mapping={"additional_values": "additionalValues"},
)
class ExternalSecretsWebhookCertManagerCertAnnotations:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: ExternalSecretsWebhookCertManagerCertAnnotations
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__91c91d29f6241f929ee858d632b73b69384b6388ab2440dc265daa5355a3607c)
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_values is not None:
            self._values["additional_values"] = additional_values

    @builtins.property
    def additional_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: ExternalSecretsWebhookCertManagerCertAnnotations#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ExternalSecretsWebhookCertManagerCertAnnotations(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="external-secrets.ExternalSecretsWebhookCertManagerCertIssuerRef",
    jsii_struct_bases=[],
    name_mapping={
        "additional_values": "additionalValues",
        "group": "group",
        "kind": "kind",
        "name": "name",
    },
)
class ExternalSecretsWebhookCertManagerCertIssuerRef:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        group: typing.Optional[builtins.str] = None,
        kind: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.
        :param group: 
        :param kind: 
        :param name: 

        :schema: ExternalSecretsWebhookCertManagerCertIssuerRef
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__42a9c6ed2409ebc4d5c6baec37aae4d95e32dd193ea25c8b59cdc83ff28b3e21)
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
            check_type(argname="argument group", value=group, expected_type=type_hints["group"])
            check_type(argname="argument kind", value=kind, expected_type=type_hints["kind"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_values is not None:
            self._values["additional_values"] = additional_values
        if group is not None:
            self._values["group"] = group
        if kind is not None:
            self._values["kind"] = kind
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def additional_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: ExternalSecretsWebhookCertManagerCertIssuerRef#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def group(self) -> typing.Optional[builtins.str]:
        '''
        :schema: ExternalSecretsWebhookCertManagerCertIssuerRef#group
        '''
        result = self._values.get("group")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kind(self) -> typing.Optional[builtins.str]:
        '''
        :schema: ExternalSecretsWebhookCertManagerCertIssuerRef#kind
        '''
        result = self._values.get("kind")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''
        :schema: ExternalSecretsWebhookCertManagerCertIssuerRef#name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ExternalSecretsWebhookCertManagerCertIssuerRef(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="external-secrets.ExternalSecretsWebhookDeploymentAnnotations",
    jsii_struct_bases=[],
    name_mapping={"additional_values": "additionalValues"},
)
class ExternalSecretsWebhookDeploymentAnnotations:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: ExternalSecretsWebhookDeploymentAnnotations
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fb90c63590ed3a886b0132d8291e2b226dc16ad844384886869bfc5b35fb2520)
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_values is not None:
            self._values["additional_values"] = additional_values

    @builtins.property
    def additional_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: ExternalSecretsWebhookDeploymentAnnotations#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ExternalSecretsWebhookDeploymentAnnotations(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="external-secrets.ExternalSecretsWebhookExtraArgs",
    jsii_struct_bases=[],
    name_mapping={"additional_values": "additionalValues"},
)
class ExternalSecretsWebhookExtraArgs:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: ExternalSecretsWebhookExtraArgs
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7ab3462bbccb589616d71ad3f098cb5b0ce648bda4411444b52f9d489e04e826)
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_values is not None:
            self._values["additional_values"] = additional_values

    @builtins.property
    def additional_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: ExternalSecretsWebhookExtraArgs#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ExternalSecretsWebhookExtraArgs(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="external-secrets.ExternalSecretsWebhookImage",
    jsii_struct_bases=[],
    name_mapping={
        "additional_values": "additionalValues",
        "flavour": "flavour",
        "pull_policy": "pullPolicy",
        "repository": "repository",
        "tag": "tag",
    },
)
class ExternalSecretsWebhookImage:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        flavour: typing.Optional[builtins.str] = None,
        pull_policy: typing.Optional[builtins.str] = None,
        repository: typing.Optional[builtins.str] = None,
        tag: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.
        :param flavour: 
        :param pull_policy: 
        :param repository: 
        :param tag: 

        :schema: ExternalSecretsWebhookImage
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__817d529ad17cc45cdcd5db526227d26f8533693fc0b488bf0996691c40a5db53)
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
            check_type(argname="argument flavour", value=flavour, expected_type=type_hints["flavour"])
            check_type(argname="argument pull_policy", value=pull_policy, expected_type=type_hints["pull_policy"])
            check_type(argname="argument repository", value=repository, expected_type=type_hints["repository"])
            check_type(argname="argument tag", value=tag, expected_type=type_hints["tag"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_values is not None:
            self._values["additional_values"] = additional_values
        if flavour is not None:
            self._values["flavour"] = flavour
        if pull_policy is not None:
            self._values["pull_policy"] = pull_policy
        if repository is not None:
            self._values["repository"] = repository
        if tag is not None:
            self._values["tag"] = tag

    @builtins.property
    def additional_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: ExternalSecretsWebhookImage#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def flavour(self) -> typing.Optional[builtins.str]:
        '''
        :schema: ExternalSecretsWebhookImage#flavour
        '''
        result = self._values.get("flavour")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def pull_policy(self) -> typing.Optional[builtins.str]:
        '''
        :schema: ExternalSecretsWebhookImage#pullPolicy
        '''
        result = self._values.get("pull_policy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def repository(self) -> typing.Optional[builtins.str]:
        '''
        :schema: ExternalSecretsWebhookImage#repository
        '''
        result = self._values.get("repository")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tag(self) -> typing.Optional[builtins.str]:
        '''
        :schema: ExternalSecretsWebhookImage#tag
        '''
        result = self._values.get("tag")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ExternalSecretsWebhookImage(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="external-secrets.ExternalSecretsWebhookLog",
    jsii_struct_bases=[],
    name_mapping={
        "additional_values": "additionalValues",
        "level": "level",
        "time_encoding": "timeEncoding",
    },
)
class ExternalSecretsWebhookLog:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        level: typing.Optional[builtins.str] = None,
        time_encoding: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.
        :param level: 
        :param time_encoding: 

        :schema: ExternalSecretsWebhookLog
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ca360874d9a5748675fd49dbefc43cc62dc388d75469000a88f6fd9783e5091d)
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
            check_type(argname="argument level", value=level, expected_type=type_hints["level"])
            check_type(argname="argument time_encoding", value=time_encoding, expected_type=type_hints["time_encoding"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_values is not None:
            self._values["additional_values"] = additional_values
        if level is not None:
            self._values["level"] = level
        if time_encoding is not None:
            self._values["time_encoding"] = time_encoding

    @builtins.property
    def additional_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: ExternalSecretsWebhookLog#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def level(self) -> typing.Optional[builtins.str]:
        '''
        :schema: ExternalSecretsWebhookLog#level
        '''
        result = self._values.get("level")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def time_encoding(self) -> typing.Optional[builtins.str]:
        '''
        :schema: ExternalSecretsWebhookLog#timeEncoding
        '''
        result = self._values.get("time_encoding")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ExternalSecretsWebhookLog(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="external-secrets.ExternalSecretsWebhookMetrics",
    jsii_struct_bases=[],
    name_mapping={
        "additional_values": "additionalValues",
        "listen": "listen",
        "service": "service",
    },
)
class ExternalSecretsWebhookMetrics:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        listen: typing.Optional[typing.Union["ExternalSecretsWebhookMetricsListen", typing.Dict[builtins.str, typing.Any]]] = None,
        service: typing.Optional[typing.Union["ExternalSecretsWebhookMetricsService", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.
        :param listen: 
        :param service: 

        :schema: ExternalSecretsWebhookMetrics
        '''
        if isinstance(listen, dict):
            listen = ExternalSecretsWebhookMetricsListen(**listen)
        if isinstance(service, dict):
            service = ExternalSecretsWebhookMetricsService(**service)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c87bf1ef9d48233299181b85a227faefe06a06d87b6461b564db477ec0f600ad)
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
            check_type(argname="argument listen", value=listen, expected_type=type_hints["listen"])
            check_type(argname="argument service", value=service, expected_type=type_hints["service"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_values is not None:
            self._values["additional_values"] = additional_values
        if listen is not None:
            self._values["listen"] = listen
        if service is not None:
            self._values["service"] = service

    @builtins.property
    def additional_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: ExternalSecretsWebhookMetrics#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def listen(self) -> typing.Optional["ExternalSecretsWebhookMetricsListen"]:
        '''
        :schema: ExternalSecretsWebhookMetrics#listen
        '''
        result = self._values.get("listen")
        return typing.cast(typing.Optional["ExternalSecretsWebhookMetricsListen"], result)

    @builtins.property
    def service(self) -> typing.Optional["ExternalSecretsWebhookMetricsService"]:
        '''
        :schema: ExternalSecretsWebhookMetrics#service
        '''
        result = self._values.get("service")
        return typing.cast(typing.Optional["ExternalSecretsWebhookMetricsService"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ExternalSecretsWebhookMetrics(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="external-secrets.ExternalSecretsWebhookMetricsListen",
    jsii_struct_bases=[],
    name_mapping={"additional_values": "additionalValues", "port": "port"},
)
class ExternalSecretsWebhookMetricsListen:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        port: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.
        :param port: 

        :schema: ExternalSecretsWebhookMetricsListen
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f2af75690bcd1b6bcbb32d9f377dd7706354cb4e81baefc6df99e33beb44befa)
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_values is not None:
            self._values["additional_values"] = additional_values
        if port is not None:
            self._values["port"] = port

    @builtins.property
    def additional_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: ExternalSecretsWebhookMetricsListen#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def port(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: ExternalSecretsWebhookMetricsListen#port
        '''
        result = self._values.get("port")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ExternalSecretsWebhookMetricsListen(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="external-secrets.ExternalSecretsWebhookMetricsService",
    jsii_struct_bases=[],
    name_mapping={
        "additional_values": "additionalValues",
        "annotations": "annotations",
        "enabled": "enabled",
        "port": "port",
    },
)
class ExternalSecretsWebhookMetricsService:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        annotations: typing.Optional[typing.Union["ExternalSecretsWebhookMetricsServiceAnnotations", typing.Dict[builtins.str, typing.Any]]] = None,
        enabled: typing.Optional[builtins.bool] = None,
        port: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.
        :param annotations: 
        :param enabled: 
        :param port: 

        :schema: ExternalSecretsWebhookMetricsService
        '''
        if isinstance(annotations, dict):
            annotations = ExternalSecretsWebhookMetricsServiceAnnotations(**annotations)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7a459169ca3b6afc64711e776b0868ec99b52454bf1bd4bcb67ac8d592e7d512)
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
            check_type(argname="argument annotations", value=annotations, expected_type=type_hints["annotations"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_values is not None:
            self._values["additional_values"] = additional_values
        if annotations is not None:
            self._values["annotations"] = annotations
        if enabled is not None:
            self._values["enabled"] = enabled
        if port is not None:
            self._values["port"] = port

    @builtins.property
    def additional_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: ExternalSecretsWebhookMetricsService#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def annotations(
        self,
    ) -> typing.Optional["ExternalSecretsWebhookMetricsServiceAnnotations"]:
        '''
        :schema: ExternalSecretsWebhookMetricsService#annotations
        '''
        result = self._values.get("annotations")
        return typing.cast(typing.Optional["ExternalSecretsWebhookMetricsServiceAnnotations"], result)

    @builtins.property
    def enabled(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: ExternalSecretsWebhookMetricsService#enabled
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def port(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: ExternalSecretsWebhookMetricsService#port
        '''
        result = self._values.get("port")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ExternalSecretsWebhookMetricsService(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="external-secrets.ExternalSecretsWebhookMetricsServiceAnnotations",
    jsii_struct_bases=[],
    name_mapping={"additional_values": "additionalValues"},
)
class ExternalSecretsWebhookMetricsServiceAnnotations:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: ExternalSecretsWebhookMetricsServiceAnnotations
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c72939b7bc6a1cd33a0af8e78ed62aa1a6438231c2bc018778b6536c06e6bbb5)
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_values is not None:
            self._values["additional_values"] = additional_values

    @builtins.property
    def additional_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: ExternalSecretsWebhookMetricsServiceAnnotations#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ExternalSecretsWebhookMetricsServiceAnnotations(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="external-secrets.ExternalSecretsWebhookNodeSelector",
    jsii_struct_bases=[],
    name_mapping={"additional_values": "additionalValues"},
)
class ExternalSecretsWebhookNodeSelector:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: ExternalSecretsWebhookNodeSelector
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a859107777f8af73f22ba880d0af6dc01b04d9655f8b644838b3030f9799f16b)
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_values is not None:
            self._values["additional_values"] = additional_values

    @builtins.property
    def additional_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: ExternalSecretsWebhookNodeSelector#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ExternalSecretsWebhookNodeSelector(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="external-secrets.ExternalSecretsWebhookPodAnnotations",
    jsii_struct_bases=[],
    name_mapping={"additional_values": "additionalValues"},
)
class ExternalSecretsWebhookPodAnnotations:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: ExternalSecretsWebhookPodAnnotations
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__90eee64ea4226ab9879b49849b4bc2df2fb361b4d6d2f567c16216f789373024)
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_values is not None:
            self._values["additional_values"] = additional_values

    @builtins.property
    def additional_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: ExternalSecretsWebhookPodAnnotations#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ExternalSecretsWebhookPodAnnotations(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="external-secrets.ExternalSecretsWebhookPodDisruptionBudget",
    jsii_struct_bases=[],
    name_mapping={
        "additional_values": "additionalValues",
        "enabled": "enabled",
        "min_available": "minAvailable",
    },
)
class ExternalSecretsWebhookPodDisruptionBudget:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        enabled: typing.Optional[builtins.bool] = None,
        min_available: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.
        :param enabled: 
        :param min_available: 

        :schema: ExternalSecretsWebhookPodDisruptionBudget
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a8db14aacfaffa28a264c6b1b65ae07d84c91245ccae2bc414d9ac018d238554)
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument min_available", value=min_available, expected_type=type_hints["min_available"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_values is not None:
            self._values["additional_values"] = additional_values
        if enabled is not None:
            self._values["enabled"] = enabled
        if min_available is not None:
            self._values["min_available"] = min_available

    @builtins.property
    def additional_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: ExternalSecretsWebhookPodDisruptionBudget#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def enabled(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: ExternalSecretsWebhookPodDisruptionBudget#enabled
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def min_available(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: ExternalSecretsWebhookPodDisruptionBudget#minAvailable
        '''
        result = self._values.get("min_available")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ExternalSecretsWebhookPodDisruptionBudget(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="external-secrets.ExternalSecretsWebhookPodLabels",
    jsii_struct_bases=[],
    name_mapping={"additional_values": "additionalValues"},
)
class ExternalSecretsWebhookPodLabels:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: ExternalSecretsWebhookPodLabels
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c7fd3147adddbf755d5d0f78b1a0711609a685d75fac7f77ef1b92dab55edc93)
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_values is not None:
            self._values["additional_values"] = additional_values

    @builtins.property
    def additional_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: ExternalSecretsWebhookPodLabels#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ExternalSecretsWebhookPodLabels(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="external-secrets.ExternalSecretsWebhookPodSecurityContext",
    jsii_struct_bases=[],
    name_mapping={"additional_values": "additionalValues", "enabled": "enabled"},
)
class ExternalSecretsWebhookPodSecurityContext:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        enabled: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.
        :param enabled: 

        :schema: ExternalSecretsWebhookPodSecurityContext
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a9015b5e8333af95af11f6f356d362cc2a8ff34cbcde4a07c5a109db2afbca4c)
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_values is not None:
            self._values["additional_values"] = additional_values
        if enabled is not None:
            self._values["enabled"] = enabled

    @builtins.property
    def additional_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: ExternalSecretsWebhookPodSecurityContext#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def enabled(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: ExternalSecretsWebhookPodSecurityContext#enabled
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ExternalSecretsWebhookPodSecurityContext(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="external-secrets.ExternalSecretsWebhookRbac",
    jsii_struct_bases=[],
    name_mapping={"additional_values": "additionalValues", "create": "create"},
)
class ExternalSecretsWebhookRbac:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        create: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.
        :param create: 

        :schema: ExternalSecretsWebhookRbac
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__119027cf1d7d295ad08574f0c1db01f2dee471fc3c200841508fca6417dbece5)
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_values is not None:
            self._values["additional_values"] = additional_values
        if create is not None:
            self._values["create"] = create

    @builtins.property
    def additional_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: ExternalSecretsWebhookRbac#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def create(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: ExternalSecretsWebhookRbac#create
        '''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ExternalSecretsWebhookRbac(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="external-secrets.ExternalSecretsWebhookReadinessProbe",
    jsii_struct_bases=[],
    name_mapping={
        "additional_values": "additionalValues",
        "address": "address",
        "port": "port",
    },
)
class ExternalSecretsWebhookReadinessProbe:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        address: typing.Optional[builtins.str] = None,
        port: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.
        :param address: 
        :param port: 

        :schema: ExternalSecretsWebhookReadinessProbe
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b5802c581d243e1cc0418a08ce9a820bbb77dacf55bcc639d64c2b314ea3b884)
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
            check_type(argname="argument address", value=address, expected_type=type_hints["address"])
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_values is not None:
            self._values["additional_values"] = additional_values
        if address is not None:
            self._values["address"] = address
        if port is not None:
            self._values["port"] = port

    @builtins.property
    def additional_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: ExternalSecretsWebhookReadinessProbe#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def address(self) -> typing.Optional[builtins.str]:
        '''
        :schema: ExternalSecretsWebhookReadinessProbe#address
        '''
        result = self._values.get("address")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def port(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: ExternalSecretsWebhookReadinessProbe#port
        '''
        result = self._values.get("port")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ExternalSecretsWebhookReadinessProbe(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="external-secrets.ExternalSecretsWebhookResources",
    jsii_struct_bases=[],
    name_mapping={"additional_values": "additionalValues"},
)
class ExternalSecretsWebhookResources:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: ExternalSecretsWebhookResources
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__211ae8e72fc9a783ee54153c4c66763729f6316304e502cd0c199f194d26fb6f)
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_values is not None:
            self._values["additional_values"] = additional_values

    @builtins.property
    def additional_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: ExternalSecretsWebhookResources#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ExternalSecretsWebhookResources(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="external-secrets.ExternalSecretsWebhookSecretAnnotations",
    jsii_struct_bases=[],
    name_mapping={"additional_values": "additionalValues"},
)
class ExternalSecretsWebhookSecretAnnotations:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: ExternalSecretsWebhookSecretAnnotations
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d4fa43b61bad8fa8dcffb1f468083127468e18d1a8e34c0806c87e3c8692f13d)
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_values is not None:
            self._values["additional_values"] = additional_values

    @builtins.property
    def additional_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: ExternalSecretsWebhookSecretAnnotations#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ExternalSecretsWebhookSecretAnnotations(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="external-secrets.ExternalSecretsWebhookSecurityContext",
    jsii_struct_bases=[],
    name_mapping={
        "additional_values": "additionalValues",
        "allow_privilege_escalation": "allowPrivilegeEscalation",
        "capabilities": "capabilities",
        "enabled": "enabled",
        "read_only_root_filesystem": "readOnlyRootFilesystem",
        "run_as_non_root": "runAsNonRoot",
        "run_as_user": "runAsUser",
        "seccomp_profile": "seccompProfile",
    },
)
class ExternalSecretsWebhookSecurityContext:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        allow_privilege_escalation: typing.Optional[builtins.bool] = None,
        capabilities: typing.Optional[typing.Union["ExternalSecretsWebhookSecurityContextCapabilities", typing.Dict[builtins.str, typing.Any]]] = None,
        enabled: typing.Optional[builtins.bool] = None,
        read_only_root_filesystem: typing.Optional[builtins.bool] = None,
        run_as_non_root: typing.Optional[builtins.bool] = None,
        run_as_user: typing.Optional[jsii.Number] = None,
        seccomp_profile: typing.Optional[typing.Union["ExternalSecretsWebhookSecurityContextSeccompProfile", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.
        :param allow_privilege_escalation: 
        :param capabilities: 
        :param enabled: 
        :param read_only_root_filesystem: 
        :param run_as_non_root: 
        :param run_as_user: 
        :param seccomp_profile: 

        :schema: ExternalSecretsWebhookSecurityContext
        '''
        if isinstance(capabilities, dict):
            capabilities = ExternalSecretsWebhookSecurityContextCapabilities(**capabilities)
        if isinstance(seccomp_profile, dict):
            seccomp_profile = ExternalSecretsWebhookSecurityContextSeccompProfile(**seccomp_profile)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d38be18bdead4131c032dacbf1c7a9e211342dd935475ab5c5982ceb61c44969)
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
            check_type(argname="argument allow_privilege_escalation", value=allow_privilege_escalation, expected_type=type_hints["allow_privilege_escalation"])
            check_type(argname="argument capabilities", value=capabilities, expected_type=type_hints["capabilities"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument read_only_root_filesystem", value=read_only_root_filesystem, expected_type=type_hints["read_only_root_filesystem"])
            check_type(argname="argument run_as_non_root", value=run_as_non_root, expected_type=type_hints["run_as_non_root"])
            check_type(argname="argument run_as_user", value=run_as_user, expected_type=type_hints["run_as_user"])
            check_type(argname="argument seccomp_profile", value=seccomp_profile, expected_type=type_hints["seccomp_profile"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_values is not None:
            self._values["additional_values"] = additional_values
        if allow_privilege_escalation is not None:
            self._values["allow_privilege_escalation"] = allow_privilege_escalation
        if capabilities is not None:
            self._values["capabilities"] = capabilities
        if enabled is not None:
            self._values["enabled"] = enabled
        if read_only_root_filesystem is not None:
            self._values["read_only_root_filesystem"] = read_only_root_filesystem
        if run_as_non_root is not None:
            self._values["run_as_non_root"] = run_as_non_root
        if run_as_user is not None:
            self._values["run_as_user"] = run_as_user
        if seccomp_profile is not None:
            self._values["seccomp_profile"] = seccomp_profile

    @builtins.property
    def additional_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: ExternalSecretsWebhookSecurityContext#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def allow_privilege_escalation(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: ExternalSecretsWebhookSecurityContext#allowPrivilegeEscalation
        '''
        result = self._values.get("allow_privilege_escalation")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def capabilities(
        self,
    ) -> typing.Optional["ExternalSecretsWebhookSecurityContextCapabilities"]:
        '''
        :schema: ExternalSecretsWebhookSecurityContext#capabilities
        '''
        result = self._values.get("capabilities")
        return typing.cast(typing.Optional["ExternalSecretsWebhookSecurityContextCapabilities"], result)

    @builtins.property
    def enabled(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: ExternalSecretsWebhookSecurityContext#enabled
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def read_only_root_filesystem(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: ExternalSecretsWebhookSecurityContext#readOnlyRootFilesystem
        '''
        result = self._values.get("read_only_root_filesystem")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def run_as_non_root(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: ExternalSecretsWebhookSecurityContext#runAsNonRoot
        '''
        result = self._values.get("run_as_non_root")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def run_as_user(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: ExternalSecretsWebhookSecurityContext#runAsUser
        '''
        result = self._values.get("run_as_user")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def seccomp_profile(
        self,
    ) -> typing.Optional["ExternalSecretsWebhookSecurityContextSeccompProfile"]:
        '''
        :schema: ExternalSecretsWebhookSecurityContext#seccompProfile
        '''
        result = self._values.get("seccomp_profile")
        return typing.cast(typing.Optional["ExternalSecretsWebhookSecurityContextSeccompProfile"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ExternalSecretsWebhookSecurityContext(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="external-secrets.ExternalSecretsWebhookSecurityContextCapabilities",
    jsii_struct_bases=[],
    name_mapping={"additional_values": "additionalValues", "drop": "drop"},
)
class ExternalSecretsWebhookSecurityContextCapabilities:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        drop: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.
        :param drop: 

        :schema: ExternalSecretsWebhookSecurityContextCapabilities
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3061c9999e96589e086a163de078b8aed89c8dad2dee841656a4943d30937127)
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
            check_type(argname="argument drop", value=drop, expected_type=type_hints["drop"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_values is not None:
            self._values["additional_values"] = additional_values
        if drop is not None:
            self._values["drop"] = drop

    @builtins.property
    def additional_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: ExternalSecretsWebhookSecurityContextCapabilities#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def drop(self) -> typing.Optional[typing.List[builtins.str]]:
        '''
        :schema: ExternalSecretsWebhookSecurityContextCapabilities#drop
        '''
        result = self._values.get("drop")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ExternalSecretsWebhookSecurityContextCapabilities(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="external-secrets.ExternalSecretsWebhookSecurityContextSeccompProfile",
    jsii_struct_bases=[],
    name_mapping={"additional_values": "additionalValues", "type": "type"},
)
class ExternalSecretsWebhookSecurityContextSeccompProfile:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.
        :param type: 

        :schema: ExternalSecretsWebhookSecurityContextSeccompProfile
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b93f794d1890a98f3519197b33e3accd93ab80f24c7af737b3381e6d865e22d6)
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_values is not None:
            self._values["additional_values"] = additional_values
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def additional_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: ExternalSecretsWebhookSecurityContextSeccompProfile#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: ExternalSecretsWebhookSecurityContextSeccompProfile#type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ExternalSecretsWebhookSecurityContextSeccompProfile(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="external-secrets.ExternalSecretsWebhookService",
    jsii_struct_bases=[],
    name_mapping={
        "additional_values": "additionalValues",
        "annotations": "annotations",
        "enabled": "enabled",
        "labels": "labels",
        "load_balancer_ip": "loadBalancerIp",
        "type": "type",
    },
)
class ExternalSecretsWebhookService:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        annotations: typing.Optional[typing.Union["ExternalSecretsWebhookServiceAnnotations", typing.Dict[builtins.str, typing.Any]]] = None,
        enabled: typing.Optional[builtins.bool] = None,
        labels: typing.Optional[typing.Union["ExternalSecretsWebhookServiceLabels", typing.Dict[builtins.str, typing.Any]]] = None,
        load_balancer_ip: typing.Optional[builtins.str] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.
        :param annotations: 
        :param enabled: 
        :param labels: 
        :param load_balancer_ip: 
        :param type: 

        :schema: ExternalSecretsWebhookService
        '''
        if isinstance(annotations, dict):
            annotations = ExternalSecretsWebhookServiceAnnotations(**annotations)
        if isinstance(labels, dict):
            labels = ExternalSecretsWebhookServiceLabels(**labels)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b89b3e4e255c9137c31be38fcf5cfd6e04abd22708d2d11f2f89d332d40dd134)
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
            check_type(argname="argument annotations", value=annotations, expected_type=type_hints["annotations"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument labels", value=labels, expected_type=type_hints["labels"])
            check_type(argname="argument load_balancer_ip", value=load_balancer_ip, expected_type=type_hints["load_balancer_ip"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_values is not None:
            self._values["additional_values"] = additional_values
        if annotations is not None:
            self._values["annotations"] = annotations
        if enabled is not None:
            self._values["enabled"] = enabled
        if labels is not None:
            self._values["labels"] = labels
        if load_balancer_ip is not None:
            self._values["load_balancer_ip"] = load_balancer_ip
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def additional_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: ExternalSecretsWebhookService#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def annotations(
        self,
    ) -> typing.Optional["ExternalSecretsWebhookServiceAnnotations"]:
        '''
        :schema: ExternalSecretsWebhookService#annotations
        '''
        result = self._values.get("annotations")
        return typing.cast(typing.Optional["ExternalSecretsWebhookServiceAnnotations"], result)

    @builtins.property
    def enabled(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: ExternalSecretsWebhookService#enabled
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def labels(self) -> typing.Optional["ExternalSecretsWebhookServiceLabels"]:
        '''
        :schema: ExternalSecretsWebhookService#labels
        '''
        result = self._values.get("labels")
        return typing.cast(typing.Optional["ExternalSecretsWebhookServiceLabels"], result)

    @builtins.property
    def load_balancer_ip(self) -> typing.Optional[builtins.str]:
        '''
        :schema: ExternalSecretsWebhookService#loadBalancerIP
        '''
        result = self._values.get("load_balancer_ip")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: ExternalSecretsWebhookService#type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ExternalSecretsWebhookService(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="external-secrets.ExternalSecretsWebhookServiceAccount",
    jsii_struct_bases=[],
    name_mapping={
        "additional_values": "additionalValues",
        "annotations": "annotations",
        "automount": "automount",
        "create": "create",
        "extra_labels": "extraLabels",
        "name": "name",
    },
)
class ExternalSecretsWebhookServiceAccount:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        annotations: typing.Optional[typing.Union["ExternalSecretsWebhookServiceAccountAnnotations", typing.Dict[builtins.str, typing.Any]]] = None,
        automount: typing.Optional[builtins.bool] = None,
        create: typing.Optional[builtins.bool] = None,
        extra_labels: typing.Optional[typing.Union["ExternalSecretsWebhookServiceAccountExtraLabels", typing.Dict[builtins.str, typing.Any]]] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.
        :param annotations: 
        :param automount: 
        :param create: 
        :param extra_labels: 
        :param name: 

        :schema: ExternalSecretsWebhookServiceAccount
        '''
        if isinstance(annotations, dict):
            annotations = ExternalSecretsWebhookServiceAccountAnnotations(**annotations)
        if isinstance(extra_labels, dict):
            extra_labels = ExternalSecretsWebhookServiceAccountExtraLabels(**extra_labels)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fbda51c0b17f7330a35dc25c1fac85c55911a5f3f47a0f4572400c0c269b53db)
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
            check_type(argname="argument annotations", value=annotations, expected_type=type_hints["annotations"])
            check_type(argname="argument automount", value=automount, expected_type=type_hints["automount"])
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
            check_type(argname="argument extra_labels", value=extra_labels, expected_type=type_hints["extra_labels"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_values is not None:
            self._values["additional_values"] = additional_values
        if annotations is not None:
            self._values["annotations"] = annotations
        if automount is not None:
            self._values["automount"] = automount
        if create is not None:
            self._values["create"] = create
        if extra_labels is not None:
            self._values["extra_labels"] = extra_labels
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def additional_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: ExternalSecretsWebhookServiceAccount#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def annotations(
        self,
    ) -> typing.Optional["ExternalSecretsWebhookServiceAccountAnnotations"]:
        '''
        :schema: ExternalSecretsWebhookServiceAccount#annotations
        '''
        result = self._values.get("annotations")
        return typing.cast(typing.Optional["ExternalSecretsWebhookServiceAccountAnnotations"], result)

    @builtins.property
    def automount(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: ExternalSecretsWebhookServiceAccount#automount
        '''
        result = self._values.get("automount")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def create(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: ExternalSecretsWebhookServiceAccount#create
        '''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def extra_labels(
        self,
    ) -> typing.Optional["ExternalSecretsWebhookServiceAccountExtraLabels"]:
        '''
        :schema: ExternalSecretsWebhookServiceAccount#extraLabels
        '''
        result = self._values.get("extra_labels")
        return typing.cast(typing.Optional["ExternalSecretsWebhookServiceAccountExtraLabels"], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''
        :schema: ExternalSecretsWebhookServiceAccount#name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ExternalSecretsWebhookServiceAccount(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="external-secrets.ExternalSecretsWebhookServiceAccountAnnotations",
    jsii_struct_bases=[],
    name_mapping={"additional_values": "additionalValues"},
)
class ExternalSecretsWebhookServiceAccountAnnotations:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: ExternalSecretsWebhookServiceAccountAnnotations
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1ffd445a6907cef4e4006e70b6522c61355c8653f32779cb617b481c7e798890)
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_values is not None:
            self._values["additional_values"] = additional_values

    @builtins.property
    def additional_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: ExternalSecretsWebhookServiceAccountAnnotations#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ExternalSecretsWebhookServiceAccountAnnotations(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="external-secrets.ExternalSecretsWebhookServiceAccountExtraLabels",
    jsii_struct_bases=[],
    name_mapping={"additional_values": "additionalValues"},
)
class ExternalSecretsWebhookServiceAccountExtraLabels:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: ExternalSecretsWebhookServiceAccountExtraLabels
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c948ee0ae534ea6581d47534a3c8ddca66680ea2e02f906a8c97b8b232e3a1a5)
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_values is not None:
            self._values["additional_values"] = additional_values

    @builtins.property
    def additional_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: ExternalSecretsWebhookServiceAccountExtraLabels#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ExternalSecretsWebhookServiceAccountExtraLabels(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="external-secrets.ExternalSecretsWebhookServiceAnnotations",
    jsii_struct_bases=[],
    name_mapping={"additional_values": "additionalValues"},
)
class ExternalSecretsWebhookServiceAnnotations:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: ExternalSecretsWebhookServiceAnnotations
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__94540b5998d1ec75cafe6b911c8bd5eeb762804a2d4a16fc5178d63a5be024a9)
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_values is not None:
            self._values["additional_values"] = additional_values

    @builtins.property
    def additional_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: ExternalSecretsWebhookServiceAnnotations#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ExternalSecretsWebhookServiceAnnotations(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="external-secrets.ExternalSecretsWebhookServiceLabels",
    jsii_struct_bases=[],
    name_mapping={"additional_values": "additionalValues"},
)
class ExternalSecretsWebhookServiceLabels:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: ExternalSecretsWebhookServiceLabels
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5a71716dfdcbe8f3ef28bb246c973edcb3e38cd31e4e829acd20cbaaedb337a5)
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_values is not None:
            self._values["additional_values"] = additional_values

    @builtins.property
    def additional_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: ExternalSecretsWebhookServiceLabels#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ExternalSecretsWebhookServiceLabels(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Externalsecrets(
    _constructs_77d1e7e8.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="external-secrets.Externalsecrets",
):
    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        helm_executable: typing.Optional[builtins.str] = None,
        helm_flags: typing.Optional[typing.Sequence[builtins.str]] = None,
        namespace: typing.Optional[builtins.str] = None,
        release_name: typing.Optional[builtins.str] = None,
        values: typing.Optional[typing.Union["ExternalsecretsValues", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param helm_executable: -
        :param helm_flags: -
        :param namespace: -
        :param release_name: -
        :param values: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6040049eae66ad607f76227ecce16bccd5fb16452bf1e97da81d7c3b0a5221df)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = ExternalsecretsProps(
            helm_executable=helm_executable,
            helm_flags=helm_flags,
            namespace=namespace,
            release_name=release_name,
            values=values,
        )

        jsii.create(self.__class__, self, [scope, id, props])


@jsii.data_type(
    jsii_type="external-secrets.ExternalsecretsProps",
    jsii_struct_bases=[],
    name_mapping={
        "helm_executable": "helmExecutable",
        "helm_flags": "helmFlags",
        "namespace": "namespace",
        "release_name": "releaseName",
        "values": "values",
    },
)
class ExternalsecretsProps:
    def __init__(
        self,
        *,
        helm_executable: typing.Optional[builtins.str] = None,
        helm_flags: typing.Optional[typing.Sequence[builtins.str]] = None,
        namespace: typing.Optional[builtins.str] = None,
        release_name: typing.Optional[builtins.str] = None,
        values: typing.Optional[typing.Union["ExternalsecretsValues", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param helm_executable: -
        :param helm_flags: -
        :param namespace: -
        :param release_name: -
        :param values: -
        '''
        if isinstance(values, dict):
            values = ExternalsecretsValues(**values)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8ab95e6d37f6032d4a30183c33df1e0cc7a3064fe3ea5582a0a7c6eff645b525)
            check_type(argname="argument helm_executable", value=helm_executable, expected_type=type_hints["helm_executable"])
            check_type(argname="argument helm_flags", value=helm_flags, expected_type=type_hints["helm_flags"])
            check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
            check_type(argname="argument release_name", value=release_name, expected_type=type_hints["release_name"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if helm_executable is not None:
            self._values["helm_executable"] = helm_executable
        if helm_flags is not None:
            self._values["helm_flags"] = helm_flags
        if namespace is not None:
            self._values["namespace"] = namespace
        if release_name is not None:
            self._values["release_name"] = release_name
        if values is not None:
            self._values["values"] = values

    @builtins.property
    def helm_executable(self) -> typing.Optional[builtins.str]:
        result = self._values.get("helm_executable")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def helm_flags(self) -> typing.Optional[typing.List[builtins.str]]:
        result = self._values.get("helm_flags")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def namespace(self) -> typing.Optional[builtins.str]:
        result = self._values.get("namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def release_name(self) -> typing.Optional[builtins.str]:
        result = self._values.get("release_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def values(self) -> typing.Optional["ExternalsecretsValues"]:
        result = self._values.get("values")
        return typing.cast(typing.Optional["ExternalsecretsValues"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ExternalsecretsProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="external-secrets.ExternalsecretsValues",
    jsii_struct_bases=[],
    name_mapping={
        "additional_values": "additionalValues",
        "affinity": "affinity",
        "bitwarden_sdk_server": "bitwardenSdkServer",
        "cert_controller": "certController",
        "common_labels": "commonLabels",
        "concurrent": "concurrent",
        "controller_class": "controllerClass",
        "crds": "crds",
        "create_operator": "createOperator",
        "deployment_annotations": "deploymentAnnotations",
        "dns_config": "dnsConfig",
        "dns_policy": "dnsPolicy",
        "extended_metric_labels": "extendedMetricLabels",
        "extra_args": "extraArgs",
        "extra_containers": "extraContainers",
        "extra_env": "extraEnv",
        "extra_objects": "extraObjects",
        "extra_volume_mounts": "extraVolumeMounts",
        "extra_volumes": "extraVolumes",
        "fullname_override": "fullnameOverride",
        "global_": "global",
        "grafana_dashboard": "grafanaDashboard",
        "host_network": "hostNetwork",
        "image": "image",
        "image_pull_secrets": "imagePullSecrets",
        "install_cr_ds": "installCrDs",
        "leader_elect": "leaderElect",
        "log": "log",
        "metrics": "metrics",
        "name_override": "nameOverride",
        "namespace_override": "namespaceOverride",
        "node_selector": "nodeSelector",
        "openshift_finalizers": "openshiftFinalizers",
        "pod_annotations": "podAnnotations",
        "pod_disruption_budget": "podDisruptionBudget",
        "pod_labels": "podLabels",
        "pod_security_context": "podSecurityContext",
        "pod_spec_extra": "podSpecExtra",
        "priority_class_name": "priorityClassName",
        "process_cluster_external_secret": "processClusterExternalSecret",
        "process_cluster_push_secret": "processClusterPushSecret",
        "process_cluster_store": "processClusterStore",
        "process_push_secret": "processPushSecret",
        "rbac": "rbac",
        "replica_count": "replicaCount",
        "resources": "resources",
        "revision_history_limit": "revisionHistoryLimit",
        "scoped_namespace": "scopedNamespace",
        "scoped_rbac": "scopedRbac",
        "security_context": "securityContext",
        "service": "service",
        "service_account": "serviceAccount",
        "service_monitor": "serviceMonitor",
        "tolerations": "tolerations",
        "topology_spread_constraints": "topologySpreadConstraints",
        "webhook": "webhook",
    },
)
class ExternalsecretsValues:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        affinity: typing.Optional[typing.Union[ExternalSecretsAffinity, typing.Dict[builtins.str, typing.Any]]] = None,
        bitwarden_sdk_server: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        cert_controller: typing.Optional[typing.Union[ExternalSecretsCertController, typing.Dict[builtins.str, typing.Any]]] = None,
        common_labels: typing.Optional[typing.Union[ExternalSecretsCommonLabels, typing.Dict[builtins.str, typing.Any]]] = None,
        concurrent: typing.Optional[jsii.Number] = None,
        controller_class: typing.Optional[builtins.str] = None,
        crds: typing.Optional[typing.Union[ExternalSecretsCrds, typing.Dict[builtins.str, typing.Any]]] = None,
        create_operator: typing.Optional[builtins.bool] = None,
        deployment_annotations: typing.Optional[typing.Union[ExternalSecretsDeploymentAnnotations, typing.Dict[builtins.str, typing.Any]]] = None,
        dns_config: typing.Optional[typing.Union[ExternalSecretsDnsConfig, typing.Dict[builtins.str, typing.Any]]] = None,
        dns_policy: typing.Optional[builtins.str] = None,
        extended_metric_labels: typing.Optional[builtins.bool] = None,
        extra_args: typing.Optional[typing.Union[ExternalSecretsExtraArgs, typing.Dict[builtins.str, typing.Any]]] = None,
        extra_containers: typing.Optional[typing.Sequence[typing.Any]] = None,
        extra_env: typing.Optional[typing.Sequence[typing.Any]] = None,
        extra_objects: typing.Optional[typing.Sequence[typing.Any]] = None,
        extra_volume_mounts: typing.Optional[typing.Sequence[typing.Any]] = None,
        extra_volumes: typing.Optional[typing.Sequence[typing.Any]] = None,
        fullname_override: typing.Optional[builtins.str] = None,
        global_: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        grafana_dashboard: typing.Optional[typing.Union[ExternalSecretsGrafanaDashboard, typing.Dict[builtins.str, typing.Any]]] = None,
        host_network: typing.Optional[builtins.bool] = None,
        image: typing.Optional[typing.Union[ExternalSecretsImage, typing.Dict[builtins.str, typing.Any]]] = None,
        image_pull_secrets: typing.Optional[typing.Sequence[typing.Any]] = None,
        install_cr_ds: typing.Optional[builtins.bool] = None,
        leader_elect: typing.Optional[builtins.bool] = None,
        log: typing.Optional[typing.Union[ExternalSecretsLog, typing.Dict[builtins.str, typing.Any]]] = None,
        metrics: typing.Optional[typing.Union[ExternalSecretsMetrics, typing.Dict[builtins.str, typing.Any]]] = None,
        name_override: typing.Optional[builtins.str] = None,
        namespace_override: typing.Optional[builtins.str] = None,
        node_selector: typing.Optional[typing.Union[ExternalSecretsNodeSelector, typing.Dict[builtins.str, typing.Any]]] = None,
        openshift_finalizers: typing.Optional[builtins.bool] = None,
        pod_annotations: typing.Optional[typing.Union[ExternalSecretsPodAnnotations, typing.Dict[builtins.str, typing.Any]]] = None,
        pod_disruption_budget: typing.Optional[typing.Union[ExternalSecretsPodDisruptionBudget, typing.Dict[builtins.str, typing.Any]]] = None,
        pod_labels: typing.Optional[typing.Union[ExternalSecretsPodLabels, typing.Dict[builtins.str, typing.Any]]] = None,
        pod_security_context: typing.Optional[typing.Union[ExternalSecretsPodSecurityContext, typing.Dict[builtins.str, typing.Any]]] = None,
        pod_spec_extra: typing.Optional[typing.Union[ExternalSecretsPodSpecExtra, typing.Dict[builtins.str, typing.Any]]] = None,
        priority_class_name: typing.Optional[builtins.str] = None,
        process_cluster_external_secret: typing.Optional[builtins.bool] = None,
        process_cluster_push_secret: typing.Optional[builtins.bool] = None,
        process_cluster_store: typing.Optional[builtins.bool] = None,
        process_push_secret: typing.Optional[builtins.bool] = None,
        rbac: typing.Optional[typing.Union[ExternalSecretsRbac, typing.Dict[builtins.str, typing.Any]]] = None,
        replica_count: typing.Optional[jsii.Number] = None,
        resources: typing.Optional[typing.Union[ExternalSecretsResources, typing.Dict[builtins.str, typing.Any]]] = None,
        revision_history_limit: typing.Optional[jsii.Number] = None,
        scoped_namespace: typing.Optional[builtins.str] = None,
        scoped_rbac: typing.Optional[builtins.bool] = None,
        security_context: typing.Optional[typing.Union[ExternalSecretsSecurityContext, typing.Dict[builtins.str, typing.Any]]] = None,
        service: typing.Optional[typing.Union[ExternalSecretsService, typing.Dict[builtins.str, typing.Any]]] = None,
        service_account: typing.Optional[typing.Union[ExternalSecretsServiceAccount, typing.Dict[builtins.str, typing.Any]]] = None,
        service_monitor: typing.Optional[typing.Union[ExternalSecretsServiceMonitor, typing.Dict[builtins.str, typing.Any]]] = None,
        tolerations: typing.Optional[typing.Sequence[typing.Any]] = None,
        topology_spread_constraints: typing.Optional[typing.Sequence[typing.Any]] = None,
        webhook: typing.Optional[typing.Union[ExternalSecretsWebhook, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.
        :param affinity: 
        :param bitwarden_sdk_server: 
        :param cert_controller: 
        :param common_labels: 
        :param concurrent: 
        :param controller_class: 
        :param crds: 
        :param create_operator: 
        :param deployment_annotations: 
        :param dns_config: 
        :param dns_policy: 
        :param extended_metric_labels: 
        :param extra_args: 
        :param extra_containers: 
        :param extra_env: 
        :param extra_objects: 
        :param extra_volume_mounts: 
        :param extra_volumes: 
        :param fullname_override: 
        :param global_: 
        :param grafana_dashboard: 
        :param host_network: 
        :param image: 
        :param image_pull_secrets: 
        :param install_cr_ds: 
        :param leader_elect: 
        :param log: 
        :param metrics: 
        :param name_override: 
        :param namespace_override: 
        :param node_selector: 
        :param openshift_finalizers: 
        :param pod_annotations: 
        :param pod_disruption_budget: 
        :param pod_labels: 
        :param pod_security_context: 
        :param pod_spec_extra: 
        :param priority_class_name: 
        :param process_cluster_external_secret: 
        :param process_cluster_push_secret: 
        :param process_cluster_store: 
        :param process_push_secret: 
        :param rbac: 
        :param replica_count: 
        :param resources: 
        :param revision_history_limit: 
        :param scoped_namespace: 
        :param scoped_rbac: 
        :param security_context: 
        :param service: 
        :param service_account: 
        :param service_monitor: 
        :param tolerations: 
        :param topology_spread_constraints: 
        :param webhook: 

        :schema: external-secrets
        '''
        if isinstance(affinity, dict):
            affinity = ExternalSecretsAffinity(**affinity)
        if isinstance(cert_controller, dict):
            cert_controller = ExternalSecretsCertController(**cert_controller)
        if isinstance(common_labels, dict):
            common_labels = ExternalSecretsCommonLabels(**common_labels)
        if isinstance(crds, dict):
            crds = ExternalSecretsCrds(**crds)
        if isinstance(deployment_annotations, dict):
            deployment_annotations = ExternalSecretsDeploymentAnnotations(**deployment_annotations)
        if isinstance(dns_config, dict):
            dns_config = ExternalSecretsDnsConfig(**dns_config)
        if isinstance(extra_args, dict):
            extra_args = ExternalSecretsExtraArgs(**extra_args)
        if isinstance(grafana_dashboard, dict):
            grafana_dashboard = ExternalSecretsGrafanaDashboard(**grafana_dashboard)
        if isinstance(image, dict):
            image = ExternalSecretsImage(**image)
        if isinstance(log, dict):
            log = ExternalSecretsLog(**log)
        if isinstance(metrics, dict):
            metrics = ExternalSecretsMetrics(**metrics)
        if isinstance(node_selector, dict):
            node_selector = ExternalSecretsNodeSelector(**node_selector)
        if isinstance(pod_annotations, dict):
            pod_annotations = ExternalSecretsPodAnnotations(**pod_annotations)
        if isinstance(pod_disruption_budget, dict):
            pod_disruption_budget = ExternalSecretsPodDisruptionBudget(**pod_disruption_budget)
        if isinstance(pod_labels, dict):
            pod_labels = ExternalSecretsPodLabels(**pod_labels)
        if isinstance(pod_security_context, dict):
            pod_security_context = ExternalSecretsPodSecurityContext(**pod_security_context)
        if isinstance(pod_spec_extra, dict):
            pod_spec_extra = ExternalSecretsPodSpecExtra(**pod_spec_extra)
        if isinstance(rbac, dict):
            rbac = ExternalSecretsRbac(**rbac)
        if isinstance(resources, dict):
            resources = ExternalSecretsResources(**resources)
        if isinstance(security_context, dict):
            security_context = ExternalSecretsSecurityContext(**security_context)
        if isinstance(service, dict):
            service = ExternalSecretsService(**service)
        if isinstance(service_account, dict):
            service_account = ExternalSecretsServiceAccount(**service_account)
        if isinstance(service_monitor, dict):
            service_monitor = ExternalSecretsServiceMonitor(**service_monitor)
        if isinstance(webhook, dict):
            webhook = ExternalSecretsWebhook(**webhook)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c534e8f71d825c8aa85c89da03ff575eafee9ff0758222d9ebc53ffbdc02b978)
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
            check_type(argname="argument affinity", value=affinity, expected_type=type_hints["affinity"])
            check_type(argname="argument bitwarden_sdk_server", value=bitwarden_sdk_server, expected_type=type_hints["bitwarden_sdk_server"])
            check_type(argname="argument cert_controller", value=cert_controller, expected_type=type_hints["cert_controller"])
            check_type(argname="argument common_labels", value=common_labels, expected_type=type_hints["common_labels"])
            check_type(argname="argument concurrent", value=concurrent, expected_type=type_hints["concurrent"])
            check_type(argname="argument controller_class", value=controller_class, expected_type=type_hints["controller_class"])
            check_type(argname="argument crds", value=crds, expected_type=type_hints["crds"])
            check_type(argname="argument create_operator", value=create_operator, expected_type=type_hints["create_operator"])
            check_type(argname="argument deployment_annotations", value=deployment_annotations, expected_type=type_hints["deployment_annotations"])
            check_type(argname="argument dns_config", value=dns_config, expected_type=type_hints["dns_config"])
            check_type(argname="argument dns_policy", value=dns_policy, expected_type=type_hints["dns_policy"])
            check_type(argname="argument extended_metric_labels", value=extended_metric_labels, expected_type=type_hints["extended_metric_labels"])
            check_type(argname="argument extra_args", value=extra_args, expected_type=type_hints["extra_args"])
            check_type(argname="argument extra_containers", value=extra_containers, expected_type=type_hints["extra_containers"])
            check_type(argname="argument extra_env", value=extra_env, expected_type=type_hints["extra_env"])
            check_type(argname="argument extra_objects", value=extra_objects, expected_type=type_hints["extra_objects"])
            check_type(argname="argument extra_volume_mounts", value=extra_volume_mounts, expected_type=type_hints["extra_volume_mounts"])
            check_type(argname="argument extra_volumes", value=extra_volumes, expected_type=type_hints["extra_volumes"])
            check_type(argname="argument fullname_override", value=fullname_override, expected_type=type_hints["fullname_override"])
            check_type(argname="argument global_", value=global_, expected_type=type_hints["global_"])
            check_type(argname="argument grafana_dashboard", value=grafana_dashboard, expected_type=type_hints["grafana_dashboard"])
            check_type(argname="argument host_network", value=host_network, expected_type=type_hints["host_network"])
            check_type(argname="argument image", value=image, expected_type=type_hints["image"])
            check_type(argname="argument image_pull_secrets", value=image_pull_secrets, expected_type=type_hints["image_pull_secrets"])
            check_type(argname="argument install_cr_ds", value=install_cr_ds, expected_type=type_hints["install_cr_ds"])
            check_type(argname="argument leader_elect", value=leader_elect, expected_type=type_hints["leader_elect"])
            check_type(argname="argument log", value=log, expected_type=type_hints["log"])
            check_type(argname="argument metrics", value=metrics, expected_type=type_hints["metrics"])
            check_type(argname="argument name_override", value=name_override, expected_type=type_hints["name_override"])
            check_type(argname="argument namespace_override", value=namespace_override, expected_type=type_hints["namespace_override"])
            check_type(argname="argument node_selector", value=node_selector, expected_type=type_hints["node_selector"])
            check_type(argname="argument openshift_finalizers", value=openshift_finalizers, expected_type=type_hints["openshift_finalizers"])
            check_type(argname="argument pod_annotations", value=pod_annotations, expected_type=type_hints["pod_annotations"])
            check_type(argname="argument pod_disruption_budget", value=pod_disruption_budget, expected_type=type_hints["pod_disruption_budget"])
            check_type(argname="argument pod_labels", value=pod_labels, expected_type=type_hints["pod_labels"])
            check_type(argname="argument pod_security_context", value=pod_security_context, expected_type=type_hints["pod_security_context"])
            check_type(argname="argument pod_spec_extra", value=pod_spec_extra, expected_type=type_hints["pod_spec_extra"])
            check_type(argname="argument priority_class_name", value=priority_class_name, expected_type=type_hints["priority_class_name"])
            check_type(argname="argument process_cluster_external_secret", value=process_cluster_external_secret, expected_type=type_hints["process_cluster_external_secret"])
            check_type(argname="argument process_cluster_push_secret", value=process_cluster_push_secret, expected_type=type_hints["process_cluster_push_secret"])
            check_type(argname="argument process_cluster_store", value=process_cluster_store, expected_type=type_hints["process_cluster_store"])
            check_type(argname="argument process_push_secret", value=process_push_secret, expected_type=type_hints["process_push_secret"])
            check_type(argname="argument rbac", value=rbac, expected_type=type_hints["rbac"])
            check_type(argname="argument replica_count", value=replica_count, expected_type=type_hints["replica_count"])
            check_type(argname="argument resources", value=resources, expected_type=type_hints["resources"])
            check_type(argname="argument revision_history_limit", value=revision_history_limit, expected_type=type_hints["revision_history_limit"])
            check_type(argname="argument scoped_namespace", value=scoped_namespace, expected_type=type_hints["scoped_namespace"])
            check_type(argname="argument scoped_rbac", value=scoped_rbac, expected_type=type_hints["scoped_rbac"])
            check_type(argname="argument security_context", value=security_context, expected_type=type_hints["security_context"])
            check_type(argname="argument service", value=service, expected_type=type_hints["service"])
            check_type(argname="argument service_account", value=service_account, expected_type=type_hints["service_account"])
            check_type(argname="argument service_monitor", value=service_monitor, expected_type=type_hints["service_monitor"])
            check_type(argname="argument tolerations", value=tolerations, expected_type=type_hints["tolerations"])
            check_type(argname="argument topology_spread_constraints", value=topology_spread_constraints, expected_type=type_hints["topology_spread_constraints"])
            check_type(argname="argument webhook", value=webhook, expected_type=type_hints["webhook"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_values is not None:
            self._values["additional_values"] = additional_values
        if affinity is not None:
            self._values["affinity"] = affinity
        if bitwarden_sdk_server is not None:
            self._values["bitwarden_sdk_server"] = bitwarden_sdk_server
        if cert_controller is not None:
            self._values["cert_controller"] = cert_controller
        if common_labels is not None:
            self._values["common_labels"] = common_labels
        if concurrent is not None:
            self._values["concurrent"] = concurrent
        if controller_class is not None:
            self._values["controller_class"] = controller_class
        if crds is not None:
            self._values["crds"] = crds
        if create_operator is not None:
            self._values["create_operator"] = create_operator
        if deployment_annotations is not None:
            self._values["deployment_annotations"] = deployment_annotations
        if dns_config is not None:
            self._values["dns_config"] = dns_config
        if dns_policy is not None:
            self._values["dns_policy"] = dns_policy
        if extended_metric_labels is not None:
            self._values["extended_metric_labels"] = extended_metric_labels
        if extra_args is not None:
            self._values["extra_args"] = extra_args
        if extra_containers is not None:
            self._values["extra_containers"] = extra_containers
        if extra_env is not None:
            self._values["extra_env"] = extra_env
        if extra_objects is not None:
            self._values["extra_objects"] = extra_objects
        if extra_volume_mounts is not None:
            self._values["extra_volume_mounts"] = extra_volume_mounts
        if extra_volumes is not None:
            self._values["extra_volumes"] = extra_volumes
        if fullname_override is not None:
            self._values["fullname_override"] = fullname_override
        if global_ is not None:
            self._values["global_"] = global_
        if grafana_dashboard is not None:
            self._values["grafana_dashboard"] = grafana_dashboard
        if host_network is not None:
            self._values["host_network"] = host_network
        if image is not None:
            self._values["image"] = image
        if image_pull_secrets is not None:
            self._values["image_pull_secrets"] = image_pull_secrets
        if install_cr_ds is not None:
            self._values["install_cr_ds"] = install_cr_ds
        if leader_elect is not None:
            self._values["leader_elect"] = leader_elect
        if log is not None:
            self._values["log"] = log
        if metrics is not None:
            self._values["metrics"] = metrics
        if name_override is not None:
            self._values["name_override"] = name_override
        if namespace_override is not None:
            self._values["namespace_override"] = namespace_override
        if node_selector is not None:
            self._values["node_selector"] = node_selector
        if openshift_finalizers is not None:
            self._values["openshift_finalizers"] = openshift_finalizers
        if pod_annotations is not None:
            self._values["pod_annotations"] = pod_annotations
        if pod_disruption_budget is not None:
            self._values["pod_disruption_budget"] = pod_disruption_budget
        if pod_labels is not None:
            self._values["pod_labels"] = pod_labels
        if pod_security_context is not None:
            self._values["pod_security_context"] = pod_security_context
        if pod_spec_extra is not None:
            self._values["pod_spec_extra"] = pod_spec_extra
        if priority_class_name is not None:
            self._values["priority_class_name"] = priority_class_name
        if process_cluster_external_secret is not None:
            self._values["process_cluster_external_secret"] = process_cluster_external_secret
        if process_cluster_push_secret is not None:
            self._values["process_cluster_push_secret"] = process_cluster_push_secret
        if process_cluster_store is not None:
            self._values["process_cluster_store"] = process_cluster_store
        if process_push_secret is not None:
            self._values["process_push_secret"] = process_push_secret
        if rbac is not None:
            self._values["rbac"] = rbac
        if replica_count is not None:
            self._values["replica_count"] = replica_count
        if resources is not None:
            self._values["resources"] = resources
        if revision_history_limit is not None:
            self._values["revision_history_limit"] = revision_history_limit
        if scoped_namespace is not None:
            self._values["scoped_namespace"] = scoped_namespace
        if scoped_rbac is not None:
            self._values["scoped_rbac"] = scoped_rbac
        if security_context is not None:
            self._values["security_context"] = security_context
        if service is not None:
            self._values["service"] = service
        if service_account is not None:
            self._values["service_account"] = service_account
        if service_monitor is not None:
            self._values["service_monitor"] = service_monitor
        if tolerations is not None:
            self._values["tolerations"] = tolerations
        if topology_spread_constraints is not None:
            self._values["topology_spread_constraints"] = topology_spread_constraints
        if webhook is not None:
            self._values["webhook"] = webhook

    @builtins.property
    def additional_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: external-secrets#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def affinity(self) -> typing.Optional[ExternalSecretsAffinity]:
        '''
        :schema: external-secrets#affinity
        '''
        result = self._values.get("affinity")
        return typing.cast(typing.Optional[ExternalSecretsAffinity], result)

    @builtins.property
    def bitwarden_sdk_server(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''
        :schema: external-secrets#bitwarden-sdk-server
        '''
        result = self._values.get("bitwarden_sdk_server")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def cert_controller(self) -> typing.Optional[ExternalSecretsCertController]:
        '''
        :schema: external-secrets#certController
        '''
        result = self._values.get("cert_controller")
        return typing.cast(typing.Optional[ExternalSecretsCertController], result)

    @builtins.property
    def common_labels(self) -> typing.Optional[ExternalSecretsCommonLabels]:
        '''
        :schema: external-secrets#commonLabels
        '''
        result = self._values.get("common_labels")
        return typing.cast(typing.Optional[ExternalSecretsCommonLabels], result)

    @builtins.property
    def concurrent(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: external-secrets#concurrent
        '''
        result = self._values.get("concurrent")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def controller_class(self) -> typing.Optional[builtins.str]:
        '''
        :schema: external-secrets#controllerClass
        '''
        result = self._values.get("controller_class")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def crds(self) -> typing.Optional[ExternalSecretsCrds]:
        '''
        :schema: external-secrets#crds
        '''
        result = self._values.get("crds")
        return typing.cast(typing.Optional[ExternalSecretsCrds], result)

    @builtins.property
    def create_operator(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: external-secrets#createOperator
        '''
        result = self._values.get("create_operator")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def deployment_annotations(
        self,
    ) -> typing.Optional[ExternalSecretsDeploymentAnnotations]:
        '''
        :schema: external-secrets#deploymentAnnotations
        '''
        result = self._values.get("deployment_annotations")
        return typing.cast(typing.Optional[ExternalSecretsDeploymentAnnotations], result)

    @builtins.property
    def dns_config(self) -> typing.Optional[ExternalSecretsDnsConfig]:
        '''
        :schema: external-secrets#dnsConfig
        '''
        result = self._values.get("dns_config")
        return typing.cast(typing.Optional[ExternalSecretsDnsConfig], result)

    @builtins.property
    def dns_policy(self) -> typing.Optional[builtins.str]:
        '''
        :schema: external-secrets#dnsPolicy
        '''
        result = self._values.get("dns_policy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def extended_metric_labels(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: external-secrets#extendedMetricLabels
        '''
        result = self._values.get("extended_metric_labels")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def extra_args(self) -> typing.Optional[ExternalSecretsExtraArgs]:
        '''
        :schema: external-secrets#extraArgs
        '''
        result = self._values.get("extra_args")
        return typing.cast(typing.Optional[ExternalSecretsExtraArgs], result)

    @builtins.property
    def extra_containers(self) -> typing.Optional[typing.List[typing.Any]]:
        '''
        :schema: external-secrets#extraContainers
        '''
        result = self._values.get("extra_containers")
        return typing.cast(typing.Optional[typing.List[typing.Any]], result)

    @builtins.property
    def extra_env(self) -> typing.Optional[typing.List[typing.Any]]:
        '''
        :schema: external-secrets#extraEnv
        '''
        result = self._values.get("extra_env")
        return typing.cast(typing.Optional[typing.List[typing.Any]], result)

    @builtins.property
    def extra_objects(self) -> typing.Optional[typing.List[typing.Any]]:
        '''
        :schema: external-secrets#extraObjects
        '''
        result = self._values.get("extra_objects")
        return typing.cast(typing.Optional[typing.List[typing.Any]], result)

    @builtins.property
    def extra_volume_mounts(self) -> typing.Optional[typing.List[typing.Any]]:
        '''
        :schema: external-secrets#extraVolumeMounts
        '''
        result = self._values.get("extra_volume_mounts")
        return typing.cast(typing.Optional[typing.List[typing.Any]], result)

    @builtins.property
    def extra_volumes(self) -> typing.Optional[typing.List[typing.Any]]:
        '''
        :schema: external-secrets#extraVolumes
        '''
        result = self._values.get("extra_volumes")
        return typing.cast(typing.Optional[typing.List[typing.Any]], result)

    @builtins.property
    def fullname_override(self) -> typing.Optional[builtins.str]:
        '''
        :schema: external-secrets#fullnameOverride
        '''
        result = self._values.get("fullname_override")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def global_(self) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''
        :schema: external-secrets#global
        '''
        result = self._values.get("global_")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def grafana_dashboard(self) -> typing.Optional[ExternalSecretsGrafanaDashboard]:
        '''
        :schema: external-secrets#grafanaDashboard
        '''
        result = self._values.get("grafana_dashboard")
        return typing.cast(typing.Optional[ExternalSecretsGrafanaDashboard], result)

    @builtins.property
    def host_network(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: external-secrets#hostNetwork
        '''
        result = self._values.get("host_network")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def image(self) -> typing.Optional[ExternalSecretsImage]:
        '''
        :schema: external-secrets#image
        '''
        result = self._values.get("image")
        return typing.cast(typing.Optional[ExternalSecretsImage], result)

    @builtins.property
    def image_pull_secrets(self) -> typing.Optional[typing.List[typing.Any]]:
        '''
        :schema: external-secrets#imagePullSecrets
        '''
        result = self._values.get("image_pull_secrets")
        return typing.cast(typing.Optional[typing.List[typing.Any]], result)

    @builtins.property
    def install_cr_ds(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: external-secrets#installCRDs
        '''
        result = self._values.get("install_cr_ds")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def leader_elect(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: external-secrets#leaderElect
        '''
        result = self._values.get("leader_elect")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def log(self) -> typing.Optional[ExternalSecretsLog]:
        '''
        :schema: external-secrets#log
        '''
        result = self._values.get("log")
        return typing.cast(typing.Optional[ExternalSecretsLog], result)

    @builtins.property
    def metrics(self) -> typing.Optional[ExternalSecretsMetrics]:
        '''
        :schema: external-secrets#metrics
        '''
        result = self._values.get("metrics")
        return typing.cast(typing.Optional[ExternalSecretsMetrics], result)

    @builtins.property
    def name_override(self) -> typing.Optional[builtins.str]:
        '''
        :schema: external-secrets#nameOverride
        '''
        result = self._values.get("name_override")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def namespace_override(self) -> typing.Optional[builtins.str]:
        '''
        :schema: external-secrets#namespaceOverride
        '''
        result = self._values.get("namespace_override")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def node_selector(self) -> typing.Optional[ExternalSecretsNodeSelector]:
        '''
        :schema: external-secrets#nodeSelector
        '''
        result = self._values.get("node_selector")
        return typing.cast(typing.Optional[ExternalSecretsNodeSelector], result)

    @builtins.property
    def openshift_finalizers(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: external-secrets#openshiftFinalizers
        '''
        result = self._values.get("openshift_finalizers")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def pod_annotations(self) -> typing.Optional[ExternalSecretsPodAnnotations]:
        '''
        :schema: external-secrets#podAnnotations
        '''
        result = self._values.get("pod_annotations")
        return typing.cast(typing.Optional[ExternalSecretsPodAnnotations], result)

    @builtins.property
    def pod_disruption_budget(
        self,
    ) -> typing.Optional[ExternalSecretsPodDisruptionBudget]:
        '''
        :schema: external-secrets#podDisruptionBudget
        '''
        result = self._values.get("pod_disruption_budget")
        return typing.cast(typing.Optional[ExternalSecretsPodDisruptionBudget], result)

    @builtins.property
    def pod_labels(self) -> typing.Optional[ExternalSecretsPodLabels]:
        '''
        :schema: external-secrets#podLabels
        '''
        result = self._values.get("pod_labels")
        return typing.cast(typing.Optional[ExternalSecretsPodLabels], result)

    @builtins.property
    def pod_security_context(
        self,
    ) -> typing.Optional[ExternalSecretsPodSecurityContext]:
        '''
        :schema: external-secrets#podSecurityContext
        '''
        result = self._values.get("pod_security_context")
        return typing.cast(typing.Optional[ExternalSecretsPodSecurityContext], result)

    @builtins.property
    def pod_spec_extra(self) -> typing.Optional[ExternalSecretsPodSpecExtra]:
        '''
        :schema: external-secrets#podSpecExtra
        '''
        result = self._values.get("pod_spec_extra")
        return typing.cast(typing.Optional[ExternalSecretsPodSpecExtra], result)

    @builtins.property
    def priority_class_name(self) -> typing.Optional[builtins.str]:
        '''
        :schema: external-secrets#priorityClassName
        '''
        result = self._values.get("priority_class_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def process_cluster_external_secret(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: external-secrets#processClusterExternalSecret
        '''
        result = self._values.get("process_cluster_external_secret")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def process_cluster_push_secret(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: external-secrets#processClusterPushSecret
        '''
        result = self._values.get("process_cluster_push_secret")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def process_cluster_store(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: external-secrets#processClusterStore
        '''
        result = self._values.get("process_cluster_store")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def process_push_secret(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: external-secrets#processPushSecret
        '''
        result = self._values.get("process_push_secret")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def rbac(self) -> typing.Optional[ExternalSecretsRbac]:
        '''
        :schema: external-secrets#rbac
        '''
        result = self._values.get("rbac")
        return typing.cast(typing.Optional[ExternalSecretsRbac], result)

    @builtins.property
    def replica_count(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: external-secrets#replicaCount
        '''
        result = self._values.get("replica_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def resources(self) -> typing.Optional[ExternalSecretsResources]:
        '''
        :schema: external-secrets#resources
        '''
        result = self._values.get("resources")
        return typing.cast(typing.Optional[ExternalSecretsResources], result)

    @builtins.property
    def revision_history_limit(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: external-secrets#revisionHistoryLimit
        '''
        result = self._values.get("revision_history_limit")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def scoped_namespace(self) -> typing.Optional[builtins.str]:
        '''
        :schema: external-secrets#scopedNamespace
        '''
        result = self._values.get("scoped_namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def scoped_rbac(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: external-secrets#scopedRBAC
        '''
        result = self._values.get("scoped_rbac")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def security_context(self) -> typing.Optional[ExternalSecretsSecurityContext]:
        '''
        :schema: external-secrets#securityContext
        '''
        result = self._values.get("security_context")
        return typing.cast(typing.Optional[ExternalSecretsSecurityContext], result)

    @builtins.property
    def service(self) -> typing.Optional[ExternalSecretsService]:
        '''
        :schema: external-secrets#service
        '''
        result = self._values.get("service")
        return typing.cast(typing.Optional[ExternalSecretsService], result)

    @builtins.property
    def service_account(self) -> typing.Optional[ExternalSecretsServiceAccount]:
        '''
        :schema: external-secrets#serviceAccount
        '''
        result = self._values.get("service_account")
        return typing.cast(typing.Optional[ExternalSecretsServiceAccount], result)

    @builtins.property
    def service_monitor(self) -> typing.Optional[ExternalSecretsServiceMonitor]:
        '''
        :schema: external-secrets#serviceMonitor
        '''
        result = self._values.get("service_monitor")
        return typing.cast(typing.Optional[ExternalSecretsServiceMonitor], result)

    @builtins.property
    def tolerations(self) -> typing.Optional[typing.List[typing.Any]]:
        '''
        :schema: external-secrets#tolerations
        '''
        result = self._values.get("tolerations")
        return typing.cast(typing.Optional[typing.List[typing.Any]], result)

    @builtins.property
    def topology_spread_constraints(self) -> typing.Optional[typing.List[typing.Any]]:
        '''
        :schema: external-secrets#topologySpreadConstraints
        '''
        result = self._values.get("topology_spread_constraints")
        return typing.cast(typing.Optional[typing.List[typing.Any]], result)

    @builtins.property
    def webhook(self) -> typing.Optional[ExternalSecretsWebhook]:
        '''
        :schema: external-secrets#webhook
        '''
        result = self._values.get("webhook")
        return typing.cast(typing.Optional[ExternalSecretsWebhook], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ExternalsecretsValues(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "ExternalSecretsAffinity",
    "ExternalSecretsCertController",
    "ExternalSecretsCertControllerAffinity",
    "ExternalSecretsCertControllerDeploymentAnnotations",
    "ExternalSecretsCertControllerExtraArgs",
    "ExternalSecretsCertControllerImage",
    "ExternalSecretsCertControllerLog",
    "ExternalSecretsCertControllerMetrics",
    "ExternalSecretsCertControllerMetricsListen",
    "ExternalSecretsCertControllerMetricsService",
    "ExternalSecretsCertControllerMetricsServiceAnnotations",
    "ExternalSecretsCertControllerNodeSelector",
    "ExternalSecretsCertControllerPodAnnotations",
    "ExternalSecretsCertControllerPodDisruptionBudget",
    "ExternalSecretsCertControllerPodLabels",
    "ExternalSecretsCertControllerPodSecurityContext",
    "ExternalSecretsCertControllerRbac",
    "ExternalSecretsCertControllerReadinessProbe",
    "ExternalSecretsCertControllerResources",
    "ExternalSecretsCertControllerSecurityContext",
    "ExternalSecretsCertControllerSecurityContextCapabilities",
    "ExternalSecretsCertControllerSecurityContextSeccompProfile",
    "ExternalSecretsCertControllerServiceAccount",
    "ExternalSecretsCertControllerServiceAccountAnnotations",
    "ExternalSecretsCertControllerServiceAccountExtraLabels",
    "ExternalSecretsCommonLabels",
    "ExternalSecretsCrds",
    "ExternalSecretsCrdsAnnotations",
    "ExternalSecretsCrdsConversion",
    "ExternalSecretsDeploymentAnnotations",
    "ExternalSecretsDnsConfig",
    "ExternalSecretsExtraArgs",
    "ExternalSecretsGrafanaDashboard",
    "ExternalSecretsGrafanaDashboardAnnotations",
    "ExternalSecretsImage",
    "ExternalSecretsLog",
    "ExternalSecretsMetrics",
    "ExternalSecretsMetricsListen",
    "ExternalSecretsMetricsService",
    "ExternalSecretsMetricsServiceAnnotations",
    "ExternalSecretsNodeSelector",
    "ExternalSecretsPodAnnotations",
    "ExternalSecretsPodDisruptionBudget",
    "ExternalSecretsPodLabels",
    "ExternalSecretsPodSecurityContext",
    "ExternalSecretsPodSpecExtra",
    "ExternalSecretsRbac",
    "ExternalSecretsRbacServicebindings",
    "ExternalSecretsResources",
    "ExternalSecretsSecurityContext",
    "ExternalSecretsSecurityContextCapabilities",
    "ExternalSecretsSecurityContextSeccompProfile",
    "ExternalSecretsService",
    "ExternalSecretsServiceAccount",
    "ExternalSecretsServiceAccountAnnotations",
    "ExternalSecretsServiceAccountExtraLabels",
    "ExternalSecretsServiceMonitor",
    "ExternalSecretsServiceMonitorAdditionalLabels",
    "ExternalSecretsWebhook",
    "ExternalSecretsWebhookAffinity",
    "ExternalSecretsWebhookAnnotations",
    "ExternalSecretsWebhookCertManager",
    "ExternalSecretsWebhookCertManagerCert",
    "ExternalSecretsWebhookCertManagerCertAnnotations",
    "ExternalSecretsWebhookCertManagerCertIssuerRef",
    "ExternalSecretsWebhookDeploymentAnnotations",
    "ExternalSecretsWebhookExtraArgs",
    "ExternalSecretsWebhookImage",
    "ExternalSecretsWebhookLog",
    "ExternalSecretsWebhookMetrics",
    "ExternalSecretsWebhookMetricsListen",
    "ExternalSecretsWebhookMetricsService",
    "ExternalSecretsWebhookMetricsServiceAnnotations",
    "ExternalSecretsWebhookNodeSelector",
    "ExternalSecretsWebhookPodAnnotations",
    "ExternalSecretsWebhookPodDisruptionBudget",
    "ExternalSecretsWebhookPodLabels",
    "ExternalSecretsWebhookPodSecurityContext",
    "ExternalSecretsWebhookRbac",
    "ExternalSecretsWebhookReadinessProbe",
    "ExternalSecretsWebhookResources",
    "ExternalSecretsWebhookSecretAnnotations",
    "ExternalSecretsWebhookSecurityContext",
    "ExternalSecretsWebhookSecurityContextCapabilities",
    "ExternalSecretsWebhookSecurityContextSeccompProfile",
    "ExternalSecretsWebhookService",
    "ExternalSecretsWebhookServiceAccount",
    "ExternalSecretsWebhookServiceAccountAnnotations",
    "ExternalSecretsWebhookServiceAccountExtraLabels",
    "ExternalSecretsWebhookServiceAnnotations",
    "ExternalSecretsWebhookServiceLabels",
    "Externalsecrets",
    "ExternalsecretsProps",
    "ExternalsecretsValues",
]

publication.publish()

def _typecheckingstub__bcfdeb8435e2b021e54a939e07980eeadb785975e74e8e6fce1e6182f6f995fa(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__687fa9c52b549d2ea7722211c58720c96e30f3932231ff2a88ca777a9bc82ca1(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    affinity: typing.Optional[typing.Union[ExternalSecretsCertControllerAffinity, typing.Dict[builtins.str, typing.Any]]] = None,
    create: typing.Optional[builtins.bool] = None,
    deployment_annotations: typing.Optional[typing.Union[ExternalSecretsCertControllerDeploymentAnnotations, typing.Dict[builtins.str, typing.Any]]] = None,
    extra_args: typing.Optional[typing.Union[ExternalSecretsCertControllerExtraArgs, typing.Dict[builtins.str, typing.Any]]] = None,
    extra_env: typing.Optional[typing.Sequence[typing.Any]] = None,
    extra_volume_mounts: typing.Optional[typing.Sequence[typing.Any]] = None,
    extra_volumes: typing.Optional[typing.Sequence[typing.Any]] = None,
    fullname_override: typing.Optional[builtins.str] = None,
    host_network: typing.Optional[builtins.bool] = None,
    image: typing.Optional[typing.Union[ExternalSecretsCertControllerImage, typing.Dict[builtins.str, typing.Any]]] = None,
    image_pull_secrets: typing.Optional[typing.Sequence[typing.Any]] = None,
    log: typing.Optional[typing.Union[ExternalSecretsCertControllerLog, typing.Dict[builtins.str, typing.Any]]] = None,
    metrics: typing.Optional[typing.Union[ExternalSecretsCertControllerMetrics, typing.Dict[builtins.str, typing.Any]]] = None,
    name_override: typing.Optional[builtins.str] = None,
    node_selector: typing.Optional[typing.Union[ExternalSecretsCertControllerNodeSelector, typing.Dict[builtins.str, typing.Any]]] = None,
    pod_annotations: typing.Optional[typing.Union[ExternalSecretsCertControllerPodAnnotations, typing.Dict[builtins.str, typing.Any]]] = None,
    pod_disruption_budget: typing.Optional[typing.Union[ExternalSecretsCertControllerPodDisruptionBudget, typing.Dict[builtins.str, typing.Any]]] = None,
    pod_labels: typing.Optional[typing.Union[ExternalSecretsCertControllerPodLabels, typing.Dict[builtins.str, typing.Any]]] = None,
    pod_security_context: typing.Optional[typing.Union[ExternalSecretsCertControllerPodSecurityContext, typing.Dict[builtins.str, typing.Any]]] = None,
    priority_class_name: typing.Optional[builtins.str] = None,
    rbac: typing.Optional[typing.Union[ExternalSecretsCertControllerRbac, typing.Dict[builtins.str, typing.Any]]] = None,
    readiness_probe: typing.Optional[typing.Union[ExternalSecretsCertControllerReadinessProbe, typing.Dict[builtins.str, typing.Any]]] = None,
    replica_count: typing.Optional[jsii.Number] = None,
    requeue_interval: typing.Optional[builtins.str] = None,
    resources: typing.Optional[typing.Union[ExternalSecretsCertControllerResources, typing.Dict[builtins.str, typing.Any]]] = None,
    revision_history_limit: typing.Optional[jsii.Number] = None,
    security_context: typing.Optional[typing.Union[ExternalSecretsCertControllerSecurityContext, typing.Dict[builtins.str, typing.Any]]] = None,
    service_account: typing.Optional[typing.Union[ExternalSecretsCertControllerServiceAccount, typing.Dict[builtins.str, typing.Any]]] = None,
    tolerations: typing.Optional[typing.Sequence[typing.Any]] = None,
    topology_spread_constraints: typing.Optional[typing.Sequence[typing.Any]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__92aec26eca28fe021d3520067a9f493e0c4718c13ca457f03a69b7fb2543aa81(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ca5a465d793b784a4bff4a4e74edc07ec32a1b1a07a17b00534a5f8f9728041a(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0f394daf0ace638c0c7721cdb76ab265c1e7b471cafebe66913c662bd596a2cf(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__14ba0d28445356231ef5bd71adea29d3f103d881919bf62e49ce3a3a0a4054de(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    flavour: typing.Optional[builtins.str] = None,
    pull_policy: typing.Optional[builtins.str] = None,
    repository: typing.Optional[builtins.str] = None,
    tag: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__82dc057cfbf2674634b0c80ba1efa2057f00af186bb2ffe966e1dd0bb46f2748(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    level: typing.Optional[builtins.str] = None,
    time_encoding: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d68b0ea54d72ae51b7032ecbf4457e20d383493383f5a6b46bf585b6d59ba3d(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    listen: typing.Optional[typing.Union[ExternalSecretsCertControllerMetricsListen, typing.Dict[builtins.str, typing.Any]]] = None,
    service: typing.Optional[typing.Union[ExternalSecretsCertControllerMetricsService, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__051c18e4a965e7dde24a4186ea68b3f4a73c5058fe2e3c5f5b35610ec3d026c7(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    port: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ea17ecb6401ce6b3f6752afb09a4c75617bacfea8b082dc20a556facfe41a72f(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    annotations: typing.Optional[typing.Union[ExternalSecretsCertControllerMetricsServiceAnnotations, typing.Dict[builtins.str, typing.Any]]] = None,
    enabled: typing.Optional[builtins.bool] = None,
    port: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0bdfcc298f1c6aeaccfd729329be0ffd7e2ba4e24ffa1ab692075b83f1d4cf45(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2b8697752ad3d83476ff076921e0af7e0af04eb916f94c14996baee6e9a110d5(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__205d9ec70d860e25aaa8da4626eb9732de613079701ade6ab1284fcb1a8ce4aa(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9f710a6a96baa670c0031b764fd856afbbab8cac398923321aa7e269fe77daab(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    enabled: typing.Optional[builtins.bool] = None,
    min_available: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7d77078db44cc4baf4e164a3fa045686091c37c6eff54146fb9988d78b37009a(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6a2e36ddf3525a42c97be28e7e9cad07f7d487b2063c757d34a7e14e9beed540(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    enabled: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a51024eeffffbada0935443bb68ec72a709471513b3845628f93d7a23539f84(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    create: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__398dc3a22a319435302aaa283fdbde20b169b285abd7506b0c41744c31adc652(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    address: typing.Optional[builtins.str] = None,
    port: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__192f9fc09348d1fd178fb6819f9f949092c082e71c08c7a02c90ee0fd5c50809(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9999c12c8f58865c079ecdd1fa8d31ad09f6cac13a1e7ae44c1b819d4c9b0cfe(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    allow_privilege_escalation: typing.Optional[builtins.bool] = None,
    capabilities: typing.Optional[typing.Union[ExternalSecretsCertControllerSecurityContextCapabilities, typing.Dict[builtins.str, typing.Any]]] = None,
    enabled: typing.Optional[builtins.bool] = None,
    read_only_root_filesystem: typing.Optional[builtins.bool] = None,
    run_as_non_root: typing.Optional[builtins.bool] = None,
    run_as_user: typing.Optional[jsii.Number] = None,
    seccomp_profile: typing.Optional[typing.Union[ExternalSecretsCertControllerSecurityContextSeccompProfile, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a5f240720f28e8a202f349a14d84a56866f833b9403fb7e6220e1b9d12ca2c5e(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    drop: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e089a636a080275eb5e1ed4e26a8ce6ccc55b08aa9753cf2261882ab20558a1(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b4972b31afd41cffd9741a674f157bbe97f49e359624a2bcb0eae302ea03c29c(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    annotations: typing.Optional[typing.Union[ExternalSecretsCertControllerServiceAccountAnnotations, typing.Dict[builtins.str, typing.Any]]] = None,
    automount: typing.Optional[builtins.bool] = None,
    create: typing.Optional[builtins.bool] = None,
    extra_labels: typing.Optional[typing.Union[ExternalSecretsCertControllerServiceAccountExtraLabels, typing.Dict[builtins.str, typing.Any]]] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__575e01b5f959f58c95296eb3aff49b63316732f733f0172ab2d0a2a2f86831ad(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4ab5ab6fd1e0fe86e0d53eec8b2f5a675da09244a356fae515bdc37f99d5f8ec(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dca8f6b7ab4c4518b1b227594f33732ca006a71897da4776c51dc5c5449c9a7a(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5a26a6d4526d16e791fd27b21085a63f44608ba2c680efefd407a86721ec0802(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    annotations: typing.Optional[typing.Union[ExternalSecretsCrdsAnnotations, typing.Dict[builtins.str, typing.Any]]] = None,
    conversion: typing.Optional[typing.Union[ExternalSecretsCrdsConversion, typing.Dict[builtins.str, typing.Any]]] = None,
    create_cluster_external_secret: typing.Optional[builtins.bool] = None,
    create_cluster_generator: typing.Optional[builtins.bool] = None,
    create_cluster_push_secret: typing.Optional[builtins.bool] = None,
    create_cluster_secret_store: typing.Optional[builtins.bool] = None,
    create_push_secret: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b0d9737373fddb1d64d7436c03a41d3d44bd36f27fb9186150771a05fc89613f(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4bcc0937b6df670047d2bda5e145435f0257ee29f88717833f9832df002e3352(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    enabled: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c2a4cb5f88d701e40538308b09ccee6d8fa71c36f90bba265b2ba48614768784(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__20701acb3a2f0fe4fcf6d75acfe310c5c35ed96a6110fd13aa3d3e5d7b48bdaa(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b797807a10ed8a58934fc83fa400d991e7b3f7f4148bb9716e8509a56dc6ed0d(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a7b46c0d66b8ca221762ec7b29a4d8ffa5bc08ba901d85bb104ca052534afb83(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    annotations: typing.Optional[typing.Union[ExternalSecretsGrafanaDashboardAnnotations, typing.Dict[builtins.str, typing.Any]]] = None,
    enabled: typing.Optional[builtins.bool] = None,
    sidecar_label: typing.Optional[builtins.str] = None,
    sidecar_label_value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e09c283fc52ae2b9b15745432386941fa9244522505c84efd5d21e445d45a9fd(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ea161ef1bed9451f11a5a337b1424fbb62c4f0fd634410c915b70ecc55989424(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    flavour: typing.Optional[builtins.str] = None,
    pull_policy: typing.Optional[builtins.str] = None,
    repository: typing.Optional[builtins.str] = None,
    tag: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4ab228c4ae140ddde5462f48ff62422199ea281422684df15c2d2eab4f0a21bf(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    level: typing.Optional[builtins.str] = None,
    time_encoding: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e21294305bff98bfcd2bd0bcee45154f480f43218712e3e8683b85567cf16b96(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    listen: typing.Optional[typing.Union[ExternalSecretsMetricsListen, typing.Dict[builtins.str, typing.Any]]] = None,
    service: typing.Optional[typing.Union[ExternalSecretsMetricsService, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__65bf3137db5396f1735b3ccee527b21147ce0c31b627ac26fae0e3e3827bc8b9(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    port: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7d86a139402a143ddb6374d70de48243e7a729b1d2a69d75cc6d3b9f8281cdfb(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    annotations: typing.Optional[typing.Union[ExternalSecretsMetricsServiceAnnotations, typing.Dict[builtins.str, typing.Any]]] = None,
    enabled: typing.Optional[builtins.bool] = None,
    port: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ab645bb0bc8839ce7e5adfc45b3084c0da5b39dc3ba68c51bc5608ac79dbfa44(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bbf479cb99c2e9319a339fdce977c7f9fa1833909f58397258532e7fbf83121c(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__50b7a00e061ae6d380a98719ffcb8ee1fa52482db8bc79fae953628f2a2b11a6(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f52d2bde3e75aff7b2b961a97dffdc8a38ec0706c41650ef7f5c98ed23574cc6(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    enabled: typing.Optional[builtins.bool] = None,
    min_available: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a9def16ae49f564838a775bb2346070b162811690200f43faeb790c105af1568(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__707d879de51daea67b7728241a4a0704769a1936ace9c3c4358768f91a94e585(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    enabled: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__149bb64fea876c68dfd3722c41e5a78477357250c93ff827058212b555c2a4dc(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7d9b2ef0e1734ddc974aeb44b3a6b46864befcfb32833a89d80bf47f3791074a(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    aggregate_to_edit: typing.Optional[builtins.bool] = None,
    aggregate_to_view: typing.Optional[builtins.bool] = None,
    create: typing.Optional[builtins.bool] = None,
    servicebindings: typing.Optional[typing.Union[ExternalSecretsRbacServicebindings, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3e5f50624e6803778810d6f884262051daff1bf9337c98e22d6c376d2fd0dd49(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    create: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6368948474ab3d8e9d6fa5e7aef356e4b64a22007e23519ba21b152f6f439d3b(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7b1981a823a7bc3e612f61be4b7ab79ef1a01468d28e4c003268d56b906a0f67(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    allow_privilege_escalation: typing.Optional[builtins.bool] = None,
    capabilities: typing.Optional[typing.Union[ExternalSecretsSecurityContextCapabilities, typing.Dict[builtins.str, typing.Any]]] = None,
    enabled: typing.Optional[builtins.bool] = None,
    read_only_root_filesystem: typing.Optional[builtins.bool] = None,
    run_as_non_root: typing.Optional[builtins.bool] = None,
    run_as_user: typing.Optional[jsii.Number] = None,
    seccomp_profile: typing.Optional[typing.Union[ExternalSecretsSecurityContextSeccompProfile, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__451d08701ab9cf031ac5233dbb3f790c6271ba377752517c96bc28439af3c8a4(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    drop: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0619ec5aded402e56bb6ed22f96683f1782db58dc8c1add12d1120372ae103f8(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8248d48ea0ac184028c7d5cb6cf9a18a9dd79454cf2bff151e44c1d58ef360eb(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    ip_families: typing.Optional[typing.Sequence[typing.Any]] = None,
    ip_family_policy: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__411b410172ce4bf5ecc4fa0049d970f979ea37b57f146fe2c2ce1537f4108c20(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    annotations: typing.Optional[typing.Union[ExternalSecretsServiceAccountAnnotations, typing.Dict[builtins.str, typing.Any]]] = None,
    automount: typing.Optional[builtins.bool] = None,
    create: typing.Optional[builtins.bool] = None,
    extra_labels: typing.Optional[typing.Union[ExternalSecretsServiceAccountExtraLabels, typing.Dict[builtins.str, typing.Any]]] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__646b8dbb27cbb9fd60d736f4001eece582a9561b1ac29fe4f04674ca32ce18fe(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__64fc74da162d9ec51ecc2f7069d506bb9512a1b72246850ccd57ad06617a99c3(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__25751ef29bc9239a97465557615fada6ca8ec60914ca7553f3dd570520278fcb(
    *,
    additional_labels: typing.Optional[typing.Union[ExternalSecretsServiceMonitorAdditionalLabels, typing.Dict[builtins.str, typing.Any]]] = None,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    enabled: typing.Optional[builtins.bool] = None,
    honor_labels: typing.Optional[builtins.bool] = None,
    interval: typing.Optional[builtins.str] = None,
    metric_relabelings: typing.Optional[typing.Sequence[typing.Any]] = None,
    namespace: typing.Optional[builtins.str] = None,
    relabelings: typing.Optional[typing.Sequence[typing.Any]] = None,
    scrape_timeout: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ffbe12387c140c1117fd65bccb0ecd74555f0d8c1a69616c14a101fdc513d382(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1bb990e5f92a626f64522d860d089a7ecfadd7ef797be3108a230f5875a33fa9(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    affinity: typing.Optional[typing.Union[ExternalSecretsWebhookAffinity, typing.Dict[builtins.str, typing.Any]]] = None,
    annotations: typing.Optional[typing.Union[ExternalSecretsWebhookAnnotations, typing.Dict[builtins.str, typing.Any]]] = None,
    cert_check_interval: typing.Optional[builtins.str] = None,
    cert_dir: typing.Optional[builtins.str] = None,
    cert_manager: typing.Optional[typing.Union[ExternalSecretsWebhookCertManager, typing.Dict[builtins.str, typing.Any]]] = None,
    create: typing.Optional[builtins.bool] = None,
    deployment_annotations: typing.Optional[typing.Union[ExternalSecretsWebhookDeploymentAnnotations, typing.Dict[builtins.str, typing.Any]]] = None,
    extra_args: typing.Optional[typing.Union[ExternalSecretsWebhookExtraArgs, typing.Dict[builtins.str, typing.Any]]] = None,
    extra_env: typing.Optional[typing.Sequence[typing.Any]] = None,
    extra_volume_mounts: typing.Optional[typing.Sequence[typing.Any]] = None,
    extra_volumes: typing.Optional[typing.Sequence[typing.Any]] = None,
    failure_policy: typing.Optional[builtins.str] = None,
    fullname_override: typing.Optional[builtins.str] = None,
    host_network: typing.Optional[builtins.bool] = None,
    image: typing.Optional[typing.Union[ExternalSecretsWebhookImage, typing.Dict[builtins.str, typing.Any]]] = None,
    image_pull_secrets: typing.Optional[typing.Sequence[typing.Any]] = None,
    log: typing.Optional[typing.Union[ExternalSecretsWebhookLog, typing.Dict[builtins.str, typing.Any]]] = None,
    lookahead_interval: typing.Optional[builtins.str] = None,
    metrics: typing.Optional[typing.Union[ExternalSecretsWebhookMetrics, typing.Dict[builtins.str, typing.Any]]] = None,
    name_override: typing.Optional[builtins.str] = None,
    node_selector: typing.Optional[typing.Union[ExternalSecretsWebhookNodeSelector, typing.Dict[builtins.str, typing.Any]]] = None,
    pod_annotations: typing.Optional[typing.Union[ExternalSecretsWebhookPodAnnotations, typing.Dict[builtins.str, typing.Any]]] = None,
    pod_disruption_budget: typing.Optional[typing.Union[ExternalSecretsWebhookPodDisruptionBudget, typing.Dict[builtins.str, typing.Any]]] = None,
    pod_labels: typing.Optional[typing.Union[ExternalSecretsWebhookPodLabels, typing.Dict[builtins.str, typing.Any]]] = None,
    pod_security_context: typing.Optional[typing.Union[ExternalSecretsWebhookPodSecurityContext, typing.Dict[builtins.str, typing.Any]]] = None,
    port: typing.Optional[jsii.Number] = None,
    priority_class_name: typing.Optional[builtins.str] = None,
    rbac: typing.Optional[typing.Union[ExternalSecretsWebhookRbac, typing.Dict[builtins.str, typing.Any]]] = None,
    readiness_probe: typing.Optional[typing.Union[ExternalSecretsWebhookReadinessProbe, typing.Dict[builtins.str, typing.Any]]] = None,
    replica_count: typing.Optional[jsii.Number] = None,
    resources: typing.Optional[typing.Union[ExternalSecretsWebhookResources, typing.Dict[builtins.str, typing.Any]]] = None,
    revision_history_limit: typing.Optional[jsii.Number] = None,
    secret_annotations: typing.Optional[typing.Union[ExternalSecretsWebhookSecretAnnotations, typing.Dict[builtins.str, typing.Any]]] = None,
    security_context: typing.Optional[typing.Union[ExternalSecretsWebhookSecurityContext, typing.Dict[builtins.str, typing.Any]]] = None,
    service: typing.Optional[typing.Union[ExternalSecretsWebhookService, typing.Dict[builtins.str, typing.Any]]] = None,
    service_account: typing.Optional[typing.Union[ExternalSecretsWebhookServiceAccount, typing.Dict[builtins.str, typing.Any]]] = None,
    tolerations: typing.Optional[typing.Sequence[typing.Any]] = None,
    topology_spread_constraints: typing.Optional[typing.Sequence[typing.Any]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__89a8a0e74170554046a3491f02d39c02763ddaf56a77009d238a1cc6d569894d(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e1b432a637e0b87983a9b7143a32813a5a59b090a01b96b6b6a17dff1193b9f5(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b23a50719f15d3b10dd519b3c305ec876c637234f5accb798f206fedd2234c9b(
    *,
    add_injector_annotations: typing.Optional[builtins.bool] = None,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    cert: typing.Optional[typing.Union[ExternalSecretsWebhookCertManagerCert, typing.Dict[builtins.str, typing.Any]]] = None,
    enabled: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__84731106ab6916ee25148ef175097b58c44701d23736c35914488a18c85349c0(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    annotations: typing.Optional[typing.Union[ExternalSecretsWebhookCertManagerCertAnnotations, typing.Dict[builtins.str, typing.Any]]] = None,
    create: typing.Optional[builtins.bool] = None,
    duration: typing.Optional[builtins.str] = None,
    issuer_ref: typing.Optional[typing.Union[ExternalSecretsWebhookCertManagerCertIssuerRef, typing.Dict[builtins.str, typing.Any]]] = None,
    renew_before: typing.Optional[builtins.str] = None,
    revision_history_limit: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__91c91d29f6241f929ee858d632b73b69384b6388ab2440dc265daa5355a3607c(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__42a9c6ed2409ebc4d5c6baec37aae4d95e32dd193ea25c8b59cdc83ff28b3e21(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    group: typing.Optional[builtins.str] = None,
    kind: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb90c63590ed3a886b0132d8291e2b226dc16ad844384886869bfc5b35fb2520(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7ab3462bbccb589616d71ad3f098cb5b0ce648bda4411444b52f9d489e04e826(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__817d529ad17cc45cdcd5db526227d26f8533693fc0b488bf0996691c40a5db53(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    flavour: typing.Optional[builtins.str] = None,
    pull_policy: typing.Optional[builtins.str] = None,
    repository: typing.Optional[builtins.str] = None,
    tag: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ca360874d9a5748675fd49dbefc43cc62dc388d75469000a88f6fd9783e5091d(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    level: typing.Optional[builtins.str] = None,
    time_encoding: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c87bf1ef9d48233299181b85a227faefe06a06d87b6461b564db477ec0f600ad(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    listen: typing.Optional[typing.Union[ExternalSecretsWebhookMetricsListen, typing.Dict[builtins.str, typing.Any]]] = None,
    service: typing.Optional[typing.Union[ExternalSecretsWebhookMetricsService, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f2af75690bcd1b6bcbb32d9f377dd7706354cb4e81baefc6df99e33beb44befa(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    port: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a459169ca3b6afc64711e776b0868ec99b52454bf1bd4bcb67ac8d592e7d512(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    annotations: typing.Optional[typing.Union[ExternalSecretsWebhookMetricsServiceAnnotations, typing.Dict[builtins.str, typing.Any]]] = None,
    enabled: typing.Optional[builtins.bool] = None,
    port: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c72939b7bc6a1cd33a0af8e78ed62aa1a6438231c2bc018778b6536c06e6bbb5(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a859107777f8af73f22ba880d0af6dc01b04d9655f8b644838b3030f9799f16b(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__90eee64ea4226ab9879b49849b4bc2df2fb361b4d6d2f567c16216f789373024(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a8db14aacfaffa28a264c6b1b65ae07d84c91245ccae2bc414d9ac018d238554(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    enabled: typing.Optional[builtins.bool] = None,
    min_available: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c7fd3147adddbf755d5d0f78b1a0711609a685d75fac7f77ef1b92dab55edc93(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a9015b5e8333af95af11f6f356d362cc2a8ff34cbcde4a07c5a109db2afbca4c(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    enabled: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__119027cf1d7d295ad08574f0c1db01f2dee471fc3c200841508fca6417dbece5(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    create: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b5802c581d243e1cc0418a08ce9a820bbb77dacf55bcc639d64c2b314ea3b884(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    address: typing.Optional[builtins.str] = None,
    port: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__211ae8e72fc9a783ee54153c4c66763729f6316304e502cd0c199f194d26fb6f(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d4fa43b61bad8fa8dcffb1f468083127468e18d1a8e34c0806c87e3c8692f13d(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d38be18bdead4131c032dacbf1c7a9e211342dd935475ab5c5982ceb61c44969(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    allow_privilege_escalation: typing.Optional[builtins.bool] = None,
    capabilities: typing.Optional[typing.Union[ExternalSecretsWebhookSecurityContextCapabilities, typing.Dict[builtins.str, typing.Any]]] = None,
    enabled: typing.Optional[builtins.bool] = None,
    read_only_root_filesystem: typing.Optional[builtins.bool] = None,
    run_as_non_root: typing.Optional[builtins.bool] = None,
    run_as_user: typing.Optional[jsii.Number] = None,
    seccomp_profile: typing.Optional[typing.Union[ExternalSecretsWebhookSecurityContextSeccompProfile, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3061c9999e96589e086a163de078b8aed89c8dad2dee841656a4943d30937127(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    drop: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b93f794d1890a98f3519197b33e3accd93ab80f24c7af737b3381e6d865e22d6(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b89b3e4e255c9137c31be38fcf5cfd6e04abd22708d2d11f2f89d332d40dd134(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    annotations: typing.Optional[typing.Union[ExternalSecretsWebhookServiceAnnotations, typing.Dict[builtins.str, typing.Any]]] = None,
    enabled: typing.Optional[builtins.bool] = None,
    labels: typing.Optional[typing.Union[ExternalSecretsWebhookServiceLabels, typing.Dict[builtins.str, typing.Any]]] = None,
    load_balancer_ip: typing.Optional[builtins.str] = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fbda51c0b17f7330a35dc25c1fac85c55911a5f3f47a0f4572400c0c269b53db(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    annotations: typing.Optional[typing.Union[ExternalSecretsWebhookServiceAccountAnnotations, typing.Dict[builtins.str, typing.Any]]] = None,
    automount: typing.Optional[builtins.bool] = None,
    create: typing.Optional[builtins.bool] = None,
    extra_labels: typing.Optional[typing.Union[ExternalSecretsWebhookServiceAccountExtraLabels, typing.Dict[builtins.str, typing.Any]]] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1ffd445a6907cef4e4006e70b6522c61355c8653f32779cb617b481c7e798890(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c948ee0ae534ea6581d47534a3c8ddca66680ea2e02f906a8c97b8b232e3a1a5(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__94540b5998d1ec75cafe6b911c8bd5eeb762804a2d4a16fc5178d63a5be024a9(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5a71716dfdcbe8f3ef28bb246c973edcb3e38cd31e4e829acd20cbaaedb337a5(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6040049eae66ad607f76227ecce16bccd5fb16452bf1e97da81d7c3b0a5221df(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    helm_executable: typing.Optional[builtins.str] = None,
    helm_flags: typing.Optional[typing.Sequence[builtins.str]] = None,
    namespace: typing.Optional[builtins.str] = None,
    release_name: typing.Optional[builtins.str] = None,
    values: typing.Optional[typing.Union[ExternalsecretsValues, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8ab95e6d37f6032d4a30183c33df1e0cc7a3064fe3ea5582a0a7c6eff645b525(
    *,
    helm_executable: typing.Optional[builtins.str] = None,
    helm_flags: typing.Optional[typing.Sequence[builtins.str]] = None,
    namespace: typing.Optional[builtins.str] = None,
    release_name: typing.Optional[builtins.str] = None,
    values: typing.Optional[typing.Union[ExternalsecretsValues, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c534e8f71d825c8aa85c89da03ff575eafee9ff0758222d9ebc53ffbdc02b978(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    affinity: typing.Optional[typing.Union[ExternalSecretsAffinity, typing.Dict[builtins.str, typing.Any]]] = None,
    bitwarden_sdk_server: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    cert_controller: typing.Optional[typing.Union[ExternalSecretsCertController, typing.Dict[builtins.str, typing.Any]]] = None,
    common_labels: typing.Optional[typing.Union[ExternalSecretsCommonLabels, typing.Dict[builtins.str, typing.Any]]] = None,
    concurrent: typing.Optional[jsii.Number] = None,
    controller_class: typing.Optional[builtins.str] = None,
    crds: typing.Optional[typing.Union[ExternalSecretsCrds, typing.Dict[builtins.str, typing.Any]]] = None,
    create_operator: typing.Optional[builtins.bool] = None,
    deployment_annotations: typing.Optional[typing.Union[ExternalSecretsDeploymentAnnotations, typing.Dict[builtins.str, typing.Any]]] = None,
    dns_config: typing.Optional[typing.Union[ExternalSecretsDnsConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    dns_policy: typing.Optional[builtins.str] = None,
    extended_metric_labels: typing.Optional[builtins.bool] = None,
    extra_args: typing.Optional[typing.Union[ExternalSecretsExtraArgs, typing.Dict[builtins.str, typing.Any]]] = None,
    extra_containers: typing.Optional[typing.Sequence[typing.Any]] = None,
    extra_env: typing.Optional[typing.Sequence[typing.Any]] = None,
    extra_objects: typing.Optional[typing.Sequence[typing.Any]] = None,
    extra_volume_mounts: typing.Optional[typing.Sequence[typing.Any]] = None,
    extra_volumes: typing.Optional[typing.Sequence[typing.Any]] = None,
    fullname_override: typing.Optional[builtins.str] = None,
    global_: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    grafana_dashboard: typing.Optional[typing.Union[ExternalSecretsGrafanaDashboard, typing.Dict[builtins.str, typing.Any]]] = None,
    host_network: typing.Optional[builtins.bool] = None,
    image: typing.Optional[typing.Union[ExternalSecretsImage, typing.Dict[builtins.str, typing.Any]]] = None,
    image_pull_secrets: typing.Optional[typing.Sequence[typing.Any]] = None,
    install_cr_ds: typing.Optional[builtins.bool] = None,
    leader_elect: typing.Optional[builtins.bool] = None,
    log: typing.Optional[typing.Union[ExternalSecretsLog, typing.Dict[builtins.str, typing.Any]]] = None,
    metrics: typing.Optional[typing.Union[ExternalSecretsMetrics, typing.Dict[builtins.str, typing.Any]]] = None,
    name_override: typing.Optional[builtins.str] = None,
    namespace_override: typing.Optional[builtins.str] = None,
    node_selector: typing.Optional[typing.Union[ExternalSecretsNodeSelector, typing.Dict[builtins.str, typing.Any]]] = None,
    openshift_finalizers: typing.Optional[builtins.bool] = None,
    pod_annotations: typing.Optional[typing.Union[ExternalSecretsPodAnnotations, typing.Dict[builtins.str, typing.Any]]] = None,
    pod_disruption_budget: typing.Optional[typing.Union[ExternalSecretsPodDisruptionBudget, typing.Dict[builtins.str, typing.Any]]] = None,
    pod_labels: typing.Optional[typing.Union[ExternalSecretsPodLabels, typing.Dict[builtins.str, typing.Any]]] = None,
    pod_security_context: typing.Optional[typing.Union[ExternalSecretsPodSecurityContext, typing.Dict[builtins.str, typing.Any]]] = None,
    pod_spec_extra: typing.Optional[typing.Union[ExternalSecretsPodSpecExtra, typing.Dict[builtins.str, typing.Any]]] = None,
    priority_class_name: typing.Optional[builtins.str] = None,
    process_cluster_external_secret: typing.Optional[builtins.bool] = None,
    process_cluster_push_secret: typing.Optional[builtins.bool] = None,
    process_cluster_store: typing.Optional[builtins.bool] = None,
    process_push_secret: typing.Optional[builtins.bool] = None,
    rbac: typing.Optional[typing.Union[ExternalSecretsRbac, typing.Dict[builtins.str, typing.Any]]] = None,
    replica_count: typing.Optional[jsii.Number] = None,
    resources: typing.Optional[typing.Union[ExternalSecretsResources, typing.Dict[builtins.str, typing.Any]]] = None,
    revision_history_limit: typing.Optional[jsii.Number] = None,
    scoped_namespace: typing.Optional[builtins.str] = None,
    scoped_rbac: typing.Optional[builtins.bool] = None,
    security_context: typing.Optional[typing.Union[ExternalSecretsSecurityContext, typing.Dict[builtins.str, typing.Any]]] = None,
    service: typing.Optional[typing.Union[ExternalSecretsService, typing.Dict[builtins.str, typing.Any]]] = None,
    service_account: typing.Optional[typing.Union[ExternalSecretsServiceAccount, typing.Dict[builtins.str, typing.Any]]] = None,
    service_monitor: typing.Optional[typing.Union[ExternalSecretsServiceMonitor, typing.Dict[builtins.str, typing.Any]]] = None,
    tolerations: typing.Optional[typing.Sequence[typing.Any]] = None,
    topology_spread_constraints: typing.Optional[typing.Sequence[typing.Any]] = None,
    webhook: typing.Optional[typing.Union[ExternalSecretsWebhook, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass
