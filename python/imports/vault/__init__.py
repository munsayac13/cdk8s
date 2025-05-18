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


class Vault(
    _constructs_77d1e7e8.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="vault.Vault",
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
        values: typing.Optional[typing.Union["VaultValues", typing.Dict[builtins.str, typing.Any]]] = None,
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
            type_hints = typing.get_type_hints(_typecheckingstub__c99521cdcd5598c8561c8003f5aa0e03085b813ce11215d8c685ebd55a3cab8d)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = VaultProps(
            helm_executable=helm_executable,
            helm_flags=helm_flags,
            namespace=namespace,
            release_name=release_name,
            values=values,
        )

        jsii.create(self.__class__, self, [scope, id, props])


@jsii.data_type(
    jsii_type="vault.VaultCsi",
    jsii_struct_bases=[],
    name_mapping={
        "additional_values": "additionalValues",
        "agent": "agent",
        "daemon_set": "daemonSet",
        "debug": "debug",
        "enabled": "enabled",
        "extra_args": "extraArgs",
        "hmac_secret_name": "hmacSecretName",
        "host_network": "hostNetwork",
        "image": "image",
        "liveness_probe": "livenessProbe",
        "log_level": "logLevel",
        "pod": "pod",
        "priority_class_name": "priorityClassName",
        "readiness_probe": "readinessProbe",
        "resources": "resources",
        "service_account": "serviceAccount",
        "volume_mounts": "volumeMounts",
        "volumes": "volumes",
    },
)
class VaultCsi:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        agent: typing.Optional[typing.Union["VaultCsiAgent", typing.Dict[builtins.str, typing.Any]]] = None,
        daemon_set: typing.Optional[typing.Union["VaultCsiDaemonSet", typing.Dict[builtins.str, typing.Any]]] = None,
        debug: typing.Optional[builtins.bool] = None,
        enabled: typing.Any = None,
        extra_args: typing.Optional[typing.Sequence[typing.Any]] = None,
        hmac_secret_name: typing.Optional[builtins.str] = None,
        host_network: typing.Optional[builtins.bool] = None,
        image: typing.Optional[typing.Union["VaultCsiImage", typing.Dict[builtins.str, typing.Any]]] = None,
        liveness_probe: typing.Optional[typing.Union["VaultCsiLivenessProbe", typing.Dict[builtins.str, typing.Any]]] = None,
        log_level: typing.Optional[builtins.str] = None,
        pod: typing.Optional[typing.Union["VaultCsiPod", typing.Dict[builtins.str, typing.Any]]] = None,
        priority_class_name: typing.Optional[builtins.str] = None,
        readiness_probe: typing.Optional[typing.Union["VaultCsiReadinessProbe", typing.Dict[builtins.str, typing.Any]]] = None,
        resources: typing.Any = None,
        service_account: typing.Optional[typing.Union["VaultCsiServiceAccount", typing.Dict[builtins.str, typing.Any]]] = None,
        volume_mounts: typing.Optional[typing.Sequence[typing.Any]] = None,
        volumes: typing.Optional[typing.Sequence[typing.Any]] = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.
        :param agent: 
        :param daemon_set: 
        :param debug: 
        :param enabled: 
        :param extra_args: 
        :param hmac_secret_name: 
        :param host_network: 
        :param image: 
        :param liveness_probe: 
        :param log_level: 
        :param pod: 
        :param priority_class_name: 
        :param readiness_probe: 
        :param resources: 
        :param service_account: 
        :param volume_mounts: 
        :param volumes: 

        :schema: VaultCsi
        '''
        if isinstance(agent, dict):
            agent = VaultCsiAgent(**agent)
        if isinstance(daemon_set, dict):
            daemon_set = VaultCsiDaemonSet(**daemon_set)
        if isinstance(image, dict):
            image = VaultCsiImage(**image)
        if isinstance(liveness_probe, dict):
            liveness_probe = VaultCsiLivenessProbe(**liveness_probe)
        if isinstance(pod, dict):
            pod = VaultCsiPod(**pod)
        if isinstance(readiness_probe, dict):
            readiness_probe = VaultCsiReadinessProbe(**readiness_probe)
        if isinstance(service_account, dict):
            service_account = VaultCsiServiceAccount(**service_account)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eb3cfc5797c505412f97eb99522136e80ea63c882fa1c85bd1534dc1b1949238)
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
            check_type(argname="argument agent", value=agent, expected_type=type_hints["agent"])
            check_type(argname="argument daemon_set", value=daemon_set, expected_type=type_hints["daemon_set"])
            check_type(argname="argument debug", value=debug, expected_type=type_hints["debug"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument extra_args", value=extra_args, expected_type=type_hints["extra_args"])
            check_type(argname="argument hmac_secret_name", value=hmac_secret_name, expected_type=type_hints["hmac_secret_name"])
            check_type(argname="argument host_network", value=host_network, expected_type=type_hints["host_network"])
            check_type(argname="argument image", value=image, expected_type=type_hints["image"])
            check_type(argname="argument liveness_probe", value=liveness_probe, expected_type=type_hints["liveness_probe"])
            check_type(argname="argument log_level", value=log_level, expected_type=type_hints["log_level"])
            check_type(argname="argument pod", value=pod, expected_type=type_hints["pod"])
            check_type(argname="argument priority_class_name", value=priority_class_name, expected_type=type_hints["priority_class_name"])
            check_type(argname="argument readiness_probe", value=readiness_probe, expected_type=type_hints["readiness_probe"])
            check_type(argname="argument resources", value=resources, expected_type=type_hints["resources"])
            check_type(argname="argument service_account", value=service_account, expected_type=type_hints["service_account"])
            check_type(argname="argument volume_mounts", value=volume_mounts, expected_type=type_hints["volume_mounts"])
            check_type(argname="argument volumes", value=volumes, expected_type=type_hints["volumes"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_values is not None:
            self._values["additional_values"] = additional_values
        if agent is not None:
            self._values["agent"] = agent
        if daemon_set is not None:
            self._values["daemon_set"] = daemon_set
        if debug is not None:
            self._values["debug"] = debug
        if enabled is not None:
            self._values["enabled"] = enabled
        if extra_args is not None:
            self._values["extra_args"] = extra_args
        if hmac_secret_name is not None:
            self._values["hmac_secret_name"] = hmac_secret_name
        if host_network is not None:
            self._values["host_network"] = host_network
        if image is not None:
            self._values["image"] = image
        if liveness_probe is not None:
            self._values["liveness_probe"] = liveness_probe
        if log_level is not None:
            self._values["log_level"] = log_level
        if pod is not None:
            self._values["pod"] = pod
        if priority_class_name is not None:
            self._values["priority_class_name"] = priority_class_name
        if readiness_probe is not None:
            self._values["readiness_probe"] = readiness_probe
        if resources is not None:
            self._values["resources"] = resources
        if service_account is not None:
            self._values["service_account"] = service_account
        if volume_mounts is not None:
            self._values["volume_mounts"] = volume_mounts
        if volumes is not None:
            self._values["volumes"] = volumes

    @builtins.property
    def additional_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: VaultCsi#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def agent(self) -> typing.Optional["VaultCsiAgent"]:
        '''
        :schema: VaultCsi#agent
        '''
        result = self._values.get("agent")
        return typing.cast(typing.Optional["VaultCsiAgent"], result)

    @builtins.property
    def daemon_set(self) -> typing.Optional["VaultCsiDaemonSet"]:
        '''
        :schema: VaultCsi#daemonSet
        '''
        result = self._values.get("daemon_set")
        return typing.cast(typing.Optional["VaultCsiDaemonSet"], result)

    @builtins.property
    def debug(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: VaultCsi#debug
        '''
        result = self._values.get("debug")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def enabled(self) -> typing.Any:
        '''
        :schema: VaultCsi#enabled
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Any, result)

    @builtins.property
    def extra_args(self) -> typing.Optional[typing.List[typing.Any]]:
        '''
        :schema: VaultCsi#extraArgs
        '''
        result = self._values.get("extra_args")
        return typing.cast(typing.Optional[typing.List[typing.Any]], result)

    @builtins.property
    def hmac_secret_name(self) -> typing.Optional[builtins.str]:
        '''
        :schema: VaultCsi#hmacSecretName
        '''
        result = self._values.get("hmac_secret_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def host_network(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: VaultCsi#hostNetwork
        '''
        result = self._values.get("host_network")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def image(self) -> typing.Optional["VaultCsiImage"]:
        '''
        :schema: VaultCsi#image
        '''
        result = self._values.get("image")
        return typing.cast(typing.Optional["VaultCsiImage"], result)

    @builtins.property
    def liveness_probe(self) -> typing.Optional["VaultCsiLivenessProbe"]:
        '''
        :schema: VaultCsi#livenessProbe
        '''
        result = self._values.get("liveness_probe")
        return typing.cast(typing.Optional["VaultCsiLivenessProbe"], result)

    @builtins.property
    def log_level(self) -> typing.Optional[builtins.str]:
        '''
        :schema: VaultCsi#logLevel
        '''
        result = self._values.get("log_level")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def pod(self) -> typing.Optional["VaultCsiPod"]:
        '''
        :schema: VaultCsi#pod
        '''
        result = self._values.get("pod")
        return typing.cast(typing.Optional["VaultCsiPod"], result)

    @builtins.property
    def priority_class_name(self) -> typing.Optional[builtins.str]:
        '''
        :schema: VaultCsi#priorityClassName
        '''
        result = self._values.get("priority_class_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def readiness_probe(self) -> typing.Optional["VaultCsiReadinessProbe"]:
        '''
        :schema: VaultCsi#readinessProbe
        '''
        result = self._values.get("readiness_probe")
        return typing.cast(typing.Optional["VaultCsiReadinessProbe"], result)

    @builtins.property
    def resources(self) -> typing.Any:
        '''
        :schema: VaultCsi#resources
        '''
        result = self._values.get("resources")
        return typing.cast(typing.Any, result)

    @builtins.property
    def service_account(self) -> typing.Optional["VaultCsiServiceAccount"]:
        '''
        :schema: VaultCsi#serviceAccount
        '''
        result = self._values.get("service_account")
        return typing.cast(typing.Optional["VaultCsiServiceAccount"], result)

    @builtins.property
    def volume_mounts(self) -> typing.Optional[typing.List[typing.Any]]:
        '''
        :schema: VaultCsi#volumeMounts
        '''
        result = self._values.get("volume_mounts")
        return typing.cast(typing.Optional[typing.List[typing.Any]], result)

    @builtins.property
    def volumes(self) -> typing.Optional[typing.List[typing.Any]]:
        '''
        :schema: VaultCsi#volumes
        '''
        result = self._values.get("volumes")
        return typing.cast(typing.Optional[typing.List[typing.Any]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VaultCsi(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="vault.VaultCsiAgent",
    jsii_struct_bases=[],
    name_mapping={
        "additional_values": "additionalValues",
        "enabled": "enabled",
        "extra_args": "extraArgs",
        "image": "image",
        "log_format": "logFormat",
        "log_level": "logLevel",
        "resources": "resources",
    },
)
class VaultCsiAgent:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        enabled: typing.Optional[builtins.bool] = None,
        extra_args: typing.Optional[typing.Sequence[typing.Any]] = None,
        image: typing.Optional[typing.Union["VaultCsiAgentImage", typing.Dict[builtins.str, typing.Any]]] = None,
        log_format: typing.Optional[builtins.str] = None,
        log_level: typing.Optional[builtins.str] = None,
        resources: typing.Any = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.
        :param enabled: 
        :param extra_args: 
        :param image: 
        :param log_format: 
        :param log_level: 
        :param resources: 

        :schema: VaultCsiAgent
        '''
        if isinstance(image, dict):
            image = VaultCsiAgentImage(**image)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__690de3ce0a44178a547711fad97b34116bf025eaa26d164e1bf37f091c57c7a4)
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument extra_args", value=extra_args, expected_type=type_hints["extra_args"])
            check_type(argname="argument image", value=image, expected_type=type_hints["image"])
            check_type(argname="argument log_format", value=log_format, expected_type=type_hints["log_format"])
            check_type(argname="argument log_level", value=log_level, expected_type=type_hints["log_level"])
            check_type(argname="argument resources", value=resources, expected_type=type_hints["resources"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_values is not None:
            self._values["additional_values"] = additional_values
        if enabled is not None:
            self._values["enabled"] = enabled
        if extra_args is not None:
            self._values["extra_args"] = extra_args
        if image is not None:
            self._values["image"] = image
        if log_format is not None:
            self._values["log_format"] = log_format
        if log_level is not None:
            self._values["log_level"] = log_level
        if resources is not None:
            self._values["resources"] = resources

    @builtins.property
    def additional_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: VaultCsiAgent#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def enabled(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: VaultCsiAgent#enabled
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def extra_args(self) -> typing.Optional[typing.List[typing.Any]]:
        '''
        :schema: VaultCsiAgent#extraArgs
        '''
        result = self._values.get("extra_args")
        return typing.cast(typing.Optional[typing.List[typing.Any]], result)

    @builtins.property
    def image(self) -> typing.Optional["VaultCsiAgentImage"]:
        '''
        :schema: VaultCsiAgent#image
        '''
        result = self._values.get("image")
        return typing.cast(typing.Optional["VaultCsiAgentImage"], result)

    @builtins.property
    def log_format(self) -> typing.Optional[builtins.str]:
        '''
        :schema: VaultCsiAgent#logFormat
        '''
        result = self._values.get("log_format")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def log_level(self) -> typing.Optional[builtins.str]:
        '''
        :schema: VaultCsiAgent#logLevel
        '''
        result = self._values.get("log_level")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def resources(self) -> typing.Any:
        '''
        :schema: VaultCsiAgent#resources
        '''
        result = self._values.get("resources")
        return typing.cast(typing.Any, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VaultCsiAgent(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="vault.VaultCsiAgentImage",
    jsii_struct_bases=[],
    name_mapping={
        "additional_values": "additionalValues",
        "pull_policy": "pullPolicy",
        "repository": "repository",
        "tag": "tag",
    },
)
class VaultCsiAgentImage:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        pull_policy: typing.Optional[builtins.str] = None,
        repository: typing.Optional[builtins.str] = None,
        tag: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.
        :param pull_policy: 
        :param repository: 
        :param tag: 

        :schema: VaultCsiAgentImage
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5edb9bf8fe04dbac9f643a4daef3c002f026ab0d1e8ada9193595080bc90853c)
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
            check_type(argname="argument pull_policy", value=pull_policy, expected_type=type_hints["pull_policy"])
            check_type(argname="argument repository", value=repository, expected_type=type_hints["repository"])
            check_type(argname="argument tag", value=tag, expected_type=type_hints["tag"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_values is not None:
            self._values["additional_values"] = additional_values
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

        :schema: VaultCsiAgentImage#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def pull_policy(self) -> typing.Optional[builtins.str]:
        '''
        :schema: VaultCsiAgentImage#pullPolicy
        '''
        result = self._values.get("pull_policy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def repository(self) -> typing.Optional[builtins.str]:
        '''
        :schema: VaultCsiAgentImage#repository
        '''
        result = self._values.get("repository")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tag(self) -> typing.Optional[builtins.str]:
        '''
        :schema: VaultCsiAgentImage#tag
        '''
        result = self._values.get("tag")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VaultCsiAgentImage(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="vault.VaultCsiDaemonSet",
    jsii_struct_bases=[],
    name_mapping={
        "additional_values": "additionalValues",
        "annotations": "annotations",
        "extra_labels": "extraLabels",
        "kubelet_root_dir": "kubeletRootDir",
        "providers_dir": "providersDir",
        "security_context": "securityContext",
        "update_strategy": "updateStrategy",
    },
)
class VaultCsiDaemonSet:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        annotations: typing.Any = None,
        extra_labels: typing.Any = None,
        kubelet_root_dir: typing.Optional[builtins.str] = None,
        providers_dir: typing.Optional[builtins.str] = None,
        security_context: typing.Optional[typing.Union["VaultCsiDaemonSetSecurityContext", typing.Dict[builtins.str, typing.Any]]] = None,
        update_strategy: typing.Optional[typing.Union["VaultCsiDaemonSetUpdateStrategy", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.
        :param annotations: 
        :param extra_labels: 
        :param kubelet_root_dir: 
        :param providers_dir: 
        :param security_context: 
        :param update_strategy: 

        :schema: VaultCsiDaemonSet
        '''
        if isinstance(security_context, dict):
            security_context = VaultCsiDaemonSetSecurityContext(**security_context)
        if isinstance(update_strategy, dict):
            update_strategy = VaultCsiDaemonSetUpdateStrategy(**update_strategy)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e597c736e8d7927b2369e5791cf508a392cf09eb1a2c1db663cb0d2a5df0ddf7)
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
            check_type(argname="argument annotations", value=annotations, expected_type=type_hints["annotations"])
            check_type(argname="argument extra_labels", value=extra_labels, expected_type=type_hints["extra_labels"])
            check_type(argname="argument kubelet_root_dir", value=kubelet_root_dir, expected_type=type_hints["kubelet_root_dir"])
            check_type(argname="argument providers_dir", value=providers_dir, expected_type=type_hints["providers_dir"])
            check_type(argname="argument security_context", value=security_context, expected_type=type_hints["security_context"])
            check_type(argname="argument update_strategy", value=update_strategy, expected_type=type_hints["update_strategy"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_values is not None:
            self._values["additional_values"] = additional_values
        if annotations is not None:
            self._values["annotations"] = annotations
        if extra_labels is not None:
            self._values["extra_labels"] = extra_labels
        if kubelet_root_dir is not None:
            self._values["kubelet_root_dir"] = kubelet_root_dir
        if providers_dir is not None:
            self._values["providers_dir"] = providers_dir
        if security_context is not None:
            self._values["security_context"] = security_context
        if update_strategy is not None:
            self._values["update_strategy"] = update_strategy

    @builtins.property
    def additional_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: VaultCsiDaemonSet#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def annotations(self) -> typing.Any:
        '''
        :schema: VaultCsiDaemonSet#annotations
        '''
        result = self._values.get("annotations")
        return typing.cast(typing.Any, result)

    @builtins.property
    def extra_labels(self) -> typing.Any:
        '''
        :schema: VaultCsiDaemonSet#extraLabels
        '''
        result = self._values.get("extra_labels")
        return typing.cast(typing.Any, result)

    @builtins.property
    def kubelet_root_dir(self) -> typing.Optional[builtins.str]:
        '''
        :schema: VaultCsiDaemonSet#kubeletRootDir
        '''
        result = self._values.get("kubelet_root_dir")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def providers_dir(self) -> typing.Optional[builtins.str]:
        '''
        :schema: VaultCsiDaemonSet#providersDir
        '''
        result = self._values.get("providers_dir")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def security_context(self) -> typing.Optional["VaultCsiDaemonSetSecurityContext"]:
        '''
        :schema: VaultCsiDaemonSet#securityContext
        '''
        result = self._values.get("security_context")
        return typing.cast(typing.Optional["VaultCsiDaemonSetSecurityContext"], result)

    @builtins.property
    def update_strategy(self) -> typing.Optional["VaultCsiDaemonSetUpdateStrategy"]:
        '''
        :schema: VaultCsiDaemonSet#updateStrategy
        '''
        result = self._values.get("update_strategy")
        return typing.cast(typing.Optional["VaultCsiDaemonSetUpdateStrategy"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VaultCsiDaemonSet(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="vault.VaultCsiDaemonSetSecurityContext",
    jsii_struct_bases=[],
    name_mapping={
        "additional_values": "additionalValues",
        "container": "container",
        "pod": "pod",
    },
)
class VaultCsiDaemonSetSecurityContext:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        container: typing.Any = None,
        pod: typing.Any = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.
        :param container: 
        :param pod: 

        :schema: VaultCsiDaemonSetSecurityContext
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__35220034df45f77f18320222defd5c608c761d2b184d88eca911cc2e4239cbf4)
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
            check_type(argname="argument container", value=container, expected_type=type_hints["container"])
            check_type(argname="argument pod", value=pod, expected_type=type_hints["pod"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_values is not None:
            self._values["additional_values"] = additional_values
        if container is not None:
            self._values["container"] = container
        if pod is not None:
            self._values["pod"] = pod

    @builtins.property
    def additional_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: VaultCsiDaemonSetSecurityContext#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def container(self) -> typing.Any:
        '''
        :schema: VaultCsiDaemonSetSecurityContext#container
        '''
        result = self._values.get("container")
        return typing.cast(typing.Any, result)

    @builtins.property
    def pod(self) -> typing.Any:
        '''
        :schema: VaultCsiDaemonSetSecurityContext#pod
        '''
        result = self._values.get("pod")
        return typing.cast(typing.Any, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VaultCsiDaemonSetSecurityContext(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="vault.VaultCsiDaemonSetUpdateStrategy",
    jsii_struct_bases=[],
    name_mapping={
        "additional_values": "additionalValues",
        "max_unavailable": "maxUnavailable",
        "type": "type",
    },
)
class VaultCsiDaemonSetUpdateStrategy:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        max_unavailable: typing.Optional[builtins.str] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.
        :param max_unavailable: 
        :param type: 

        :schema: VaultCsiDaemonSetUpdateStrategy
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3154182529948dde2e8d0a88d335f923a6e5facfd2d8583c777b31f0b180d72e)
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
            check_type(argname="argument max_unavailable", value=max_unavailable, expected_type=type_hints["max_unavailable"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_values is not None:
            self._values["additional_values"] = additional_values
        if max_unavailable is not None:
            self._values["max_unavailable"] = max_unavailable
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def additional_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: VaultCsiDaemonSetUpdateStrategy#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def max_unavailable(self) -> typing.Optional[builtins.str]:
        '''
        :schema: VaultCsiDaemonSetUpdateStrategy#maxUnavailable
        '''
        result = self._values.get("max_unavailable")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: VaultCsiDaemonSetUpdateStrategy#type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VaultCsiDaemonSetUpdateStrategy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="vault.VaultCsiImage",
    jsii_struct_bases=[],
    name_mapping={
        "additional_values": "additionalValues",
        "pull_policy": "pullPolicy",
        "repository": "repository",
        "tag": "tag",
    },
)
class VaultCsiImage:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        pull_policy: typing.Optional[builtins.str] = None,
        repository: typing.Optional[builtins.str] = None,
        tag: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.
        :param pull_policy: 
        :param repository: 
        :param tag: 

        :schema: VaultCsiImage
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__104a4d6b24a0faa09eb09ecf1c1c0457a749ee804cae00ab3a076ded85e0d05c)
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
            check_type(argname="argument pull_policy", value=pull_policy, expected_type=type_hints["pull_policy"])
            check_type(argname="argument repository", value=repository, expected_type=type_hints["repository"])
            check_type(argname="argument tag", value=tag, expected_type=type_hints["tag"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_values is not None:
            self._values["additional_values"] = additional_values
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

        :schema: VaultCsiImage#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def pull_policy(self) -> typing.Optional[builtins.str]:
        '''
        :schema: VaultCsiImage#pullPolicy
        '''
        result = self._values.get("pull_policy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def repository(self) -> typing.Optional[builtins.str]:
        '''
        :schema: VaultCsiImage#repository
        '''
        result = self._values.get("repository")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tag(self) -> typing.Optional[builtins.str]:
        '''
        :schema: VaultCsiImage#tag
        '''
        result = self._values.get("tag")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VaultCsiImage(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="vault.VaultCsiLivenessProbe",
    jsii_struct_bases=[],
    name_mapping={
        "additional_values": "additionalValues",
        "failure_threshold": "failureThreshold",
        "initial_delay_seconds": "initialDelaySeconds",
        "period_seconds": "periodSeconds",
        "success_threshold": "successThreshold",
        "timeout_seconds": "timeoutSeconds",
    },
)
class VaultCsiLivenessProbe:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        failure_threshold: typing.Optional[jsii.Number] = None,
        initial_delay_seconds: typing.Optional[jsii.Number] = None,
        period_seconds: typing.Optional[jsii.Number] = None,
        success_threshold: typing.Optional[jsii.Number] = None,
        timeout_seconds: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.
        :param failure_threshold: 
        :param initial_delay_seconds: 
        :param period_seconds: 
        :param success_threshold: 
        :param timeout_seconds: 

        :schema: VaultCsiLivenessProbe
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b0b372a4df8cd386e5e9ae3168dbb804f461e52f17bb1f86638b598f15fca8c0)
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
            check_type(argname="argument failure_threshold", value=failure_threshold, expected_type=type_hints["failure_threshold"])
            check_type(argname="argument initial_delay_seconds", value=initial_delay_seconds, expected_type=type_hints["initial_delay_seconds"])
            check_type(argname="argument period_seconds", value=period_seconds, expected_type=type_hints["period_seconds"])
            check_type(argname="argument success_threshold", value=success_threshold, expected_type=type_hints["success_threshold"])
            check_type(argname="argument timeout_seconds", value=timeout_seconds, expected_type=type_hints["timeout_seconds"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_values is not None:
            self._values["additional_values"] = additional_values
        if failure_threshold is not None:
            self._values["failure_threshold"] = failure_threshold
        if initial_delay_seconds is not None:
            self._values["initial_delay_seconds"] = initial_delay_seconds
        if period_seconds is not None:
            self._values["period_seconds"] = period_seconds
        if success_threshold is not None:
            self._values["success_threshold"] = success_threshold
        if timeout_seconds is not None:
            self._values["timeout_seconds"] = timeout_seconds

    @builtins.property
    def additional_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: VaultCsiLivenessProbe#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def failure_threshold(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: VaultCsiLivenessProbe#failureThreshold
        '''
        result = self._values.get("failure_threshold")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def initial_delay_seconds(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: VaultCsiLivenessProbe#initialDelaySeconds
        '''
        result = self._values.get("initial_delay_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def period_seconds(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: VaultCsiLivenessProbe#periodSeconds
        '''
        result = self._values.get("period_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def success_threshold(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: VaultCsiLivenessProbe#successThreshold
        '''
        result = self._values.get("success_threshold")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def timeout_seconds(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: VaultCsiLivenessProbe#timeoutSeconds
        '''
        result = self._values.get("timeout_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VaultCsiLivenessProbe(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="vault.VaultCsiPod",
    jsii_struct_bases=[],
    name_mapping={
        "additional_values": "additionalValues",
        "affinity": "affinity",
        "annotations": "annotations",
        "extra_labels": "extraLabels",
        "node_selector": "nodeSelector",
        "tolerations": "tolerations",
    },
)
class VaultCsiPod:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        affinity: typing.Any = None,
        annotations: typing.Any = None,
        extra_labels: typing.Any = None,
        node_selector: typing.Any = None,
        tolerations: typing.Any = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.
        :param affinity: 
        :param annotations: 
        :param extra_labels: 
        :param node_selector: 
        :param tolerations: 

        :schema: VaultCsiPod
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bbcf2f0f1ac2f575f8be9d45a001b987e27e835f0e587a9e0090ed3f51eb2a12)
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
            check_type(argname="argument affinity", value=affinity, expected_type=type_hints["affinity"])
            check_type(argname="argument annotations", value=annotations, expected_type=type_hints["annotations"])
            check_type(argname="argument extra_labels", value=extra_labels, expected_type=type_hints["extra_labels"])
            check_type(argname="argument node_selector", value=node_selector, expected_type=type_hints["node_selector"])
            check_type(argname="argument tolerations", value=tolerations, expected_type=type_hints["tolerations"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_values is not None:
            self._values["additional_values"] = additional_values
        if affinity is not None:
            self._values["affinity"] = affinity
        if annotations is not None:
            self._values["annotations"] = annotations
        if extra_labels is not None:
            self._values["extra_labels"] = extra_labels
        if node_selector is not None:
            self._values["node_selector"] = node_selector
        if tolerations is not None:
            self._values["tolerations"] = tolerations

    @builtins.property
    def additional_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: VaultCsiPod#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def affinity(self) -> typing.Any:
        '''
        :schema: VaultCsiPod#affinity
        '''
        result = self._values.get("affinity")
        return typing.cast(typing.Any, result)

    @builtins.property
    def annotations(self) -> typing.Any:
        '''
        :schema: VaultCsiPod#annotations
        '''
        result = self._values.get("annotations")
        return typing.cast(typing.Any, result)

    @builtins.property
    def extra_labels(self) -> typing.Any:
        '''
        :schema: VaultCsiPod#extraLabels
        '''
        result = self._values.get("extra_labels")
        return typing.cast(typing.Any, result)

    @builtins.property
    def node_selector(self) -> typing.Any:
        '''
        :schema: VaultCsiPod#nodeSelector
        '''
        result = self._values.get("node_selector")
        return typing.cast(typing.Any, result)

    @builtins.property
    def tolerations(self) -> typing.Any:
        '''
        :schema: VaultCsiPod#tolerations
        '''
        result = self._values.get("tolerations")
        return typing.cast(typing.Any, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VaultCsiPod(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="vault.VaultCsiReadinessProbe",
    jsii_struct_bases=[],
    name_mapping={
        "additional_values": "additionalValues",
        "failure_threshold": "failureThreshold",
        "initial_delay_seconds": "initialDelaySeconds",
        "period_seconds": "periodSeconds",
        "success_threshold": "successThreshold",
        "timeout_seconds": "timeoutSeconds",
    },
)
class VaultCsiReadinessProbe:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        failure_threshold: typing.Optional[jsii.Number] = None,
        initial_delay_seconds: typing.Optional[jsii.Number] = None,
        period_seconds: typing.Optional[jsii.Number] = None,
        success_threshold: typing.Optional[jsii.Number] = None,
        timeout_seconds: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.
        :param failure_threshold: 
        :param initial_delay_seconds: 
        :param period_seconds: 
        :param success_threshold: 
        :param timeout_seconds: 

        :schema: VaultCsiReadinessProbe
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c59e9ff042ba7058e6b8f7d1e02c2c22f94607384c141d16f4554100fd884601)
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
            check_type(argname="argument failure_threshold", value=failure_threshold, expected_type=type_hints["failure_threshold"])
            check_type(argname="argument initial_delay_seconds", value=initial_delay_seconds, expected_type=type_hints["initial_delay_seconds"])
            check_type(argname="argument period_seconds", value=period_seconds, expected_type=type_hints["period_seconds"])
            check_type(argname="argument success_threshold", value=success_threshold, expected_type=type_hints["success_threshold"])
            check_type(argname="argument timeout_seconds", value=timeout_seconds, expected_type=type_hints["timeout_seconds"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_values is not None:
            self._values["additional_values"] = additional_values
        if failure_threshold is not None:
            self._values["failure_threshold"] = failure_threshold
        if initial_delay_seconds is not None:
            self._values["initial_delay_seconds"] = initial_delay_seconds
        if period_seconds is not None:
            self._values["period_seconds"] = period_seconds
        if success_threshold is not None:
            self._values["success_threshold"] = success_threshold
        if timeout_seconds is not None:
            self._values["timeout_seconds"] = timeout_seconds

    @builtins.property
    def additional_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: VaultCsiReadinessProbe#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def failure_threshold(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: VaultCsiReadinessProbe#failureThreshold
        '''
        result = self._values.get("failure_threshold")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def initial_delay_seconds(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: VaultCsiReadinessProbe#initialDelaySeconds
        '''
        result = self._values.get("initial_delay_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def period_seconds(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: VaultCsiReadinessProbe#periodSeconds
        '''
        result = self._values.get("period_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def success_threshold(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: VaultCsiReadinessProbe#successThreshold
        '''
        result = self._values.get("success_threshold")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def timeout_seconds(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: VaultCsiReadinessProbe#timeoutSeconds
        '''
        result = self._values.get("timeout_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VaultCsiReadinessProbe(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="vault.VaultCsiServiceAccount",
    jsii_struct_bases=[],
    name_mapping={
        "additional_values": "additionalValues",
        "annotations": "annotations",
        "extra_labels": "extraLabels",
    },
)
class VaultCsiServiceAccount:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        annotations: typing.Any = None,
        extra_labels: typing.Any = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.
        :param annotations: 
        :param extra_labels: 

        :schema: VaultCsiServiceAccount
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4778e3b6220ebd049d4955a2000aceb362406c165c9cd7ee9f56ca621aa7b0ab)
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
            check_type(argname="argument annotations", value=annotations, expected_type=type_hints["annotations"])
            check_type(argname="argument extra_labels", value=extra_labels, expected_type=type_hints["extra_labels"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_values is not None:
            self._values["additional_values"] = additional_values
        if annotations is not None:
            self._values["annotations"] = annotations
        if extra_labels is not None:
            self._values["extra_labels"] = extra_labels

    @builtins.property
    def additional_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: VaultCsiServiceAccount#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def annotations(self) -> typing.Any:
        '''
        :schema: VaultCsiServiceAccount#annotations
        '''
        result = self._values.get("annotations")
        return typing.cast(typing.Any, result)

    @builtins.property
    def extra_labels(self) -> typing.Any:
        '''
        :schema: VaultCsiServiceAccount#extraLabels
        '''
        result = self._values.get("extra_labels")
        return typing.cast(typing.Any, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VaultCsiServiceAccount(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="vault.VaultInjector",
    jsii_struct_bases=[],
    name_mapping={
        "additional_values": "additionalValues",
        "affinity": "affinity",
        "agent_defaults": "agentDefaults",
        "agent_image": "agentImage",
        "annotations": "annotations",
        "auth_path": "authPath",
        "certs": "certs",
        "enabled": "enabled",
        "external_vault_addr": "externalVaultAddr",
        "extra_environment_vars": "extraEnvironmentVars",
        "extra_labels": "extraLabels",
        "failure_policy": "failurePolicy",
        "host_network": "hostNetwork",
        "image": "image",
        "leader_elector": "leaderElector",
        "liveness_probe": "livenessProbe",
        "log_format": "logFormat",
        "log_level": "logLevel",
        "metrics": "metrics",
        "namespace_selector": "namespaceSelector",
        "node_selector": "nodeSelector",
        "object_selector": "objectSelector",
        "pod_disruption_budget": "podDisruptionBudget",
        "port": "port",
        "priority_class_name": "priorityClassName",
        "readiness_probe": "readinessProbe",
        "replicas": "replicas",
        "resources": "resources",
        "revoke_on_shutdown": "revokeOnShutdown",
        "security_context": "securityContext",
        "service": "service",
        "service_account": "serviceAccount",
        "startup_probe": "startupProbe",
        "strategy": "strategy",
        "tolerations": "tolerations",
        "topology_spread_constraints": "topologySpreadConstraints",
        "webhook": "webhook",
        "webhook_annotations": "webhookAnnotations",
    },
)
class VaultInjector:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        affinity: typing.Any = None,
        agent_defaults: typing.Optional[typing.Union["VaultInjectorAgentDefaults", typing.Dict[builtins.str, typing.Any]]] = None,
        agent_image: typing.Optional[typing.Union["VaultInjectorAgentImage", typing.Dict[builtins.str, typing.Any]]] = None,
        annotations: typing.Any = None,
        auth_path: typing.Optional[builtins.str] = None,
        certs: typing.Optional[typing.Union["VaultInjectorCerts", typing.Dict[builtins.str, typing.Any]]] = None,
        enabled: typing.Any = None,
        external_vault_addr: typing.Optional[builtins.str] = None,
        extra_environment_vars: typing.Any = None,
        extra_labels: typing.Any = None,
        failure_policy: typing.Optional[builtins.str] = None,
        host_network: typing.Optional[builtins.bool] = None,
        image: typing.Optional[typing.Union["VaultInjectorImage", typing.Dict[builtins.str, typing.Any]]] = None,
        leader_elector: typing.Optional[typing.Union["VaultInjectorLeaderElector", typing.Dict[builtins.str, typing.Any]]] = None,
        liveness_probe: typing.Optional[typing.Union["VaultInjectorLivenessProbe", typing.Dict[builtins.str, typing.Any]]] = None,
        log_format: typing.Optional[builtins.str] = None,
        log_level: typing.Optional[builtins.str] = None,
        metrics: typing.Optional[typing.Union["VaultInjectorMetrics", typing.Dict[builtins.str, typing.Any]]] = None,
        namespace_selector: typing.Any = None,
        node_selector: typing.Any = None,
        object_selector: typing.Any = None,
        pod_disruption_budget: typing.Any = None,
        port: typing.Optional[jsii.Number] = None,
        priority_class_name: typing.Optional[builtins.str] = None,
        readiness_probe: typing.Optional[typing.Union["VaultInjectorReadinessProbe", typing.Dict[builtins.str, typing.Any]]] = None,
        replicas: typing.Optional[jsii.Number] = None,
        resources: typing.Any = None,
        revoke_on_shutdown: typing.Optional[builtins.bool] = None,
        security_context: typing.Optional[typing.Union["VaultInjectorSecurityContext", typing.Dict[builtins.str, typing.Any]]] = None,
        service: typing.Optional[typing.Union["VaultInjectorService", typing.Dict[builtins.str, typing.Any]]] = None,
        service_account: typing.Optional[typing.Union["VaultInjectorServiceAccount", typing.Dict[builtins.str, typing.Any]]] = None,
        startup_probe: typing.Optional[typing.Union["VaultInjectorStartupProbe", typing.Dict[builtins.str, typing.Any]]] = None,
        strategy: typing.Any = None,
        tolerations: typing.Any = None,
        topology_spread_constraints: typing.Any = None,
        webhook: typing.Optional[typing.Union["VaultInjectorWebhook", typing.Dict[builtins.str, typing.Any]]] = None,
        webhook_annotations: typing.Any = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.
        :param affinity: 
        :param agent_defaults: 
        :param agent_image: 
        :param annotations: 
        :param auth_path: 
        :param certs: 
        :param enabled: 
        :param external_vault_addr: 
        :param extra_environment_vars: 
        :param extra_labels: 
        :param failure_policy: 
        :param host_network: 
        :param image: 
        :param leader_elector: 
        :param liveness_probe: 
        :param log_format: 
        :param log_level: 
        :param metrics: 
        :param namespace_selector: 
        :param node_selector: 
        :param object_selector: 
        :param pod_disruption_budget: 
        :param port: 
        :param priority_class_name: 
        :param readiness_probe: 
        :param replicas: 
        :param resources: 
        :param revoke_on_shutdown: 
        :param security_context: 
        :param service: 
        :param service_account: 
        :param startup_probe: 
        :param strategy: 
        :param tolerations: 
        :param topology_spread_constraints: 
        :param webhook: 
        :param webhook_annotations: 

        :schema: VaultInjector
        '''
        if isinstance(agent_defaults, dict):
            agent_defaults = VaultInjectorAgentDefaults(**agent_defaults)
        if isinstance(agent_image, dict):
            agent_image = VaultInjectorAgentImage(**agent_image)
        if isinstance(certs, dict):
            certs = VaultInjectorCerts(**certs)
        if isinstance(image, dict):
            image = VaultInjectorImage(**image)
        if isinstance(leader_elector, dict):
            leader_elector = VaultInjectorLeaderElector(**leader_elector)
        if isinstance(liveness_probe, dict):
            liveness_probe = VaultInjectorLivenessProbe(**liveness_probe)
        if isinstance(metrics, dict):
            metrics = VaultInjectorMetrics(**metrics)
        if isinstance(readiness_probe, dict):
            readiness_probe = VaultInjectorReadinessProbe(**readiness_probe)
        if isinstance(security_context, dict):
            security_context = VaultInjectorSecurityContext(**security_context)
        if isinstance(service, dict):
            service = VaultInjectorService(**service)
        if isinstance(service_account, dict):
            service_account = VaultInjectorServiceAccount(**service_account)
        if isinstance(startup_probe, dict):
            startup_probe = VaultInjectorStartupProbe(**startup_probe)
        if isinstance(webhook, dict):
            webhook = VaultInjectorWebhook(**webhook)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cee6dc0abd85a66c574529991e8a568c04956118370ee82269d2e6d03f2fc585)
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
            check_type(argname="argument affinity", value=affinity, expected_type=type_hints["affinity"])
            check_type(argname="argument agent_defaults", value=agent_defaults, expected_type=type_hints["agent_defaults"])
            check_type(argname="argument agent_image", value=agent_image, expected_type=type_hints["agent_image"])
            check_type(argname="argument annotations", value=annotations, expected_type=type_hints["annotations"])
            check_type(argname="argument auth_path", value=auth_path, expected_type=type_hints["auth_path"])
            check_type(argname="argument certs", value=certs, expected_type=type_hints["certs"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument external_vault_addr", value=external_vault_addr, expected_type=type_hints["external_vault_addr"])
            check_type(argname="argument extra_environment_vars", value=extra_environment_vars, expected_type=type_hints["extra_environment_vars"])
            check_type(argname="argument extra_labels", value=extra_labels, expected_type=type_hints["extra_labels"])
            check_type(argname="argument failure_policy", value=failure_policy, expected_type=type_hints["failure_policy"])
            check_type(argname="argument host_network", value=host_network, expected_type=type_hints["host_network"])
            check_type(argname="argument image", value=image, expected_type=type_hints["image"])
            check_type(argname="argument leader_elector", value=leader_elector, expected_type=type_hints["leader_elector"])
            check_type(argname="argument liveness_probe", value=liveness_probe, expected_type=type_hints["liveness_probe"])
            check_type(argname="argument log_format", value=log_format, expected_type=type_hints["log_format"])
            check_type(argname="argument log_level", value=log_level, expected_type=type_hints["log_level"])
            check_type(argname="argument metrics", value=metrics, expected_type=type_hints["metrics"])
            check_type(argname="argument namespace_selector", value=namespace_selector, expected_type=type_hints["namespace_selector"])
            check_type(argname="argument node_selector", value=node_selector, expected_type=type_hints["node_selector"])
            check_type(argname="argument object_selector", value=object_selector, expected_type=type_hints["object_selector"])
            check_type(argname="argument pod_disruption_budget", value=pod_disruption_budget, expected_type=type_hints["pod_disruption_budget"])
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
            check_type(argname="argument priority_class_name", value=priority_class_name, expected_type=type_hints["priority_class_name"])
            check_type(argname="argument readiness_probe", value=readiness_probe, expected_type=type_hints["readiness_probe"])
            check_type(argname="argument replicas", value=replicas, expected_type=type_hints["replicas"])
            check_type(argname="argument resources", value=resources, expected_type=type_hints["resources"])
            check_type(argname="argument revoke_on_shutdown", value=revoke_on_shutdown, expected_type=type_hints["revoke_on_shutdown"])
            check_type(argname="argument security_context", value=security_context, expected_type=type_hints["security_context"])
            check_type(argname="argument service", value=service, expected_type=type_hints["service"])
            check_type(argname="argument service_account", value=service_account, expected_type=type_hints["service_account"])
            check_type(argname="argument startup_probe", value=startup_probe, expected_type=type_hints["startup_probe"])
            check_type(argname="argument strategy", value=strategy, expected_type=type_hints["strategy"])
            check_type(argname="argument tolerations", value=tolerations, expected_type=type_hints["tolerations"])
            check_type(argname="argument topology_spread_constraints", value=topology_spread_constraints, expected_type=type_hints["topology_spread_constraints"])
            check_type(argname="argument webhook", value=webhook, expected_type=type_hints["webhook"])
            check_type(argname="argument webhook_annotations", value=webhook_annotations, expected_type=type_hints["webhook_annotations"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_values is not None:
            self._values["additional_values"] = additional_values
        if affinity is not None:
            self._values["affinity"] = affinity
        if agent_defaults is not None:
            self._values["agent_defaults"] = agent_defaults
        if agent_image is not None:
            self._values["agent_image"] = agent_image
        if annotations is not None:
            self._values["annotations"] = annotations
        if auth_path is not None:
            self._values["auth_path"] = auth_path
        if certs is not None:
            self._values["certs"] = certs
        if enabled is not None:
            self._values["enabled"] = enabled
        if external_vault_addr is not None:
            self._values["external_vault_addr"] = external_vault_addr
        if extra_environment_vars is not None:
            self._values["extra_environment_vars"] = extra_environment_vars
        if extra_labels is not None:
            self._values["extra_labels"] = extra_labels
        if failure_policy is not None:
            self._values["failure_policy"] = failure_policy
        if host_network is not None:
            self._values["host_network"] = host_network
        if image is not None:
            self._values["image"] = image
        if leader_elector is not None:
            self._values["leader_elector"] = leader_elector
        if liveness_probe is not None:
            self._values["liveness_probe"] = liveness_probe
        if log_format is not None:
            self._values["log_format"] = log_format
        if log_level is not None:
            self._values["log_level"] = log_level
        if metrics is not None:
            self._values["metrics"] = metrics
        if namespace_selector is not None:
            self._values["namespace_selector"] = namespace_selector
        if node_selector is not None:
            self._values["node_selector"] = node_selector
        if object_selector is not None:
            self._values["object_selector"] = object_selector
        if pod_disruption_budget is not None:
            self._values["pod_disruption_budget"] = pod_disruption_budget
        if port is not None:
            self._values["port"] = port
        if priority_class_name is not None:
            self._values["priority_class_name"] = priority_class_name
        if readiness_probe is not None:
            self._values["readiness_probe"] = readiness_probe
        if replicas is not None:
            self._values["replicas"] = replicas
        if resources is not None:
            self._values["resources"] = resources
        if revoke_on_shutdown is not None:
            self._values["revoke_on_shutdown"] = revoke_on_shutdown
        if security_context is not None:
            self._values["security_context"] = security_context
        if service is not None:
            self._values["service"] = service
        if service_account is not None:
            self._values["service_account"] = service_account
        if startup_probe is not None:
            self._values["startup_probe"] = startup_probe
        if strategy is not None:
            self._values["strategy"] = strategy
        if tolerations is not None:
            self._values["tolerations"] = tolerations
        if topology_spread_constraints is not None:
            self._values["topology_spread_constraints"] = topology_spread_constraints
        if webhook is not None:
            self._values["webhook"] = webhook
        if webhook_annotations is not None:
            self._values["webhook_annotations"] = webhook_annotations

    @builtins.property
    def additional_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: VaultInjector#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def affinity(self) -> typing.Any:
        '''
        :schema: VaultInjector#affinity
        '''
        result = self._values.get("affinity")
        return typing.cast(typing.Any, result)

    @builtins.property
    def agent_defaults(self) -> typing.Optional["VaultInjectorAgentDefaults"]:
        '''
        :schema: VaultInjector#agentDefaults
        '''
        result = self._values.get("agent_defaults")
        return typing.cast(typing.Optional["VaultInjectorAgentDefaults"], result)

    @builtins.property
    def agent_image(self) -> typing.Optional["VaultInjectorAgentImage"]:
        '''
        :schema: VaultInjector#agentImage
        '''
        result = self._values.get("agent_image")
        return typing.cast(typing.Optional["VaultInjectorAgentImage"], result)

    @builtins.property
    def annotations(self) -> typing.Any:
        '''
        :schema: VaultInjector#annotations
        '''
        result = self._values.get("annotations")
        return typing.cast(typing.Any, result)

    @builtins.property
    def auth_path(self) -> typing.Optional[builtins.str]:
        '''
        :schema: VaultInjector#authPath
        '''
        result = self._values.get("auth_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def certs(self) -> typing.Optional["VaultInjectorCerts"]:
        '''
        :schema: VaultInjector#certs
        '''
        result = self._values.get("certs")
        return typing.cast(typing.Optional["VaultInjectorCerts"], result)

    @builtins.property
    def enabled(self) -> typing.Any:
        '''
        :schema: VaultInjector#enabled
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Any, result)

    @builtins.property
    def external_vault_addr(self) -> typing.Optional[builtins.str]:
        '''
        :schema: VaultInjector#externalVaultAddr
        '''
        result = self._values.get("external_vault_addr")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def extra_environment_vars(self) -> typing.Any:
        '''
        :schema: VaultInjector#extraEnvironmentVars
        '''
        result = self._values.get("extra_environment_vars")
        return typing.cast(typing.Any, result)

    @builtins.property
    def extra_labels(self) -> typing.Any:
        '''
        :schema: VaultInjector#extraLabels
        '''
        result = self._values.get("extra_labels")
        return typing.cast(typing.Any, result)

    @builtins.property
    def failure_policy(self) -> typing.Optional[builtins.str]:
        '''
        :schema: VaultInjector#failurePolicy
        '''
        result = self._values.get("failure_policy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def host_network(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: VaultInjector#hostNetwork
        '''
        result = self._values.get("host_network")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def image(self) -> typing.Optional["VaultInjectorImage"]:
        '''
        :schema: VaultInjector#image
        '''
        result = self._values.get("image")
        return typing.cast(typing.Optional["VaultInjectorImage"], result)

    @builtins.property
    def leader_elector(self) -> typing.Optional["VaultInjectorLeaderElector"]:
        '''
        :schema: VaultInjector#leaderElector
        '''
        result = self._values.get("leader_elector")
        return typing.cast(typing.Optional["VaultInjectorLeaderElector"], result)

    @builtins.property
    def liveness_probe(self) -> typing.Optional["VaultInjectorLivenessProbe"]:
        '''
        :schema: VaultInjector#livenessProbe
        '''
        result = self._values.get("liveness_probe")
        return typing.cast(typing.Optional["VaultInjectorLivenessProbe"], result)

    @builtins.property
    def log_format(self) -> typing.Optional[builtins.str]:
        '''
        :schema: VaultInjector#logFormat
        '''
        result = self._values.get("log_format")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def log_level(self) -> typing.Optional[builtins.str]:
        '''
        :schema: VaultInjector#logLevel
        '''
        result = self._values.get("log_level")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def metrics(self) -> typing.Optional["VaultInjectorMetrics"]:
        '''
        :schema: VaultInjector#metrics
        '''
        result = self._values.get("metrics")
        return typing.cast(typing.Optional["VaultInjectorMetrics"], result)

    @builtins.property
    def namespace_selector(self) -> typing.Any:
        '''
        :schema: VaultInjector#namespaceSelector
        '''
        result = self._values.get("namespace_selector")
        return typing.cast(typing.Any, result)

    @builtins.property
    def node_selector(self) -> typing.Any:
        '''
        :schema: VaultInjector#nodeSelector
        '''
        result = self._values.get("node_selector")
        return typing.cast(typing.Any, result)

    @builtins.property
    def object_selector(self) -> typing.Any:
        '''
        :schema: VaultInjector#objectSelector
        '''
        result = self._values.get("object_selector")
        return typing.cast(typing.Any, result)

    @builtins.property
    def pod_disruption_budget(self) -> typing.Any:
        '''
        :schema: VaultInjector#podDisruptionBudget
        '''
        result = self._values.get("pod_disruption_budget")
        return typing.cast(typing.Any, result)

    @builtins.property
    def port(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: VaultInjector#port
        '''
        result = self._values.get("port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def priority_class_name(self) -> typing.Optional[builtins.str]:
        '''
        :schema: VaultInjector#priorityClassName
        '''
        result = self._values.get("priority_class_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def readiness_probe(self) -> typing.Optional["VaultInjectorReadinessProbe"]:
        '''
        :schema: VaultInjector#readinessProbe
        '''
        result = self._values.get("readiness_probe")
        return typing.cast(typing.Optional["VaultInjectorReadinessProbe"], result)

    @builtins.property
    def replicas(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: VaultInjector#replicas
        '''
        result = self._values.get("replicas")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def resources(self) -> typing.Any:
        '''
        :schema: VaultInjector#resources
        '''
        result = self._values.get("resources")
        return typing.cast(typing.Any, result)

    @builtins.property
    def revoke_on_shutdown(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: VaultInjector#revokeOnShutdown
        '''
        result = self._values.get("revoke_on_shutdown")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def security_context(self) -> typing.Optional["VaultInjectorSecurityContext"]:
        '''
        :schema: VaultInjector#securityContext
        '''
        result = self._values.get("security_context")
        return typing.cast(typing.Optional["VaultInjectorSecurityContext"], result)

    @builtins.property
    def service(self) -> typing.Optional["VaultInjectorService"]:
        '''
        :schema: VaultInjector#service
        '''
        result = self._values.get("service")
        return typing.cast(typing.Optional["VaultInjectorService"], result)

    @builtins.property
    def service_account(self) -> typing.Optional["VaultInjectorServiceAccount"]:
        '''
        :schema: VaultInjector#serviceAccount
        '''
        result = self._values.get("service_account")
        return typing.cast(typing.Optional["VaultInjectorServiceAccount"], result)

    @builtins.property
    def startup_probe(self) -> typing.Optional["VaultInjectorStartupProbe"]:
        '''
        :schema: VaultInjector#startupProbe
        '''
        result = self._values.get("startup_probe")
        return typing.cast(typing.Optional["VaultInjectorStartupProbe"], result)

    @builtins.property
    def strategy(self) -> typing.Any:
        '''
        :schema: VaultInjector#strategy
        '''
        result = self._values.get("strategy")
        return typing.cast(typing.Any, result)

    @builtins.property
    def tolerations(self) -> typing.Any:
        '''
        :schema: VaultInjector#tolerations
        '''
        result = self._values.get("tolerations")
        return typing.cast(typing.Any, result)

    @builtins.property
    def topology_spread_constraints(self) -> typing.Any:
        '''
        :schema: VaultInjector#topologySpreadConstraints
        '''
        result = self._values.get("topology_spread_constraints")
        return typing.cast(typing.Any, result)

    @builtins.property
    def webhook(self) -> typing.Optional["VaultInjectorWebhook"]:
        '''
        :schema: VaultInjector#webhook
        '''
        result = self._values.get("webhook")
        return typing.cast(typing.Optional["VaultInjectorWebhook"], result)

    @builtins.property
    def webhook_annotations(self) -> typing.Any:
        '''
        :schema: VaultInjector#webhookAnnotations
        '''
        result = self._values.get("webhook_annotations")
        return typing.cast(typing.Any, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VaultInjector(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="vault.VaultInjectorAgentDefaults",
    jsii_struct_bases=[],
    name_mapping={
        "additional_values": "additionalValues",
        "cpu_limit": "cpuLimit",
        "cpu_request": "cpuRequest",
        "ephemeral_limit": "ephemeralLimit",
        "ephemeral_request": "ephemeralRequest",
        "mem_limit": "memLimit",
        "mem_request": "memRequest",
        "template": "template",
        "template_config": "templateConfig",
    },
)
class VaultInjectorAgentDefaults:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        cpu_limit: typing.Optional[builtins.str] = None,
        cpu_request: typing.Optional[builtins.str] = None,
        ephemeral_limit: typing.Optional[builtins.str] = None,
        ephemeral_request: typing.Optional[builtins.str] = None,
        mem_limit: typing.Optional[builtins.str] = None,
        mem_request: typing.Optional[builtins.str] = None,
        template: typing.Optional[builtins.str] = None,
        template_config: typing.Optional[typing.Union["VaultInjectorAgentDefaultsTemplateConfig", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.
        :param cpu_limit: 
        :param cpu_request: 
        :param ephemeral_limit: 
        :param ephemeral_request: 
        :param mem_limit: 
        :param mem_request: 
        :param template: 
        :param template_config: 

        :schema: VaultInjectorAgentDefaults
        '''
        if isinstance(template_config, dict):
            template_config = VaultInjectorAgentDefaultsTemplateConfig(**template_config)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__51b4fe880e8893046d0a8b11c912ef33be6187b434ec0c25eb05b1201dd91bb3)
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
            check_type(argname="argument cpu_limit", value=cpu_limit, expected_type=type_hints["cpu_limit"])
            check_type(argname="argument cpu_request", value=cpu_request, expected_type=type_hints["cpu_request"])
            check_type(argname="argument ephemeral_limit", value=ephemeral_limit, expected_type=type_hints["ephemeral_limit"])
            check_type(argname="argument ephemeral_request", value=ephemeral_request, expected_type=type_hints["ephemeral_request"])
            check_type(argname="argument mem_limit", value=mem_limit, expected_type=type_hints["mem_limit"])
            check_type(argname="argument mem_request", value=mem_request, expected_type=type_hints["mem_request"])
            check_type(argname="argument template", value=template, expected_type=type_hints["template"])
            check_type(argname="argument template_config", value=template_config, expected_type=type_hints["template_config"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_values is not None:
            self._values["additional_values"] = additional_values
        if cpu_limit is not None:
            self._values["cpu_limit"] = cpu_limit
        if cpu_request is not None:
            self._values["cpu_request"] = cpu_request
        if ephemeral_limit is not None:
            self._values["ephemeral_limit"] = ephemeral_limit
        if ephemeral_request is not None:
            self._values["ephemeral_request"] = ephemeral_request
        if mem_limit is not None:
            self._values["mem_limit"] = mem_limit
        if mem_request is not None:
            self._values["mem_request"] = mem_request
        if template is not None:
            self._values["template"] = template
        if template_config is not None:
            self._values["template_config"] = template_config

    @builtins.property
    def additional_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: VaultInjectorAgentDefaults#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def cpu_limit(self) -> typing.Optional[builtins.str]:
        '''
        :schema: VaultInjectorAgentDefaults#cpuLimit
        '''
        result = self._values.get("cpu_limit")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cpu_request(self) -> typing.Optional[builtins.str]:
        '''
        :schema: VaultInjectorAgentDefaults#cpuRequest
        '''
        result = self._values.get("cpu_request")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ephemeral_limit(self) -> typing.Optional[builtins.str]:
        '''
        :schema: VaultInjectorAgentDefaults#ephemeralLimit
        '''
        result = self._values.get("ephemeral_limit")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ephemeral_request(self) -> typing.Optional[builtins.str]:
        '''
        :schema: VaultInjectorAgentDefaults#ephemeralRequest
        '''
        result = self._values.get("ephemeral_request")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def mem_limit(self) -> typing.Optional[builtins.str]:
        '''
        :schema: VaultInjectorAgentDefaults#memLimit
        '''
        result = self._values.get("mem_limit")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def mem_request(self) -> typing.Optional[builtins.str]:
        '''
        :schema: VaultInjectorAgentDefaults#memRequest
        '''
        result = self._values.get("mem_request")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def template(self) -> typing.Optional[builtins.str]:
        '''
        :schema: VaultInjectorAgentDefaults#template
        '''
        result = self._values.get("template")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def template_config(
        self,
    ) -> typing.Optional["VaultInjectorAgentDefaultsTemplateConfig"]:
        '''
        :schema: VaultInjectorAgentDefaults#templateConfig
        '''
        result = self._values.get("template_config")
        return typing.cast(typing.Optional["VaultInjectorAgentDefaultsTemplateConfig"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VaultInjectorAgentDefaults(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="vault.VaultInjectorAgentDefaultsTemplateConfig",
    jsii_struct_bases=[],
    name_mapping={
        "additional_values": "additionalValues",
        "exit_on_retry_failure": "exitOnRetryFailure",
        "static_secret_render_interval": "staticSecretRenderInterval",
    },
)
class VaultInjectorAgentDefaultsTemplateConfig:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        exit_on_retry_failure: typing.Optional[builtins.bool] = None,
        static_secret_render_interval: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.
        :param exit_on_retry_failure: 
        :param static_secret_render_interval: 

        :schema: VaultInjectorAgentDefaultsTemplateConfig
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0b695a03fde26ac4adce6f3521db23e50f3690fa72a9382c1e7f675eaaad83c8)
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
            check_type(argname="argument exit_on_retry_failure", value=exit_on_retry_failure, expected_type=type_hints["exit_on_retry_failure"])
            check_type(argname="argument static_secret_render_interval", value=static_secret_render_interval, expected_type=type_hints["static_secret_render_interval"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_values is not None:
            self._values["additional_values"] = additional_values
        if exit_on_retry_failure is not None:
            self._values["exit_on_retry_failure"] = exit_on_retry_failure
        if static_secret_render_interval is not None:
            self._values["static_secret_render_interval"] = static_secret_render_interval

    @builtins.property
    def additional_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: VaultInjectorAgentDefaultsTemplateConfig#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def exit_on_retry_failure(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: VaultInjectorAgentDefaultsTemplateConfig#exitOnRetryFailure
        '''
        result = self._values.get("exit_on_retry_failure")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def static_secret_render_interval(self) -> typing.Optional[builtins.str]:
        '''
        :schema: VaultInjectorAgentDefaultsTemplateConfig#staticSecretRenderInterval
        '''
        result = self._values.get("static_secret_render_interval")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VaultInjectorAgentDefaultsTemplateConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="vault.VaultInjectorAgentImage",
    jsii_struct_bases=[],
    name_mapping={
        "additional_values": "additionalValues",
        "repository": "repository",
        "tag": "tag",
    },
)
class VaultInjectorAgentImage:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        repository: typing.Optional[builtins.str] = None,
        tag: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.
        :param repository: 
        :param tag: 

        :schema: VaultInjectorAgentImage
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__af8a927cb1ea564d82d127069666af1234fe0c65b94f2af0b0d3bd3d4016bc17)
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
            check_type(argname="argument repository", value=repository, expected_type=type_hints["repository"])
            check_type(argname="argument tag", value=tag, expected_type=type_hints["tag"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_values is not None:
            self._values["additional_values"] = additional_values
        if repository is not None:
            self._values["repository"] = repository
        if tag is not None:
            self._values["tag"] = tag

    @builtins.property
    def additional_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: VaultInjectorAgentImage#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def repository(self) -> typing.Optional[builtins.str]:
        '''
        :schema: VaultInjectorAgentImage#repository
        '''
        result = self._values.get("repository")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tag(self) -> typing.Optional[builtins.str]:
        '''
        :schema: VaultInjectorAgentImage#tag
        '''
        result = self._values.get("tag")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VaultInjectorAgentImage(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="vault.VaultInjectorCerts",
    jsii_struct_bases=[],
    name_mapping={
        "additional_values": "additionalValues",
        "ca_bundle": "caBundle",
        "cert_name": "certName",
        "key_name": "keyName",
        "secret_name": "secretName",
    },
)
class VaultInjectorCerts:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        ca_bundle: typing.Optional[builtins.str] = None,
        cert_name: typing.Optional[builtins.str] = None,
        key_name: typing.Optional[builtins.str] = None,
        secret_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.
        :param ca_bundle: 
        :param cert_name: 
        :param key_name: 
        :param secret_name: 

        :schema: VaultInjectorCerts
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__62d62c806a3ca9c6c4fe124a15dc61a274ef728aeec34412374164af440fe54c)
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
            check_type(argname="argument ca_bundle", value=ca_bundle, expected_type=type_hints["ca_bundle"])
            check_type(argname="argument cert_name", value=cert_name, expected_type=type_hints["cert_name"])
            check_type(argname="argument key_name", value=key_name, expected_type=type_hints["key_name"])
            check_type(argname="argument secret_name", value=secret_name, expected_type=type_hints["secret_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_values is not None:
            self._values["additional_values"] = additional_values
        if ca_bundle is not None:
            self._values["ca_bundle"] = ca_bundle
        if cert_name is not None:
            self._values["cert_name"] = cert_name
        if key_name is not None:
            self._values["key_name"] = key_name
        if secret_name is not None:
            self._values["secret_name"] = secret_name

    @builtins.property
    def additional_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: VaultInjectorCerts#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def ca_bundle(self) -> typing.Optional[builtins.str]:
        '''
        :schema: VaultInjectorCerts#caBundle
        '''
        result = self._values.get("ca_bundle")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cert_name(self) -> typing.Optional[builtins.str]:
        '''
        :schema: VaultInjectorCerts#certName
        '''
        result = self._values.get("cert_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def key_name(self) -> typing.Optional[builtins.str]:
        '''
        :schema: VaultInjectorCerts#keyName
        '''
        result = self._values.get("key_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def secret_name(self) -> typing.Optional[builtins.str]:
        '''
        :schema: VaultInjectorCerts#secretName
        '''
        result = self._values.get("secret_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VaultInjectorCerts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="vault.VaultInjectorImage",
    jsii_struct_bases=[],
    name_mapping={
        "additional_values": "additionalValues",
        "pull_policy": "pullPolicy",
        "repository": "repository",
        "tag": "tag",
    },
)
class VaultInjectorImage:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        pull_policy: typing.Optional[builtins.str] = None,
        repository: typing.Optional[builtins.str] = None,
        tag: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.
        :param pull_policy: 
        :param repository: 
        :param tag: 

        :schema: VaultInjectorImage
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__52536a6ddc366ef4a85b18165e1782de1d0d3ee32a4f0931580deb5932989fa5)
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
            check_type(argname="argument pull_policy", value=pull_policy, expected_type=type_hints["pull_policy"])
            check_type(argname="argument repository", value=repository, expected_type=type_hints["repository"])
            check_type(argname="argument tag", value=tag, expected_type=type_hints["tag"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_values is not None:
            self._values["additional_values"] = additional_values
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

        :schema: VaultInjectorImage#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def pull_policy(self) -> typing.Optional[builtins.str]:
        '''
        :schema: VaultInjectorImage#pullPolicy
        '''
        result = self._values.get("pull_policy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def repository(self) -> typing.Optional[builtins.str]:
        '''
        :schema: VaultInjectorImage#repository
        '''
        result = self._values.get("repository")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tag(self) -> typing.Optional[builtins.str]:
        '''
        :schema: VaultInjectorImage#tag
        '''
        result = self._values.get("tag")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VaultInjectorImage(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="vault.VaultInjectorLeaderElector",
    jsii_struct_bases=[],
    name_mapping={"additional_values": "additionalValues", "enabled": "enabled"},
)
class VaultInjectorLeaderElector:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        enabled: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.
        :param enabled: 

        :schema: VaultInjectorLeaderElector
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c6a258c1d4a6af48484adc17c41c686ecc67607f82897b55514535435e5c3c68)
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

        :schema: VaultInjectorLeaderElector#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def enabled(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: VaultInjectorLeaderElector#enabled
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VaultInjectorLeaderElector(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="vault.VaultInjectorLivenessProbe",
    jsii_struct_bases=[],
    name_mapping={
        "additional_values": "additionalValues",
        "failure_threshold": "failureThreshold",
        "initial_delay_seconds": "initialDelaySeconds",
        "period_seconds": "periodSeconds",
        "success_threshold": "successThreshold",
        "timeout_seconds": "timeoutSeconds",
    },
)
class VaultInjectorLivenessProbe:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        failure_threshold: typing.Optional[jsii.Number] = None,
        initial_delay_seconds: typing.Optional[jsii.Number] = None,
        period_seconds: typing.Optional[jsii.Number] = None,
        success_threshold: typing.Optional[jsii.Number] = None,
        timeout_seconds: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.
        :param failure_threshold: 
        :param initial_delay_seconds: 
        :param period_seconds: 
        :param success_threshold: 
        :param timeout_seconds: 

        :schema: VaultInjectorLivenessProbe
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2e4c4da16af46227522996a8354af8ae5d2b75c3b783771c5f46c3ac673b94cd)
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
            check_type(argname="argument failure_threshold", value=failure_threshold, expected_type=type_hints["failure_threshold"])
            check_type(argname="argument initial_delay_seconds", value=initial_delay_seconds, expected_type=type_hints["initial_delay_seconds"])
            check_type(argname="argument period_seconds", value=period_seconds, expected_type=type_hints["period_seconds"])
            check_type(argname="argument success_threshold", value=success_threshold, expected_type=type_hints["success_threshold"])
            check_type(argname="argument timeout_seconds", value=timeout_seconds, expected_type=type_hints["timeout_seconds"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_values is not None:
            self._values["additional_values"] = additional_values
        if failure_threshold is not None:
            self._values["failure_threshold"] = failure_threshold
        if initial_delay_seconds is not None:
            self._values["initial_delay_seconds"] = initial_delay_seconds
        if period_seconds is not None:
            self._values["period_seconds"] = period_seconds
        if success_threshold is not None:
            self._values["success_threshold"] = success_threshold
        if timeout_seconds is not None:
            self._values["timeout_seconds"] = timeout_seconds

    @builtins.property
    def additional_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: VaultInjectorLivenessProbe#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def failure_threshold(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: VaultInjectorLivenessProbe#failureThreshold
        '''
        result = self._values.get("failure_threshold")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def initial_delay_seconds(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: VaultInjectorLivenessProbe#initialDelaySeconds
        '''
        result = self._values.get("initial_delay_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def period_seconds(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: VaultInjectorLivenessProbe#periodSeconds
        '''
        result = self._values.get("period_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def success_threshold(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: VaultInjectorLivenessProbe#successThreshold
        '''
        result = self._values.get("success_threshold")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def timeout_seconds(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: VaultInjectorLivenessProbe#timeoutSeconds
        '''
        result = self._values.get("timeout_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VaultInjectorLivenessProbe(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="vault.VaultInjectorMetrics",
    jsii_struct_bases=[],
    name_mapping={"additional_values": "additionalValues", "enabled": "enabled"},
)
class VaultInjectorMetrics:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        enabled: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.
        :param enabled: 

        :schema: VaultInjectorMetrics
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1653b9a00c4aff25d127c12173f92606f0259c1ad17cc2944057b0ad395f2b75)
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

        :schema: VaultInjectorMetrics#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def enabled(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: VaultInjectorMetrics#enabled
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VaultInjectorMetrics(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="vault.VaultInjectorReadinessProbe",
    jsii_struct_bases=[],
    name_mapping={
        "additional_values": "additionalValues",
        "failure_threshold": "failureThreshold",
        "initial_delay_seconds": "initialDelaySeconds",
        "period_seconds": "periodSeconds",
        "success_threshold": "successThreshold",
        "timeout_seconds": "timeoutSeconds",
    },
)
class VaultInjectorReadinessProbe:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        failure_threshold: typing.Optional[jsii.Number] = None,
        initial_delay_seconds: typing.Optional[jsii.Number] = None,
        period_seconds: typing.Optional[jsii.Number] = None,
        success_threshold: typing.Optional[jsii.Number] = None,
        timeout_seconds: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.
        :param failure_threshold: 
        :param initial_delay_seconds: 
        :param period_seconds: 
        :param success_threshold: 
        :param timeout_seconds: 

        :schema: VaultInjectorReadinessProbe
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fcd88cdfeb775e3076ee4a8865d9dfba0bb474e43b3eb4d8a8c9e8c4c3f68104)
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
            check_type(argname="argument failure_threshold", value=failure_threshold, expected_type=type_hints["failure_threshold"])
            check_type(argname="argument initial_delay_seconds", value=initial_delay_seconds, expected_type=type_hints["initial_delay_seconds"])
            check_type(argname="argument period_seconds", value=period_seconds, expected_type=type_hints["period_seconds"])
            check_type(argname="argument success_threshold", value=success_threshold, expected_type=type_hints["success_threshold"])
            check_type(argname="argument timeout_seconds", value=timeout_seconds, expected_type=type_hints["timeout_seconds"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_values is not None:
            self._values["additional_values"] = additional_values
        if failure_threshold is not None:
            self._values["failure_threshold"] = failure_threshold
        if initial_delay_seconds is not None:
            self._values["initial_delay_seconds"] = initial_delay_seconds
        if period_seconds is not None:
            self._values["period_seconds"] = period_seconds
        if success_threshold is not None:
            self._values["success_threshold"] = success_threshold
        if timeout_seconds is not None:
            self._values["timeout_seconds"] = timeout_seconds

    @builtins.property
    def additional_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: VaultInjectorReadinessProbe#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def failure_threshold(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: VaultInjectorReadinessProbe#failureThreshold
        '''
        result = self._values.get("failure_threshold")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def initial_delay_seconds(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: VaultInjectorReadinessProbe#initialDelaySeconds
        '''
        result = self._values.get("initial_delay_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def period_seconds(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: VaultInjectorReadinessProbe#periodSeconds
        '''
        result = self._values.get("period_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def success_threshold(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: VaultInjectorReadinessProbe#successThreshold
        '''
        result = self._values.get("success_threshold")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def timeout_seconds(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: VaultInjectorReadinessProbe#timeoutSeconds
        '''
        result = self._values.get("timeout_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VaultInjectorReadinessProbe(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="vault.VaultInjectorSecurityContext",
    jsii_struct_bases=[],
    name_mapping={
        "additional_values": "additionalValues",
        "container": "container",
        "pod": "pod",
    },
)
class VaultInjectorSecurityContext:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        container: typing.Any = None,
        pod: typing.Any = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.
        :param container: 
        :param pod: 

        :schema: VaultInjectorSecurityContext
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__93682a70d7ea342aa58eb8fc794987c419d207779748cd3b9dca833af6a4d9a9)
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
            check_type(argname="argument container", value=container, expected_type=type_hints["container"])
            check_type(argname="argument pod", value=pod, expected_type=type_hints["pod"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_values is not None:
            self._values["additional_values"] = additional_values
        if container is not None:
            self._values["container"] = container
        if pod is not None:
            self._values["pod"] = pod

    @builtins.property
    def additional_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: VaultInjectorSecurityContext#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def container(self) -> typing.Any:
        '''
        :schema: VaultInjectorSecurityContext#container
        '''
        result = self._values.get("container")
        return typing.cast(typing.Any, result)

    @builtins.property
    def pod(self) -> typing.Any:
        '''
        :schema: VaultInjectorSecurityContext#pod
        '''
        result = self._values.get("pod")
        return typing.cast(typing.Any, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VaultInjectorSecurityContext(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="vault.VaultInjectorService",
    jsii_struct_bases=[],
    name_mapping={
        "additional_values": "additionalValues",
        "annotations": "annotations",
    },
)
class VaultInjectorService:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        annotations: typing.Any = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.
        :param annotations: 

        :schema: VaultInjectorService
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5d074e28fdcd505c535aede327d5b429aaa337a41f1f69f1f57b942363357d73)
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
            check_type(argname="argument annotations", value=annotations, expected_type=type_hints["annotations"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_values is not None:
            self._values["additional_values"] = additional_values
        if annotations is not None:
            self._values["annotations"] = annotations

    @builtins.property
    def additional_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: VaultInjectorService#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def annotations(self) -> typing.Any:
        '''
        :schema: VaultInjectorService#annotations
        '''
        result = self._values.get("annotations")
        return typing.cast(typing.Any, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VaultInjectorService(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="vault.VaultInjectorServiceAccount",
    jsii_struct_bases=[],
    name_mapping={
        "additional_values": "additionalValues",
        "annotations": "annotations",
    },
)
class VaultInjectorServiceAccount:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        annotations: typing.Any = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.
        :param annotations: 

        :schema: VaultInjectorServiceAccount
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b1e932448512bbaad52eb94420530e86d4be7ae06c4e32c3325c31b098b59d67)
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
            check_type(argname="argument annotations", value=annotations, expected_type=type_hints["annotations"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_values is not None:
            self._values["additional_values"] = additional_values
        if annotations is not None:
            self._values["annotations"] = annotations

    @builtins.property
    def additional_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: VaultInjectorServiceAccount#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def annotations(self) -> typing.Any:
        '''
        :schema: VaultInjectorServiceAccount#annotations
        '''
        result = self._values.get("annotations")
        return typing.cast(typing.Any, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VaultInjectorServiceAccount(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="vault.VaultInjectorStartupProbe",
    jsii_struct_bases=[],
    name_mapping={
        "additional_values": "additionalValues",
        "failure_threshold": "failureThreshold",
        "initial_delay_seconds": "initialDelaySeconds",
        "period_seconds": "periodSeconds",
        "success_threshold": "successThreshold",
        "timeout_seconds": "timeoutSeconds",
    },
)
class VaultInjectorStartupProbe:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        failure_threshold: typing.Optional[jsii.Number] = None,
        initial_delay_seconds: typing.Optional[jsii.Number] = None,
        period_seconds: typing.Optional[jsii.Number] = None,
        success_threshold: typing.Optional[jsii.Number] = None,
        timeout_seconds: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.
        :param failure_threshold: 
        :param initial_delay_seconds: 
        :param period_seconds: 
        :param success_threshold: 
        :param timeout_seconds: 

        :schema: VaultInjectorStartupProbe
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3d99800e278ee9172c01b656f46a1897ac953c43ea5e73b96df606c202018a69)
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
            check_type(argname="argument failure_threshold", value=failure_threshold, expected_type=type_hints["failure_threshold"])
            check_type(argname="argument initial_delay_seconds", value=initial_delay_seconds, expected_type=type_hints["initial_delay_seconds"])
            check_type(argname="argument period_seconds", value=period_seconds, expected_type=type_hints["period_seconds"])
            check_type(argname="argument success_threshold", value=success_threshold, expected_type=type_hints["success_threshold"])
            check_type(argname="argument timeout_seconds", value=timeout_seconds, expected_type=type_hints["timeout_seconds"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_values is not None:
            self._values["additional_values"] = additional_values
        if failure_threshold is not None:
            self._values["failure_threshold"] = failure_threshold
        if initial_delay_seconds is not None:
            self._values["initial_delay_seconds"] = initial_delay_seconds
        if period_seconds is not None:
            self._values["period_seconds"] = period_seconds
        if success_threshold is not None:
            self._values["success_threshold"] = success_threshold
        if timeout_seconds is not None:
            self._values["timeout_seconds"] = timeout_seconds

    @builtins.property
    def additional_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: VaultInjectorStartupProbe#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def failure_threshold(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: VaultInjectorStartupProbe#failureThreshold
        '''
        result = self._values.get("failure_threshold")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def initial_delay_seconds(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: VaultInjectorStartupProbe#initialDelaySeconds
        '''
        result = self._values.get("initial_delay_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def period_seconds(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: VaultInjectorStartupProbe#periodSeconds
        '''
        result = self._values.get("period_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def success_threshold(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: VaultInjectorStartupProbe#successThreshold
        '''
        result = self._values.get("success_threshold")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def timeout_seconds(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: VaultInjectorStartupProbe#timeoutSeconds
        '''
        result = self._values.get("timeout_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VaultInjectorStartupProbe(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="vault.VaultInjectorWebhook",
    jsii_struct_bases=[],
    name_mapping={
        "additional_values": "additionalValues",
        "annotations": "annotations",
        "failure_policy": "failurePolicy",
        "match_policy": "matchPolicy",
        "namespace_selector": "namespaceSelector",
        "object_selector": "objectSelector",
        "timeout_seconds": "timeoutSeconds",
    },
)
class VaultInjectorWebhook:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        annotations: typing.Any = None,
        failure_policy: typing.Optional[builtins.str] = None,
        match_policy: typing.Optional[builtins.str] = None,
        namespace_selector: typing.Any = None,
        object_selector: typing.Any = None,
        timeout_seconds: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.
        :param annotations: 
        :param failure_policy: 
        :param match_policy: 
        :param namespace_selector: 
        :param object_selector: 
        :param timeout_seconds: 

        :schema: VaultInjectorWebhook
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5eefdf91d97ff96a44dae7a3d9bf3e8813e821227a2359e3ecda1fcb0470040b)
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
            check_type(argname="argument annotations", value=annotations, expected_type=type_hints["annotations"])
            check_type(argname="argument failure_policy", value=failure_policy, expected_type=type_hints["failure_policy"])
            check_type(argname="argument match_policy", value=match_policy, expected_type=type_hints["match_policy"])
            check_type(argname="argument namespace_selector", value=namespace_selector, expected_type=type_hints["namespace_selector"])
            check_type(argname="argument object_selector", value=object_selector, expected_type=type_hints["object_selector"])
            check_type(argname="argument timeout_seconds", value=timeout_seconds, expected_type=type_hints["timeout_seconds"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_values is not None:
            self._values["additional_values"] = additional_values
        if annotations is not None:
            self._values["annotations"] = annotations
        if failure_policy is not None:
            self._values["failure_policy"] = failure_policy
        if match_policy is not None:
            self._values["match_policy"] = match_policy
        if namespace_selector is not None:
            self._values["namespace_selector"] = namespace_selector
        if object_selector is not None:
            self._values["object_selector"] = object_selector
        if timeout_seconds is not None:
            self._values["timeout_seconds"] = timeout_seconds

    @builtins.property
    def additional_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: VaultInjectorWebhook#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def annotations(self) -> typing.Any:
        '''
        :schema: VaultInjectorWebhook#annotations
        '''
        result = self._values.get("annotations")
        return typing.cast(typing.Any, result)

    @builtins.property
    def failure_policy(self) -> typing.Optional[builtins.str]:
        '''
        :schema: VaultInjectorWebhook#failurePolicy
        '''
        result = self._values.get("failure_policy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def match_policy(self) -> typing.Optional[builtins.str]:
        '''
        :schema: VaultInjectorWebhook#matchPolicy
        '''
        result = self._values.get("match_policy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def namespace_selector(self) -> typing.Any:
        '''
        :schema: VaultInjectorWebhook#namespaceSelector
        '''
        result = self._values.get("namespace_selector")
        return typing.cast(typing.Any, result)

    @builtins.property
    def object_selector(self) -> typing.Any:
        '''
        :schema: VaultInjectorWebhook#objectSelector
        '''
        result = self._values.get("object_selector")
        return typing.cast(typing.Any, result)

    @builtins.property
    def timeout_seconds(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: VaultInjectorWebhook#timeoutSeconds
        '''
        result = self._values.get("timeout_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VaultInjectorWebhook(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="vault.VaultProps",
    jsii_struct_bases=[],
    name_mapping={
        "helm_executable": "helmExecutable",
        "helm_flags": "helmFlags",
        "namespace": "namespace",
        "release_name": "releaseName",
        "values": "values",
    },
)
class VaultProps:
    def __init__(
        self,
        *,
        helm_executable: typing.Optional[builtins.str] = None,
        helm_flags: typing.Optional[typing.Sequence[builtins.str]] = None,
        namespace: typing.Optional[builtins.str] = None,
        release_name: typing.Optional[builtins.str] = None,
        values: typing.Optional[typing.Union["VaultValues", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param helm_executable: -
        :param helm_flags: -
        :param namespace: -
        :param release_name: -
        :param values: -
        '''
        if isinstance(values, dict):
            values = VaultValues(**values)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3516748a8734cf1c44155b30bbfa1b0d45edd6e8cd28d2feaf6c783d30b654a2)
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
    def values(self) -> typing.Optional["VaultValues"]:
        result = self._values.get("values")
        return typing.cast(typing.Optional["VaultValues"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VaultProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="vault.VaultServer",
    jsii_struct_bases=[],
    name_mapping={
        "additional_values": "additionalValues",
        "affinity": "affinity",
        "annotations": "annotations",
        "audit_storage": "auditStorage",
        "auth_delegator": "authDelegator",
        "data_storage": "dataStorage",
        "dev": "dev",
        "enabled": "enabled",
        "enterprise_license": "enterpriseLicense",
        "extra_args": "extraArgs",
        "extra_containers": "extraContainers",
        "extra_environment_vars": "extraEnvironmentVars",
        "extra_init_containers": "extraInitContainers",
        "extra_labels": "extraLabels",
        "extra_ports": "extraPorts",
        "extra_secret_environment_vars": "extraSecretEnvironmentVars",
        "extra_volumes": "extraVolumes",
        "ha": "ha",
        "host_aliases": "hostAliases",
        "host_network": "hostNetwork",
        "image": "image",
        "include_config_annotation": "includeConfigAnnotation",
        "ingress": "ingress",
        "liveness_probe": "livenessProbe",
        "log_format": "logFormat",
        "log_level": "logLevel",
        "network_policy": "networkPolicy",
        "node_selector": "nodeSelector",
        "persistent_volume_claim_retention_policy": "persistentVolumeClaimRetentionPolicy",
        "post_start": "postStart",
        "pre_stop_sleep_seconds": "preStopSleepSeconds",
        "priority_class_name": "priorityClassName",
        "readiness_probe": "readinessProbe",
        "resources": "resources",
        "route": "route",
        "service": "service",
        "service_account": "serviceAccount",
        "share_process_namespace": "shareProcessNamespace",
        "standalone": "standalone",
        "stateful_set": "statefulSet",
        "termination_grace_period_seconds": "terminationGracePeriodSeconds",
        "tolerations": "tolerations",
        "topology_spread_constraints": "topologySpreadConstraints",
        "update_strategy_type": "updateStrategyType",
        "volume_mounts": "volumeMounts",
        "volumes": "volumes",
    },
)
class VaultServer:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        affinity: typing.Any = None,
        annotations: typing.Any = None,
        audit_storage: typing.Optional[typing.Union["VaultServerAuditStorage", typing.Dict[builtins.str, typing.Any]]] = None,
        auth_delegator: typing.Optional[typing.Union["VaultServerAuthDelegator", typing.Dict[builtins.str, typing.Any]]] = None,
        data_storage: typing.Optional[typing.Union["VaultServerDataStorage", typing.Dict[builtins.str, typing.Any]]] = None,
        dev: typing.Optional[typing.Union["VaultServerDev", typing.Dict[builtins.str, typing.Any]]] = None,
        enabled: typing.Any = None,
        enterprise_license: typing.Optional[typing.Union["VaultServerEnterpriseLicense", typing.Dict[builtins.str, typing.Any]]] = None,
        extra_args: typing.Optional[builtins.str] = None,
        extra_containers: typing.Optional[typing.Sequence[typing.Any]] = None,
        extra_environment_vars: typing.Any = None,
        extra_init_containers: typing.Optional[typing.Sequence[typing.Any]] = None,
        extra_labels: typing.Any = None,
        extra_ports: typing.Optional[typing.Sequence[typing.Any]] = None,
        extra_secret_environment_vars: typing.Optional[typing.Sequence[typing.Any]] = None,
        extra_volumes: typing.Optional[typing.Sequence[typing.Any]] = None,
        ha: typing.Optional[typing.Union["VaultServerHa", typing.Dict[builtins.str, typing.Any]]] = None,
        host_aliases: typing.Optional[typing.Sequence[typing.Any]] = None,
        host_network: typing.Optional[builtins.bool] = None,
        image: typing.Optional[typing.Union["VaultServerImage", typing.Dict[builtins.str, typing.Any]]] = None,
        include_config_annotation: typing.Optional[builtins.bool] = None,
        ingress: typing.Optional[typing.Union["VaultServerIngress", typing.Dict[builtins.str, typing.Any]]] = None,
        liveness_probe: typing.Optional[typing.Union["VaultServerLivenessProbe", typing.Dict[builtins.str, typing.Any]]] = None,
        log_format: typing.Optional[builtins.str] = None,
        log_level: typing.Optional[builtins.str] = None,
        network_policy: typing.Optional[typing.Union["VaultServerNetworkPolicy", typing.Dict[builtins.str, typing.Any]]] = None,
        node_selector: typing.Any = None,
        persistent_volume_claim_retention_policy: typing.Optional[typing.Union["VaultServerPersistentVolumeClaimRetentionPolicy", typing.Dict[builtins.str, typing.Any]]] = None,
        post_start: typing.Optional[typing.Sequence[typing.Any]] = None,
        pre_stop_sleep_seconds: typing.Optional[jsii.Number] = None,
        priority_class_name: typing.Optional[builtins.str] = None,
        readiness_probe: typing.Optional[typing.Union["VaultServerReadinessProbe", typing.Dict[builtins.str, typing.Any]]] = None,
        resources: typing.Any = None,
        route: typing.Optional[typing.Union["VaultServerRoute", typing.Dict[builtins.str, typing.Any]]] = None,
        service: typing.Optional[typing.Union["VaultServerService", typing.Dict[builtins.str, typing.Any]]] = None,
        service_account: typing.Optional[typing.Union["VaultServerServiceAccount", typing.Dict[builtins.str, typing.Any]]] = None,
        share_process_namespace: typing.Optional[builtins.bool] = None,
        standalone: typing.Optional[typing.Union["VaultServerStandalone", typing.Dict[builtins.str, typing.Any]]] = None,
        stateful_set: typing.Optional[typing.Union["VaultServerStatefulSet", typing.Dict[builtins.str, typing.Any]]] = None,
        termination_grace_period_seconds: typing.Optional[jsii.Number] = None,
        tolerations: typing.Any = None,
        topology_spread_constraints: typing.Any = None,
        update_strategy_type: typing.Optional[builtins.str] = None,
        volume_mounts: typing.Optional[typing.Sequence[typing.Any]] = None,
        volumes: typing.Optional[typing.Sequence[typing.Any]] = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.
        :param affinity: 
        :param annotations: 
        :param audit_storage: 
        :param auth_delegator: 
        :param data_storage: 
        :param dev: 
        :param enabled: 
        :param enterprise_license: 
        :param extra_args: 
        :param extra_containers: 
        :param extra_environment_vars: 
        :param extra_init_containers: 
        :param extra_labels: 
        :param extra_ports: 
        :param extra_secret_environment_vars: 
        :param extra_volumes: 
        :param ha: 
        :param host_aliases: 
        :param host_network: 
        :param image: 
        :param include_config_annotation: 
        :param ingress: 
        :param liveness_probe: 
        :param log_format: 
        :param log_level: 
        :param network_policy: 
        :param node_selector: 
        :param persistent_volume_claim_retention_policy: 
        :param post_start: 
        :param pre_stop_sleep_seconds: 
        :param priority_class_name: 
        :param readiness_probe: 
        :param resources: 
        :param route: 
        :param service: 
        :param service_account: 
        :param share_process_namespace: 
        :param standalone: 
        :param stateful_set: 
        :param termination_grace_period_seconds: 
        :param tolerations: 
        :param topology_spread_constraints: 
        :param update_strategy_type: 
        :param volume_mounts: 
        :param volumes: 

        :schema: VaultServer
        '''
        if isinstance(audit_storage, dict):
            audit_storage = VaultServerAuditStorage(**audit_storage)
        if isinstance(auth_delegator, dict):
            auth_delegator = VaultServerAuthDelegator(**auth_delegator)
        if isinstance(data_storage, dict):
            data_storage = VaultServerDataStorage(**data_storage)
        if isinstance(dev, dict):
            dev = VaultServerDev(**dev)
        if isinstance(enterprise_license, dict):
            enterprise_license = VaultServerEnterpriseLicense(**enterprise_license)
        if isinstance(ha, dict):
            ha = VaultServerHa(**ha)
        if isinstance(image, dict):
            image = VaultServerImage(**image)
        if isinstance(ingress, dict):
            ingress = VaultServerIngress(**ingress)
        if isinstance(liveness_probe, dict):
            liveness_probe = VaultServerLivenessProbe(**liveness_probe)
        if isinstance(network_policy, dict):
            network_policy = VaultServerNetworkPolicy(**network_policy)
        if isinstance(persistent_volume_claim_retention_policy, dict):
            persistent_volume_claim_retention_policy = VaultServerPersistentVolumeClaimRetentionPolicy(**persistent_volume_claim_retention_policy)
        if isinstance(readiness_probe, dict):
            readiness_probe = VaultServerReadinessProbe(**readiness_probe)
        if isinstance(route, dict):
            route = VaultServerRoute(**route)
        if isinstance(service, dict):
            service = VaultServerService(**service)
        if isinstance(service_account, dict):
            service_account = VaultServerServiceAccount(**service_account)
        if isinstance(standalone, dict):
            standalone = VaultServerStandalone(**standalone)
        if isinstance(stateful_set, dict):
            stateful_set = VaultServerStatefulSet(**stateful_set)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bb5c6e8fee72dc5d759f67b5f13f2dbc50f027bbcf46286412f7ff8e16a1a726)
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
            check_type(argname="argument affinity", value=affinity, expected_type=type_hints["affinity"])
            check_type(argname="argument annotations", value=annotations, expected_type=type_hints["annotations"])
            check_type(argname="argument audit_storage", value=audit_storage, expected_type=type_hints["audit_storage"])
            check_type(argname="argument auth_delegator", value=auth_delegator, expected_type=type_hints["auth_delegator"])
            check_type(argname="argument data_storage", value=data_storage, expected_type=type_hints["data_storage"])
            check_type(argname="argument dev", value=dev, expected_type=type_hints["dev"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument enterprise_license", value=enterprise_license, expected_type=type_hints["enterprise_license"])
            check_type(argname="argument extra_args", value=extra_args, expected_type=type_hints["extra_args"])
            check_type(argname="argument extra_containers", value=extra_containers, expected_type=type_hints["extra_containers"])
            check_type(argname="argument extra_environment_vars", value=extra_environment_vars, expected_type=type_hints["extra_environment_vars"])
            check_type(argname="argument extra_init_containers", value=extra_init_containers, expected_type=type_hints["extra_init_containers"])
            check_type(argname="argument extra_labels", value=extra_labels, expected_type=type_hints["extra_labels"])
            check_type(argname="argument extra_ports", value=extra_ports, expected_type=type_hints["extra_ports"])
            check_type(argname="argument extra_secret_environment_vars", value=extra_secret_environment_vars, expected_type=type_hints["extra_secret_environment_vars"])
            check_type(argname="argument extra_volumes", value=extra_volumes, expected_type=type_hints["extra_volumes"])
            check_type(argname="argument ha", value=ha, expected_type=type_hints["ha"])
            check_type(argname="argument host_aliases", value=host_aliases, expected_type=type_hints["host_aliases"])
            check_type(argname="argument host_network", value=host_network, expected_type=type_hints["host_network"])
            check_type(argname="argument image", value=image, expected_type=type_hints["image"])
            check_type(argname="argument include_config_annotation", value=include_config_annotation, expected_type=type_hints["include_config_annotation"])
            check_type(argname="argument ingress", value=ingress, expected_type=type_hints["ingress"])
            check_type(argname="argument liveness_probe", value=liveness_probe, expected_type=type_hints["liveness_probe"])
            check_type(argname="argument log_format", value=log_format, expected_type=type_hints["log_format"])
            check_type(argname="argument log_level", value=log_level, expected_type=type_hints["log_level"])
            check_type(argname="argument network_policy", value=network_policy, expected_type=type_hints["network_policy"])
            check_type(argname="argument node_selector", value=node_selector, expected_type=type_hints["node_selector"])
            check_type(argname="argument persistent_volume_claim_retention_policy", value=persistent_volume_claim_retention_policy, expected_type=type_hints["persistent_volume_claim_retention_policy"])
            check_type(argname="argument post_start", value=post_start, expected_type=type_hints["post_start"])
            check_type(argname="argument pre_stop_sleep_seconds", value=pre_stop_sleep_seconds, expected_type=type_hints["pre_stop_sleep_seconds"])
            check_type(argname="argument priority_class_name", value=priority_class_name, expected_type=type_hints["priority_class_name"])
            check_type(argname="argument readiness_probe", value=readiness_probe, expected_type=type_hints["readiness_probe"])
            check_type(argname="argument resources", value=resources, expected_type=type_hints["resources"])
            check_type(argname="argument route", value=route, expected_type=type_hints["route"])
            check_type(argname="argument service", value=service, expected_type=type_hints["service"])
            check_type(argname="argument service_account", value=service_account, expected_type=type_hints["service_account"])
            check_type(argname="argument share_process_namespace", value=share_process_namespace, expected_type=type_hints["share_process_namespace"])
            check_type(argname="argument standalone", value=standalone, expected_type=type_hints["standalone"])
            check_type(argname="argument stateful_set", value=stateful_set, expected_type=type_hints["stateful_set"])
            check_type(argname="argument termination_grace_period_seconds", value=termination_grace_period_seconds, expected_type=type_hints["termination_grace_period_seconds"])
            check_type(argname="argument tolerations", value=tolerations, expected_type=type_hints["tolerations"])
            check_type(argname="argument topology_spread_constraints", value=topology_spread_constraints, expected_type=type_hints["topology_spread_constraints"])
            check_type(argname="argument update_strategy_type", value=update_strategy_type, expected_type=type_hints["update_strategy_type"])
            check_type(argname="argument volume_mounts", value=volume_mounts, expected_type=type_hints["volume_mounts"])
            check_type(argname="argument volumes", value=volumes, expected_type=type_hints["volumes"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_values is not None:
            self._values["additional_values"] = additional_values
        if affinity is not None:
            self._values["affinity"] = affinity
        if annotations is not None:
            self._values["annotations"] = annotations
        if audit_storage is not None:
            self._values["audit_storage"] = audit_storage
        if auth_delegator is not None:
            self._values["auth_delegator"] = auth_delegator
        if data_storage is not None:
            self._values["data_storage"] = data_storage
        if dev is not None:
            self._values["dev"] = dev
        if enabled is not None:
            self._values["enabled"] = enabled
        if enterprise_license is not None:
            self._values["enterprise_license"] = enterprise_license
        if extra_args is not None:
            self._values["extra_args"] = extra_args
        if extra_containers is not None:
            self._values["extra_containers"] = extra_containers
        if extra_environment_vars is not None:
            self._values["extra_environment_vars"] = extra_environment_vars
        if extra_init_containers is not None:
            self._values["extra_init_containers"] = extra_init_containers
        if extra_labels is not None:
            self._values["extra_labels"] = extra_labels
        if extra_ports is not None:
            self._values["extra_ports"] = extra_ports
        if extra_secret_environment_vars is not None:
            self._values["extra_secret_environment_vars"] = extra_secret_environment_vars
        if extra_volumes is not None:
            self._values["extra_volumes"] = extra_volumes
        if ha is not None:
            self._values["ha"] = ha
        if host_aliases is not None:
            self._values["host_aliases"] = host_aliases
        if host_network is not None:
            self._values["host_network"] = host_network
        if image is not None:
            self._values["image"] = image
        if include_config_annotation is not None:
            self._values["include_config_annotation"] = include_config_annotation
        if ingress is not None:
            self._values["ingress"] = ingress
        if liveness_probe is not None:
            self._values["liveness_probe"] = liveness_probe
        if log_format is not None:
            self._values["log_format"] = log_format
        if log_level is not None:
            self._values["log_level"] = log_level
        if network_policy is not None:
            self._values["network_policy"] = network_policy
        if node_selector is not None:
            self._values["node_selector"] = node_selector
        if persistent_volume_claim_retention_policy is not None:
            self._values["persistent_volume_claim_retention_policy"] = persistent_volume_claim_retention_policy
        if post_start is not None:
            self._values["post_start"] = post_start
        if pre_stop_sleep_seconds is not None:
            self._values["pre_stop_sleep_seconds"] = pre_stop_sleep_seconds
        if priority_class_name is not None:
            self._values["priority_class_name"] = priority_class_name
        if readiness_probe is not None:
            self._values["readiness_probe"] = readiness_probe
        if resources is not None:
            self._values["resources"] = resources
        if route is not None:
            self._values["route"] = route
        if service is not None:
            self._values["service"] = service
        if service_account is not None:
            self._values["service_account"] = service_account
        if share_process_namespace is not None:
            self._values["share_process_namespace"] = share_process_namespace
        if standalone is not None:
            self._values["standalone"] = standalone
        if stateful_set is not None:
            self._values["stateful_set"] = stateful_set
        if termination_grace_period_seconds is not None:
            self._values["termination_grace_period_seconds"] = termination_grace_period_seconds
        if tolerations is not None:
            self._values["tolerations"] = tolerations
        if topology_spread_constraints is not None:
            self._values["topology_spread_constraints"] = topology_spread_constraints
        if update_strategy_type is not None:
            self._values["update_strategy_type"] = update_strategy_type
        if volume_mounts is not None:
            self._values["volume_mounts"] = volume_mounts
        if volumes is not None:
            self._values["volumes"] = volumes

    @builtins.property
    def additional_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: VaultServer#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def affinity(self) -> typing.Any:
        '''
        :schema: VaultServer#affinity
        '''
        result = self._values.get("affinity")
        return typing.cast(typing.Any, result)

    @builtins.property
    def annotations(self) -> typing.Any:
        '''
        :schema: VaultServer#annotations
        '''
        result = self._values.get("annotations")
        return typing.cast(typing.Any, result)

    @builtins.property
    def audit_storage(self) -> typing.Optional["VaultServerAuditStorage"]:
        '''
        :schema: VaultServer#auditStorage
        '''
        result = self._values.get("audit_storage")
        return typing.cast(typing.Optional["VaultServerAuditStorage"], result)

    @builtins.property
    def auth_delegator(self) -> typing.Optional["VaultServerAuthDelegator"]:
        '''
        :schema: VaultServer#authDelegator
        '''
        result = self._values.get("auth_delegator")
        return typing.cast(typing.Optional["VaultServerAuthDelegator"], result)

    @builtins.property
    def data_storage(self) -> typing.Optional["VaultServerDataStorage"]:
        '''
        :schema: VaultServer#dataStorage
        '''
        result = self._values.get("data_storage")
        return typing.cast(typing.Optional["VaultServerDataStorage"], result)

    @builtins.property
    def dev(self) -> typing.Optional["VaultServerDev"]:
        '''
        :schema: VaultServer#dev
        '''
        result = self._values.get("dev")
        return typing.cast(typing.Optional["VaultServerDev"], result)

    @builtins.property
    def enabled(self) -> typing.Any:
        '''
        :schema: VaultServer#enabled
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Any, result)

    @builtins.property
    def enterprise_license(self) -> typing.Optional["VaultServerEnterpriseLicense"]:
        '''
        :schema: VaultServer#enterpriseLicense
        '''
        result = self._values.get("enterprise_license")
        return typing.cast(typing.Optional["VaultServerEnterpriseLicense"], result)

    @builtins.property
    def extra_args(self) -> typing.Optional[builtins.str]:
        '''
        :schema: VaultServer#extraArgs
        '''
        result = self._values.get("extra_args")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def extra_containers(self) -> typing.Optional[typing.List[typing.Any]]:
        '''
        :schema: VaultServer#extraContainers
        '''
        result = self._values.get("extra_containers")
        return typing.cast(typing.Optional[typing.List[typing.Any]], result)

    @builtins.property
    def extra_environment_vars(self) -> typing.Any:
        '''
        :schema: VaultServer#extraEnvironmentVars
        '''
        result = self._values.get("extra_environment_vars")
        return typing.cast(typing.Any, result)

    @builtins.property
    def extra_init_containers(self) -> typing.Optional[typing.List[typing.Any]]:
        '''
        :schema: VaultServer#extraInitContainers
        '''
        result = self._values.get("extra_init_containers")
        return typing.cast(typing.Optional[typing.List[typing.Any]], result)

    @builtins.property
    def extra_labels(self) -> typing.Any:
        '''
        :schema: VaultServer#extraLabels
        '''
        result = self._values.get("extra_labels")
        return typing.cast(typing.Any, result)

    @builtins.property
    def extra_ports(self) -> typing.Optional[typing.List[typing.Any]]:
        '''
        :schema: VaultServer#extraPorts
        '''
        result = self._values.get("extra_ports")
        return typing.cast(typing.Optional[typing.List[typing.Any]], result)

    @builtins.property
    def extra_secret_environment_vars(self) -> typing.Optional[typing.List[typing.Any]]:
        '''
        :schema: VaultServer#extraSecretEnvironmentVars
        '''
        result = self._values.get("extra_secret_environment_vars")
        return typing.cast(typing.Optional[typing.List[typing.Any]], result)

    @builtins.property
    def extra_volumes(self) -> typing.Optional[typing.List[typing.Any]]:
        '''
        :schema: VaultServer#extraVolumes
        '''
        result = self._values.get("extra_volumes")
        return typing.cast(typing.Optional[typing.List[typing.Any]], result)

    @builtins.property
    def ha(self) -> typing.Optional["VaultServerHa"]:
        '''
        :schema: VaultServer#ha
        '''
        result = self._values.get("ha")
        return typing.cast(typing.Optional["VaultServerHa"], result)

    @builtins.property
    def host_aliases(self) -> typing.Optional[typing.List[typing.Any]]:
        '''
        :schema: VaultServer#hostAliases
        '''
        result = self._values.get("host_aliases")
        return typing.cast(typing.Optional[typing.List[typing.Any]], result)

    @builtins.property
    def host_network(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: VaultServer#hostNetwork
        '''
        result = self._values.get("host_network")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def image(self) -> typing.Optional["VaultServerImage"]:
        '''
        :schema: VaultServer#image
        '''
        result = self._values.get("image")
        return typing.cast(typing.Optional["VaultServerImage"], result)

    @builtins.property
    def include_config_annotation(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: VaultServer#includeConfigAnnotation
        '''
        result = self._values.get("include_config_annotation")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def ingress(self) -> typing.Optional["VaultServerIngress"]:
        '''
        :schema: VaultServer#ingress
        '''
        result = self._values.get("ingress")
        return typing.cast(typing.Optional["VaultServerIngress"], result)

    @builtins.property
    def liveness_probe(self) -> typing.Optional["VaultServerLivenessProbe"]:
        '''
        :schema: VaultServer#livenessProbe
        '''
        result = self._values.get("liveness_probe")
        return typing.cast(typing.Optional["VaultServerLivenessProbe"], result)

    @builtins.property
    def log_format(self) -> typing.Optional[builtins.str]:
        '''
        :schema: VaultServer#logFormat
        '''
        result = self._values.get("log_format")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def log_level(self) -> typing.Optional[builtins.str]:
        '''
        :schema: VaultServer#logLevel
        '''
        result = self._values.get("log_level")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def network_policy(self) -> typing.Optional["VaultServerNetworkPolicy"]:
        '''
        :schema: VaultServer#networkPolicy
        '''
        result = self._values.get("network_policy")
        return typing.cast(typing.Optional["VaultServerNetworkPolicy"], result)

    @builtins.property
    def node_selector(self) -> typing.Any:
        '''
        :schema: VaultServer#nodeSelector
        '''
        result = self._values.get("node_selector")
        return typing.cast(typing.Any, result)

    @builtins.property
    def persistent_volume_claim_retention_policy(
        self,
    ) -> typing.Optional["VaultServerPersistentVolumeClaimRetentionPolicy"]:
        '''
        :schema: VaultServer#persistentVolumeClaimRetentionPolicy
        '''
        result = self._values.get("persistent_volume_claim_retention_policy")
        return typing.cast(typing.Optional["VaultServerPersistentVolumeClaimRetentionPolicy"], result)

    @builtins.property
    def post_start(self) -> typing.Optional[typing.List[typing.Any]]:
        '''
        :schema: VaultServer#postStart
        '''
        result = self._values.get("post_start")
        return typing.cast(typing.Optional[typing.List[typing.Any]], result)

    @builtins.property
    def pre_stop_sleep_seconds(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: VaultServer#preStopSleepSeconds
        '''
        result = self._values.get("pre_stop_sleep_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def priority_class_name(self) -> typing.Optional[builtins.str]:
        '''
        :schema: VaultServer#priorityClassName
        '''
        result = self._values.get("priority_class_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def readiness_probe(self) -> typing.Optional["VaultServerReadinessProbe"]:
        '''
        :schema: VaultServer#readinessProbe
        '''
        result = self._values.get("readiness_probe")
        return typing.cast(typing.Optional["VaultServerReadinessProbe"], result)

    @builtins.property
    def resources(self) -> typing.Any:
        '''
        :schema: VaultServer#resources
        '''
        result = self._values.get("resources")
        return typing.cast(typing.Any, result)

    @builtins.property
    def route(self) -> typing.Optional["VaultServerRoute"]:
        '''
        :schema: VaultServer#route
        '''
        result = self._values.get("route")
        return typing.cast(typing.Optional["VaultServerRoute"], result)

    @builtins.property
    def service(self) -> typing.Optional["VaultServerService"]:
        '''
        :schema: VaultServer#service
        '''
        result = self._values.get("service")
        return typing.cast(typing.Optional["VaultServerService"], result)

    @builtins.property
    def service_account(self) -> typing.Optional["VaultServerServiceAccount"]:
        '''
        :schema: VaultServer#serviceAccount
        '''
        result = self._values.get("service_account")
        return typing.cast(typing.Optional["VaultServerServiceAccount"], result)

    @builtins.property
    def share_process_namespace(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: VaultServer#shareProcessNamespace
        '''
        result = self._values.get("share_process_namespace")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def standalone(self) -> typing.Optional["VaultServerStandalone"]:
        '''
        :schema: VaultServer#standalone
        '''
        result = self._values.get("standalone")
        return typing.cast(typing.Optional["VaultServerStandalone"], result)

    @builtins.property
    def stateful_set(self) -> typing.Optional["VaultServerStatefulSet"]:
        '''
        :schema: VaultServer#statefulSet
        '''
        result = self._values.get("stateful_set")
        return typing.cast(typing.Optional["VaultServerStatefulSet"], result)

    @builtins.property
    def termination_grace_period_seconds(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: VaultServer#terminationGracePeriodSeconds
        '''
        result = self._values.get("termination_grace_period_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def tolerations(self) -> typing.Any:
        '''
        :schema: VaultServer#tolerations
        '''
        result = self._values.get("tolerations")
        return typing.cast(typing.Any, result)

    @builtins.property
    def topology_spread_constraints(self) -> typing.Any:
        '''
        :schema: VaultServer#topologySpreadConstraints
        '''
        result = self._values.get("topology_spread_constraints")
        return typing.cast(typing.Any, result)

    @builtins.property
    def update_strategy_type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: VaultServer#updateStrategyType
        '''
        result = self._values.get("update_strategy_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def volume_mounts(self) -> typing.Optional[typing.List[typing.Any]]:
        '''
        :schema: VaultServer#volumeMounts
        '''
        result = self._values.get("volume_mounts")
        return typing.cast(typing.Optional[typing.List[typing.Any]], result)

    @builtins.property
    def volumes(self) -> typing.Optional[typing.List[typing.Any]]:
        '''
        :schema: VaultServer#volumes
        '''
        result = self._values.get("volumes")
        return typing.cast(typing.Optional[typing.List[typing.Any]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VaultServer(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="vault.VaultServerAuditStorage",
    jsii_struct_bases=[],
    name_mapping={
        "access_mode": "accessMode",
        "additional_values": "additionalValues",
        "annotations": "annotations",
        "enabled": "enabled",
        "labels": "labels",
        "mount_path": "mountPath",
        "size": "size",
        "storage_class": "storageClass",
    },
)
class VaultServerAuditStorage:
    def __init__(
        self,
        *,
        access_mode: typing.Optional[builtins.str] = None,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        annotations: typing.Any = None,
        enabled: typing.Any = None,
        labels: typing.Any = None,
        mount_path: typing.Optional[builtins.str] = None,
        size: typing.Optional[builtins.str] = None,
        storage_class: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param access_mode: 
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.
        :param annotations: 
        :param enabled: 
        :param labels: 
        :param mount_path: 
        :param size: 
        :param storage_class: 

        :schema: VaultServerAuditStorage
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__26f604d1e3fac6d4ef51fbf7522fcf3357c75d0ec693f8ca0496b3b2b3891026)
            check_type(argname="argument access_mode", value=access_mode, expected_type=type_hints["access_mode"])
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
            check_type(argname="argument annotations", value=annotations, expected_type=type_hints["annotations"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument labels", value=labels, expected_type=type_hints["labels"])
            check_type(argname="argument mount_path", value=mount_path, expected_type=type_hints["mount_path"])
            check_type(argname="argument size", value=size, expected_type=type_hints["size"])
            check_type(argname="argument storage_class", value=storage_class, expected_type=type_hints["storage_class"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if access_mode is not None:
            self._values["access_mode"] = access_mode
        if additional_values is not None:
            self._values["additional_values"] = additional_values
        if annotations is not None:
            self._values["annotations"] = annotations
        if enabled is not None:
            self._values["enabled"] = enabled
        if labels is not None:
            self._values["labels"] = labels
        if mount_path is not None:
            self._values["mount_path"] = mount_path
        if size is not None:
            self._values["size"] = size
        if storage_class is not None:
            self._values["storage_class"] = storage_class

    @builtins.property
    def access_mode(self) -> typing.Optional[builtins.str]:
        '''
        :schema: VaultServerAuditStorage#accessMode
        '''
        result = self._values.get("access_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def additional_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: VaultServerAuditStorage#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def annotations(self) -> typing.Any:
        '''
        :schema: VaultServerAuditStorage#annotations
        '''
        result = self._values.get("annotations")
        return typing.cast(typing.Any, result)

    @builtins.property
    def enabled(self) -> typing.Any:
        '''
        :schema: VaultServerAuditStorage#enabled
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Any, result)

    @builtins.property
    def labels(self) -> typing.Any:
        '''
        :schema: VaultServerAuditStorage#labels
        '''
        result = self._values.get("labels")
        return typing.cast(typing.Any, result)

    @builtins.property
    def mount_path(self) -> typing.Optional[builtins.str]:
        '''
        :schema: VaultServerAuditStorage#mountPath
        '''
        result = self._values.get("mount_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def size(self) -> typing.Optional[builtins.str]:
        '''
        :schema: VaultServerAuditStorage#size
        '''
        result = self._values.get("size")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def storage_class(self) -> typing.Optional[builtins.str]:
        '''
        :schema: VaultServerAuditStorage#storageClass
        '''
        result = self._values.get("storage_class")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VaultServerAuditStorage(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="vault.VaultServerAuthDelegator",
    jsii_struct_bases=[],
    name_mapping={"additional_values": "additionalValues", "enabled": "enabled"},
)
class VaultServerAuthDelegator:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        enabled: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.
        :param enabled: 

        :schema: VaultServerAuthDelegator
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9d17299c62b642e66ed27f3bfc739abd73c55549a7fe2b6ba1a01951463169c7)
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

        :schema: VaultServerAuthDelegator#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def enabled(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: VaultServerAuthDelegator#enabled
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VaultServerAuthDelegator(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="vault.VaultServerDataStorage",
    jsii_struct_bases=[],
    name_mapping={
        "access_mode": "accessMode",
        "additional_values": "additionalValues",
        "annotations": "annotations",
        "enabled": "enabled",
        "labels": "labels",
        "mount_path": "mountPath",
        "size": "size",
        "storage_class": "storageClass",
    },
)
class VaultServerDataStorage:
    def __init__(
        self,
        *,
        access_mode: typing.Optional[builtins.str] = None,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        annotations: typing.Any = None,
        enabled: typing.Any = None,
        labels: typing.Any = None,
        mount_path: typing.Optional[builtins.str] = None,
        size: typing.Optional[builtins.str] = None,
        storage_class: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param access_mode: 
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.
        :param annotations: 
        :param enabled: 
        :param labels: 
        :param mount_path: 
        :param size: 
        :param storage_class: 

        :schema: VaultServerDataStorage
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dc93d620ebfcadd63222313fd67c9eadcc11d526e8c5f1378be2e756cef1b8da)
            check_type(argname="argument access_mode", value=access_mode, expected_type=type_hints["access_mode"])
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
            check_type(argname="argument annotations", value=annotations, expected_type=type_hints["annotations"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument labels", value=labels, expected_type=type_hints["labels"])
            check_type(argname="argument mount_path", value=mount_path, expected_type=type_hints["mount_path"])
            check_type(argname="argument size", value=size, expected_type=type_hints["size"])
            check_type(argname="argument storage_class", value=storage_class, expected_type=type_hints["storage_class"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if access_mode is not None:
            self._values["access_mode"] = access_mode
        if additional_values is not None:
            self._values["additional_values"] = additional_values
        if annotations is not None:
            self._values["annotations"] = annotations
        if enabled is not None:
            self._values["enabled"] = enabled
        if labels is not None:
            self._values["labels"] = labels
        if mount_path is not None:
            self._values["mount_path"] = mount_path
        if size is not None:
            self._values["size"] = size
        if storage_class is not None:
            self._values["storage_class"] = storage_class

    @builtins.property
    def access_mode(self) -> typing.Optional[builtins.str]:
        '''
        :schema: VaultServerDataStorage#accessMode
        '''
        result = self._values.get("access_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def additional_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: VaultServerDataStorage#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def annotations(self) -> typing.Any:
        '''
        :schema: VaultServerDataStorage#annotations
        '''
        result = self._values.get("annotations")
        return typing.cast(typing.Any, result)

    @builtins.property
    def enabled(self) -> typing.Any:
        '''
        :schema: VaultServerDataStorage#enabled
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Any, result)

    @builtins.property
    def labels(self) -> typing.Any:
        '''
        :schema: VaultServerDataStorage#labels
        '''
        result = self._values.get("labels")
        return typing.cast(typing.Any, result)

    @builtins.property
    def mount_path(self) -> typing.Optional[builtins.str]:
        '''
        :schema: VaultServerDataStorage#mountPath
        '''
        result = self._values.get("mount_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def size(self) -> typing.Optional[builtins.str]:
        '''
        :schema: VaultServerDataStorage#size
        '''
        result = self._values.get("size")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def storage_class(self) -> typing.Optional[builtins.str]:
        '''
        :schema: VaultServerDataStorage#storageClass
        '''
        result = self._values.get("storage_class")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VaultServerDataStorage(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="vault.VaultServerDev",
    jsii_struct_bases=[],
    name_mapping={
        "additional_values": "additionalValues",
        "dev_root_token": "devRootToken",
        "enabled": "enabled",
    },
)
class VaultServerDev:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        dev_root_token: typing.Optional[builtins.str] = None,
        enabled: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.
        :param dev_root_token: 
        :param enabled: 

        :schema: VaultServerDev
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b3c5936407a0ed1495db6e00b8044d1902d3993b67ec7a9a4c004a0e607115c9)
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
            check_type(argname="argument dev_root_token", value=dev_root_token, expected_type=type_hints["dev_root_token"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_values is not None:
            self._values["additional_values"] = additional_values
        if dev_root_token is not None:
            self._values["dev_root_token"] = dev_root_token
        if enabled is not None:
            self._values["enabled"] = enabled

    @builtins.property
    def additional_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: VaultServerDev#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def dev_root_token(self) -> typing.Optional[builtins.str]:
        '''
        :schema: VaultServerDev#devRootToken
        '''
        result = self._values.get("dev_root_token")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enabled(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: VaultServerDev#enabled
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VaultServerDev(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="vault.VaultServerEnterpriseLicense",
    jsii_struct_bases=[],
    name_mapping={
        "additional_values": "additionalValues",
        "secret_key": "secretKey",
        "secret_name": "secretName",
    },
)
class VaultServerEnterpriseLicense:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        secret_key: typing.Optional[builtins.str] = None,
        secret_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.
        :param secret_key: 
        :param secret_name: 

        :schema: VaultServerEnterpriseLicense
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__792a78e09c28dfc95fc6f611469d8b1c54f288b921a6ab0b50a2275a3686f1d3)
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
            check_type(argname="argument secret_key", value=secret_key, expected_type=type_hints["secret_key"])
            check_type(argname="argument secret_name", value=secret_name, expected_type=type_hints["secret_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_values is not None:
            self._values["additional_values"] = additional_values
        if secret_key is not None:
            self._values["secret_key"] = secret_key
        if secret_name is not None:
            self._values["secret_name"] = secret_name

    @builtins.property
    def additional_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: VaultServerEnterpriseLicense#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def secret_key(self) -> typing.Optional[builtins.str]:
        '''
        :schema: VaultServerEnterpriseLicense#secretKey
        '''
        result = self._values.get("secret_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def secret_name(self) -> typing.Optional[builtins.str]:
        '''
        :schema: VaultServerEnterpriseLicense#secretName
        '''
        result = self._values.get("secret_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VaultServerEnterpriseLicense(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="vault.VaultServerHa",
    jsii_struct_bases=[],
    name_mapping={
        "additional_values": "additionalValues",
        "api_addr": "apiAddr",
        "cluster_addr": "clusterAddr",
        "config": "config",
        "disruption_budget": "disruptionBudget",
        "enabled": "enabled",
        "raft": "raft",
        "replicas": "replicas",
    },
)
class VaultServerHa:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        api_addr: typing.Optional[builtins.str] = None,
        cluster_addr: typing.Optional[builtins.str] = None,
        config: typing.Any = None,
        disruption_budget: typing.Optional[typing.Union["VaultServerHaDisruptionBudget", typing.Dict[builtins.str, typing.Any]]] = None,
        enabled: typing.Optional[builtins.bool] = None,
        raft: typing.Optional[typing.Union["VaultServerHaRaft", typing.Dict[builtins.str, typing.Any]]] = None,
        replicas: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.
        :param api_addr: 
        :param cluster_addr: 
        :param config: 
        :param disruption_budget: 
        :param enabled: 
        :param raft: 
        :param replicas: 

        :schema: VaultServerHa
        '''
        if isinstance(disruption_budget, dict):
            disruption_budget = VaultServerHaDisruptionBudget(**disruption_budget)
        if isinstance(raft, dict):
            raft = VaultServerHaRaft(**raft)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a85f5b50607467af77b8ac6eb3c03e0b74b08549d47782768b6d9839d6421216)
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
            check_type(argname="argument api_addr", value=api_addr, expected_type=type_hints["api_addr"])
            check_type(argname="argument cluster_addr", value=cluster_addr, expected_type=type_hints["cluster_addr"])
            check_type(argname="argument config", value=config, expected_type=type_hints["config"])
            check_type(argname="argument disruption_budget", value=disruption_budget, expected_type=type_hints["disruption_budget"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument raft", value=raft, expected_type=type_hints["raft"])
            check_type(argname="argument replicas", value=replicas, expected_type=type_hints["replicas"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_values is not None:
            self._values["additional_values"] = additional_values
        if api_addr is not None:
            self._values["api_addr"] = api_addr
        if cluster_addr is not None:
            self._values["cluster_addr"] = cluster_addr
        if config is not None:
            self._values["config"] = config
        if disruption_budget is not None:
            self._values["disruption_budget"] = disruption_budget
        if enabled is not None:
            self._values["enabled"] = enabled
        if raft is not None:
            self._values["raft"] = raft
        if replicas is not None:
            self._values["replicas"] = replicas

    @builtins.property
    def additional_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: VaultServerHa#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def api_addr(self) -> typing.Optional[builtins.str]:
        '''
        :schema: VaultServerHa#apiAddr
        '''
        result = self._values.get("api_addr")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cluster_addr(self) -> typing.Optional[builtins.str]:
        '''
        :schema: VaultServerHa#clusterAddr
        '''
        result = self._values.get("cluster_addr")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def config(self) -> typing.Any:
        '''
        :schema: VaultServerHa#config
        '''
        result = self._values.get("config")
        return typing.cast(typing.Any, result)

    @builtins.property
    def disruption_budget(self) -> typing.Optional["VaultServerHaDisruptionBudget"]:
        '''
        :schema: VaultServerHa#disruptionBudget
        '''
        result = self._values.get("disruption_budget")
        return typing.cast(typing.Optional["VaultServerHaDisruptionBudget"], result)

    @builtins.property
    def enabled(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: VaultServerHa#enabled
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def raft(self) -> typing.Optional["VaultServerHaRaft"]:
        '''
        :schema: VaultServerHa#raft
        '''
        result = self._values.get("raft")
        return typing.cast(typing.Optional["VaultServerHaRaft"], result)

    @builtins.property
    def replicas(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: VaultServerHa#replicas
        '''
        result = self._values.get("replicas")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VaultServerHa(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="vault.VaultServerHaDisruptionBudget",
    jsii_struct_bases=[],
    name_mapping={
        "additional_values": "additionalValues",
        "enabled": "enabled",
        "max_unavailable": "maxUnavailable",
    },
)
class VaultServerHaDisruptionBudget:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        enabled: typing.Optional[builtins.bool] = None,
        max_unavailable: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.
        :param enabled: 
        :param max_unavailable: 

        :schema: VaultServerHaDisruptionBudget
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c4cdcbe702d2f0bd9e2935f65d1cc96c2f004ba04e1791a1ea1d076c32d118b7)
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument max_unavailable", value=max_unavailable, expected_type=type_hints["max_unavailable"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_values is not None:
            self._values["additional_values"] = additional_values
        if enabled is not None:
            self._values["enabled"] = enabled
        if max_unavailable is not None:
            self._values["max_unavailable"] = max_unavailable

    @builtins.property
    def additional_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: VaultServerHaDisruptionBudget#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def enabled(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: VaultServerHaDisruptionBudget#enabled
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def max_unavailable(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: VaultServerHaDisruptionBudget#maxUnavailable
        '''
        result = self._values.get("max_unavailable")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VaultServerHaDisruptionBudget(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="vault.VaultServerHaRaft",
    jsii_struct_bases=[],
    name_mapping={
        "additional_values": "additionalValues",
        "config": "config",
        "enabled": "enabled",
        "set_node_id": "setNodeId",
    },
)
class VaultServerHaRaft:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        config: typing.Any = None,
        enabled: typing.Optional[builtins.bool] = None,
        set_node_id: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.
        :param config: 
        :param enabled: 
        :param set_node_id: 

        :schema: VaultServerHaRaft
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__41a2403a61c304b439ba6472e66794a9e0120a6b53ca2b3df820e85e2eea3db9)
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
            check_type(argname="argument config", value=config, expected_type=type_hints["config"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument set_node_id", value=set_node_id, expected_type=type_hints["set_node_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_values is not None:
            self._values["additional_values"] = additional_values
        if config is not None:
            self._values["config"] = config
        if enabled is not None:
            self._values["enabled"] = enabled
        if set_node_id is not None:
            self._values["set_node_id"] = set_node_id

    @builtins.property
    def additional_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: VaultServerHaRaft#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def config(self) -> typing.Any:
        '''
        :schema: VaultServerHaRaft#config
        '''
        result = self._values.get("config")
        return typing.cast(typing.Any, result)

    @builtins.property
    def enabled(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: VaultServerHaRaft#enabled
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def set_node_id(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: VaultServerHaRaft#setNodeId
        '''
        result = self._values.get("set_node_id")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VaultServerHaRaft(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="vault.VaultServerImage",
    jsii_struct_bases=[],
    name_mapping={
        "additional_values": "additionalValues",
        "pull_policy": "pullPolicy",
        "repository": "repository",
        "tag": "tag",
    },
)
class VaultServerImage:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        pull_policy: typing.Optional[builtins.str] = None,
        repository: typing.Optional[builtins.str] = None,
        tag: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.
        :param pull_policy: 
        :param repository: 
        :param tag: 

        :schema: VaultServerImage
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9b580c02f1c1bd2bb2f5fc2ec0a3aa261b9ea3d6061d248a1c57c7dcf9ebd3d0)
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
            check_type(argname="argument pull_policy", value=pull_policy, expected_type=type_hints["pull_policy"])
            check_type(argname="argument repository", value=repository, expected_type=type_hints["repository"])
            check_type(argname="argument tag", value=tag, expected_type=type_hints["tag"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_values is not None:
            self._values["additional_values"] = additional_values
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

        :schema: VaultServerImage#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def pull_policy(self) -> typing.Optional[builtins.str]:
        '''
        :schema: VaultServerImage#pullPolicy
        '''
        result = self._values.get("pull_policy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def repository(self) -> typing.Optional[builtins.str]:
        '''
        :schema: VaultServerImage#repository
        '''
        result = self._values.get("repository")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tag(self) -> typing.Optional[builtins.str]:
        '''
        :schema: VaultServerImage#tag
        '''
        result = self._values.get("tag")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VaultServerImage(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="vault.VaultServerIngress",
    jsii_struct_bases=[],
    name_mapping={
        "active_service": "activeService",
        "additional_values": "additionalValues",
        "annotations": "annotations",
        "enabled": "enabled",
        "extra_paths": "extraPaths",
        "hosts": "hosts",
        "ingress_class_name": "ingressClassName",
        "labels": "labels",
        "path_type": "pathType",
        "tls": "tls",
    },
)
class VaultServerIngress:
    def __init__(
        self,
        *,
        active_service: typing.Optional[builtins.bool] = None,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        annotations: typing.Any = None,
        enabled: typing.Optional[builtins.bool] = None,
        extra_paths: typing.Optional[typing.Sequence[typing.Any]] = None,
        hosts: typing.Optional[typing.Sequence[typing.Union["VaultServerIngressHosts", typing.Dict[builtins.str, typing.Any]]]] = None,
        ingress_class_name: typing.Optional[builtins.str] = None,
        labels: typing.Any = None,
        path_type: typing.Optional[builtins.str] = None,
        tls: typing.Optional[typing.Sequence[typing.Any]] = None,
    ) -> None:
        '''
        :param active_service: 
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.
        :param annotations: 
        :param enabled: 
        :param extra_paths: 
        :param hosts: 
        :param ingress_class_name: 
        :param labels: 
        :param path_type: 
        :param tls: 

        :schema: VaultServerIngress
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cb1f8c9753a0338e9f81d02a6015fd381fc45e21d50f2f8f36225d4ef7cbb885)
            check_type(argname="argument active_service", value=active_service, expected_type=type_hints["active_service"])
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
            check_type(argname="argument annotations", value=annotations, expected_type=type_hints["annotations"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument extra_paths", value=extra_paths, expected_type=type_hints["extra_paths"])
            check_type(argname="argument hosts", value=hosts, expected_type=type_hints["hosts"])
            check_type(argname="argument ingress_class_name", value=ingress_class_name, expected_type=type_hints["ingress_class_name"])
            check_type(argname="argument labels", value=labels, expected_type=type_hints["labels"])
            check_type(argname="argument path_type", value=path_type, expected_type=type_hints["path_type"])
            check_type(argname="argument tls", value=tls, expected_type=type_hints["tls"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if active_service is not None:
            self._values["active_service"] = active_service
        if additional_values is not None:
            self._values["additional_values"] = additional_values
        if annotations is not None:
            self._values["annotations"] = annotations
        if enabled is not None:
            self._values["enabled"] = enabled
        if extra_paths is not None:
            self._values["extra_paths"] = extra_paths
        if hosts is not None:
            self._values["hosts"] = hosts
        if ingress_class_name is not None:
            self._values["ingress_class_name"] = ingress_class_name
        if labels is not None:
            self._values["labels"] = labels
        if path_type is not None:
            self._values["path_type"] = path_type
        if tls is not None:
            self._values["tls"] = tls

    @builtins.property
    def active_service(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: VaultServerIngress#activeService
        '''
        result = self._values.get("active_service")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def additional_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: VaultServerIngress#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def annotations(self) -> typing.Any:
        '''
        :schema: VaultServerIngress#annotations
        '''
        result = self._values.get("annotations")
        return typing.cast(typing.Any, result)

    @builtins.property
    def enabled(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: VaultServerIngress#enabled
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def extra_paths(self) -> typing.Optional[typing.List[typing.Any]]:
        '''
        :schema: VaultServerIngress#extraPaths
        '''
        result = self._values.get("extra_paths")
        return typing.cast(typing.Optional[typing.List[typing.Any]], result)

    @builtins.property
    def hosts(self) -> typing.Optional[typing.List["VaultServerIngressHosts"]]:
        '''
        :schema: VaultServerIngress#hosts
        '''
        result = self._values.get("hosts")
        return typing.cast(typing.Optional[typing.List["VaultServerIngressHosts"]], result)

    @builtins.property
    def ingress_class_name(self) -> typing.Optional[builtins.str]:
        '''
        :schema: VaultServerIngress#ingressClassName
        '''
        result = self._values.get("ingress_class_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def labels(self) -> typing.Any:
        '''
        :schema: VaultServerIngress#labels
        '''
        result = self._values.get("labels")
        return typing.cast(typing.Any, result)

    @builtins.property
    def path_type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: VaultServerIngress#pathType
        '''
        result = self._values.get("path_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tls(self) -> typing.Optional[typing.List[typing.Any]]:
        '''
        :schema: VaultServerIngress#tls
        '''
        result = self._values.get("tls")
        return typing.cast(typing.Optional[typing.List[typing.Any]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VaultServerIngress(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="vault.VaultServerIngressHosts",
    jsii_struct_bases=[],
    name_mapping={"host": "host", "paths": "paths"},
)
class VaultServerIngressHosts:
    def __init__(
        self,
        *,
        host: typing.Optional[builtins.str] = None,
        paths: typing.Optional[typing.Sequence[typing.Any]] = None,
    ) -> None:
        '''
        :param host: 
        :param paths: 

        :schema: VaultServerIngressHosts
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__38e71b00967178ddfbcd045d0ad9d940f5ba833795a5dd8f5e8805d4a2bb40d0)
            check_type(argname="argument host", value=host, expected_type=type_hints["host"])
            check_type(argname="argument paths", value=paths, expected_type=type_hints["paths"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if host is not None:
            self._values["host"] = host
        if paths is not None:
            self._values["paths"] = paths

    @builtins.property
    def host(self) -> typing.Optional[builtins.str]:
        '''
        :schema: VaultServerIngressHosts#host
        '''
        result = self._values.get("host")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def paths(self) -> typing.Optional[typing.List[typing.Any]]:
        '''
        :schema: VaultServerIngressHosts#paths
        '''
        result = self._values.get("paths")
        return typing.cast(typing.Optional[typing.List[typing.Any]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VaultServerIngressHosts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="vault.VaultServerLivenessProbe",
    jsii_struct_bases=[],
    name_mapping={
        "additional_values": "additionalValues",
        "enabled": "enabled",
        "exec_command": "execCommand",
        "failure_threshold": "failureThreshold",
        "initial_delay_seconds": "initialDelaySeconds",
        "path": "path",
        "period_seconds": "periodSeconds",
        "port": "port",
        "success_threshold": "successThreshold",
        "timeout_seconds": "timeoutSeconds",
    },
)
class VaultServerLivenessProbe:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        enabled: typing.Optional[builtins.bool] = None,
        exec_command: typing.Optional[typing.Sequence[typing.Any]] = None,
        failure_threshold: typing.Optional[jsii.Number] = None,
        initial_delay_seconds: typing.Optional[jsii.Number] = None,
        path: typing.Optional[builtins.str] = None,
        period_seconds: typing.Optional[jsii.Number] = None,
        port: typing.Optional[jsii.Number] = None,
        success_threshold: typing.Optional[jsii.Number] = None,
        timeout_seconds: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.
        :param enabled: 
        :param exec_command: 
        :param failure_threshold: 
        :param initial_delay_seconds: 
        :param path: 
        :param period_seconds: 
        :param port: 
        :param success_threshold: 
        :param timeout_seconds: 

        :schema: VaultServerLivenessProbe
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7fe9e4444d3e77702169191cdb83762bccdc93f49a00011433290313f3122979)
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument exec_command", value=exec_command, expected_type=type_hints["exec_command"])
            check_type(argname="argument failure_threshold", value=failure_threshold, expected_type=type_hints["failure_threshold"])
            check_type(argname="argument initial_delay_seconds", value=initial_delay_seconds, expected_type=type_hints["initial_delay_seconds"])
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            check_type(argname="argument period_seconds", value=period_seconds, expected_type=type_hints["period_seconds"])
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
            check_type(argname="argument success_threshold", value=success_threshold, expected_type=type_hints["success_threshold"])
            check_type(argname="argument timeout_seconds", value=timeout_seconds, expected_type=type_hints["timeout_seconds"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_values is not None:
            self._values["additional_values"] = additional_values
        if enabled is not None:
            self._values["enabled"] = enabled
        if exec_command is not None:
            self._values["exec_command"] = exec_command
        if failure_threshold is not None:
            self._values["failure_threshold"] = failure_threshold
        if initial_delay_seconds is not None:
            self._values["initial_delay_seconds"] = initial_delay_seconds
        if path is not None:
            self._values["path"] = path
        if period_seconds is not None:
            self._values["period_seconds"] = period_seconds
        if port is not None:
            self._values["port"] = port
        if success_threshold is not None:
            self._values["success_threshold"] = success_threshold
        if timeout_seconds is not None:
            self._values["timeout_seconds"] = timeout_seconds

    @builtins.property
    def additional_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: VaultServerLivenessProbe#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def enabled(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: VaultServerLivenessProbe#enabled
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def exec_command(self) -> typing.Optional[typing.List[typing.Any]]:
        '''
        :schema: VaultServerLivenessProbe#execCommand
        '''
        result = self._values.get("exec_command")
        return typing.cast(typing.Optional[typing.List[typing.Any]], result)

    @builtins.property
    def failure_threshold(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: VaultServerLivenessProbe#failureThreshold
        '''
        result = self._values.get("failure_threshold")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def initial_delay_seconds(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: VaultServerLivenessProbe#initialDelaySeconds
        '''
        result = self._values.get("initial_delay_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def path(self) -> typing.Optional[builtins.str]:
        '''
        :schema: VaultServerLivenessProbe#path
        '''
        result = self._values.get("path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def period_seconds(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: VaultServerLivenessProbe#periodSeconds
        '''
        result = self._values.get("period_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def port(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: VaultServerLivenessProbe#port
        '''
        result = self._values.get("port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def success_threshold(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: VaultServerLivenessProbe#successThreshold
        '''
        result = self._values.get("success_threshold")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def timeout_seconds(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: VaultServerLivenessProbe#timeoutSeconds
        '''
        result = self._values.get("timeout_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VaultServerLivenessProbe(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="vault.VaultServerNetworkPolicy",
    jsii_struct_bases=[],
    name_mapping={
        "additional_values": "additionalValues",
        "egress": "egress",
        "enabled": "enabled",
        "ingress": "ingress",
    },
)
class VaultServerNetworkPolicy:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        egress: typing.Optional[typing.Sequence[typing.Any]] = None,
        enabled: typing.Optional[builtins.bool] = None,
        ingress: typing.Optional[typing.Sequence[typing.Any]] = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.
        :param egress: 
        :param enabled: 
        :param ingress: 

        :schema: VaultServerNetworkPolicy
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fe312061004d7f526d33cf6835c8dbba0d8688c3ba7e40f517ad9995560fd0db)
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
            check_type(argname="argument egress", value=egress, expected_type=type_hints["egress"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument ingress", value=ingress, expected_type=type_hints["ingress"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_values is not None:
            self._values["additional_values"] = additional_values
        if egress is not None:
            self._values["egress"] = egress
        if enabled is not None:
            self._values["enabled"] = enabled
        if ingress is not None:
            self._values["ingress"] = ingress

    @builtins.property
    def additional_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: VaultServerNetworkPolicy#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def egress(self) -> typing.Optional[typing.List[typing.Any]]:
        '''
        :schema: VaultServerNetworkPolicy#egress
        '''
        result = self._values.get("egress")
        return typing.cast(typing.Optional[typing.List[typing.Any]], result)

    @builtins.property
    def enabled(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: VaultServerNetworkPolicy#enabled
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def ingress(self) -> typing.Optional[typing.List[typing.Any]]:
        '''
        :schema: VaultServerNetworkPolicy#ingress
        '''
        result = self._values.get("ingress")
        return typing.cast(typing.Optional[typing.List[typing.Any]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VaultServerNetworkPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="vault.VaultServerPersistentVolumeClaimRetentionPolicy",
    jsii_struct_bases=[],
    name_mapping={
        "additional_values": "additionalValues",
        "when_deleted": "whenDeleted",
        "when_scaled": "whenScaled",
    },
)
class VaultServerPersistentVolumeClaimRetentionPolicy:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        when_deleted: typing.Optional[builtins.str] = None,
        when_scaled: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.
        :param when_deleted: 
        :param when_scaled: 

        :schema: VaultServerPersistentVolumeClaimRetentionPolicy
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__43acf80ad2563b040e3d648aa3f74c8d3030c26b523f05854687bf1f1b402ce5)
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
            check_type(argname="argument when_deleted", value=when_deleted, expected_type=type_hints["when_deleted"])
            check_type(argname="argument when_scaled", value=when_scaled, expected_type=type_hints["when_scaled"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_values is not None:
            self._values["additional_values"] = additional_values
        if when_deleted is not None:
            self._values["when_deleted"] = when_deleted
        if when_scaled is not None:
            self._values["when_scaled"] = when_scaled

    @builtins.property
    def additional_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: VaultServerPersistentVolumeClaimRetentionPolicy#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def when_deleted(self) -> typing.Optional[builtins.str]:
        '''
        :schema: VaultServerPersistentVolumeClaimRetentionPolicy#whenDeleted
        '''
        result = self._values.get("when_deleted")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def when_scaled(self) -> typing.Optional[builtins.str]:
        '''
        :schema: VaultServerPersistentVolumeClaimRetentionPolicy#whenScaled
        '''
        result = self._values.get("when_scaled")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VaultServerPersistentVolumeClaimRetentionPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="vault.VaultServerReadinessProbe",
    jsii_struct_bases=[],
    name_mapping={
        "additional_values": "additionalValues",
        "enabled": "enabled",
        "failure_threshold": "failureThreshold",
        "initial_delay_seconds": "initialDelaySeconds",
        "period_seconds": "periodSeconds",
        "port": "port",
        "success_threshold": "successThreshold",
        "timeout_seconds": "timeoutSeconds",
    },
)
class VaultServerReadinessProbe:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        enabled: typing.Optional[builtins.bool] = None,
        failure_threshold: typing.Optional[jsii.Number] = None,
        initial_delay_seconds: typing.Optional[jsii.Number] = None,
        period_seconds: typing.Optional[jsii.Number] = None,
        port: typing.Optional[jsii.Number] = None,
        success_threshold: typing.Optional[jsii.Number] = None,
        timeout_seconds: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.
        :param enabled: 
        :param failure_threshold: 
        :param initial_delay_seconds: 
        :param period_seconds: 
        :param port: 
        :param success_threshold: 
        :param timeout_seconds: 

        :schema: VaultServerReadinessProbe
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__74e65ef403a4182326fb82b2b1c46d75187549d986422f7ff3c51f2273de7981)
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument failure_threshold", value=failure_threshold, expected_type=type_hints["failure_threshold"])
            check_type(argname="argument initial_delay_seconds", value=initial_delay_seconds, expected_type=type_hints["initial_delay_seconds"])
            check_type(argname="argument period_seconds", value=period_seconds, expected_type=type_hints["period_seconds"])
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
            check_type(argname="argument success_threshold", value=success_threshold, expected_type=type_hints["success_threshold"])
            check_type(argname="argument timeout_seconds", value=timeout_seconds, expected_type=type_hints["timeout_seconds"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_values is not None:
            self._values["additional_values"] = additional_values
        if enabled is not None:
            self._values["enabled"] = enabled
        if failure_threshold is not None:
            self._values["failure_threshold"] = failure_threshold
        if initial_delay_seconds is not None:
            self._values["initial_delay_seconds"] = initial_delay_seconds
        if period_seconds is not None:
            self._values["period_seconds"] = period_seconds
        if port is not None:
            self._values["port"] = port
        if success_threshold is not None:
            self._values["success_threshold"] = success_threshold
        if timeout_seconds is not None:
            self._values["timeout_seconds"] = timeout_seconds

    @builtins.property
    def additional_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: VaultServerReadinessProbe#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def enabled(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: VaultServerReadinessProbe#enabled
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def failure_threshold(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: VaultServerReadinessProbe#failureThreshold
        '''
        result = self._values.get("failure_threshold")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def initial_delay_seconds(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: VaultServerReadinessProbe#initialDelaySeconds
        '''
        result = self._values.get("initial_delay_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def period_seconds(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: VaultServerReadinessProbe#periodSeconds
        '''
        result = self._values.get("period_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def port(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: VaultServerReadinessProbe#port
        '''
        result = self._values.get("port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def success_threshold(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: VaultServerReadinessProbe#successThreshold
        '''
        result = self._values.get("success_threshold")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def timeout_seconds(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: VaultServerReadinessProbe#timeoutSeconds
        '''
        result = self._values.get("timeout_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VaultServerReadinessProbe(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="vault.VaultServerRoute",
    jsii_struct_bases=[],
    name_mapping={
        "active_service": "activeService",
        "additional_values": "additionalValues",
        "annotations": "annotations",
        "enabled": "enabled",
        "host": "host",
        "labels": "labels",
        "tls": "tls",
    },
)
class VaultServerRoute:
    def __init__(
        self,
        *,
        active_service: typing.Optional[builtins.bool] = None,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        annotations: typing.Any = None,
        enabled: typing.Optional[builtins.bool] = None,
        host: typing.Optional[builtins.str] = None,
        labels: typing.Any = None,
        tls: typing.Any = None,
    ) -> None:
        '''
        :param active_service: 
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.
        :param annotations: 
        :param enabled: 
        :param host: 
        :param labels: 
        :param tls: 

        :schema: VaultServerRoute
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__89e18f3aa62665bd680600a3136d7d680bd43c5b9baf6286330f2d0975b87f3a)
            check_type(argname="argument active_service", value=active_service, expected_type=type_hints["active_service"])
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
            check_type(argname="argument annotations", value=annotations, expected_type=type_hints["annotations"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument host", value=host, expected_type=type_hints["host"])
            check_type(argname="argument labels", value=labels, expected_type=type_hints["labels"])
            check_type(argname="argument tls", value=tls, expected_type=type_hints["tls"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if active_service is not None:
            self._values["active_service"] = active_service
        if additional_values is not None:
            self._values["additional_values"] = additional_values
        if annotations is not None:
            self._values["annotations"] = annotations
        if enabled is not None:
            self._values["enabled"] = enabled
        if host is not None:
            self._values["host"] = host
        if labels is not None:
            self._values["labels"] = labels
        if tls is not None:
            self._values["tls"] = tls

    @builtins.property
    def active_service(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: VaultServerRoute#activeService
        '''
        result = self._values.get("active_service")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def additional_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: VaultServerRoute#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def annotations(self) -> typing.Any:
        '''
        :schema: VaultServerRoute#annotations
        '''
        result = self._values.get("annotations")
        return typing.cast(typing.Any, result)

    @builtins.property
    def enabled(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: VaultServerRoute#enabled
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def host(self) -> typing.Optional[builtins.str]:
        '''
        :schema: VaultServerRoute#host
        '''
        result = self._values.get("host")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def labels(self) -> typing.Any:
        '''
        :schema: VaultServerRoute#labels
        '''
        result = self._values.get("labels")
        return typing.cast(typing.Any, result)

    @builtins.property
    def tls(self) -> typing.Any:
        '''
        :schema: VaultServerRoute#tls
        '''
        result = self._values.get("tls")
        return typing.cast(typing.Any, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VaultServerRoute(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="vault.VaultServerService",
    jsii_struct_bases=[],
    name_mapping={
        "active": "active",
        "active_node_port": "activeNodePort",
        "additional_values": "additionalValues",
        "annotations": "annotations",
        "enabled": "enabled",
        "external_traffic_policy": "externalTrafficPolicy",
        "instance_selector": "instanceSelector",
        "ip_families": "ipFamilies",
        "ip_family_policy": "ipFamilyPolicy",
        "node_port": "nodePort",
        "port": "port",
        "publish_not_ready_addresses": "publishNotReadyAddresses",
        "standby": "standby",
        "standby_node_port": "standbyNodePort",
        "target_port": "targetPort",
    },
)
class VaultServerService:
    def __init__(
        self,
        *,
        active: typing.Optional[typing.Union["VaultServerServiceActive", typing.Dict[builtins.str, typing.Any]]] = None,
        active_node_port: typing.Optional[jsii.Number] = None,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        annotations: typing.Any = None,
        enabled: typing.Optional[builtins.bool] = None,
        external_traffic_policy: typing.Optional[builtins.str] = None,
        instance_selector: typing.Optional[typing.Union["VaultServerServiceInstanceSelector", typing.Dict[builtins.str, typing.Any]]] = None,
        ip_families: typing.Optional[typing.Sequence[typing.Any]] = None,
        ip_family_policy: typing.Optional[builtins.str] = None,
        node_port: typing.Optional[jsii.Number] = None,
        port: typing.Optional[jsii.Number] = None,
        publish_not_ready_addresses: typing.Optional[builtins.bool] = None,
        standby: typing.Optional[typing.Union["VaultServerServiceStandby", typing.Dict[builtins.str, typing.Any]]] = None,
        standby_node_port: typing.Optional[jsii.Number] = None,
        target_port: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param active: 
        :param active_node_port: 
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.
        :param annotations: 
        :param enabled: 
        :param external_traffic_policy: 
        :param instance_selector: 
        :param ip_families: 
        :param ip_family_policy: 
        :param node_port: 
        :param port: 
        :param publish_not_ready_addresses: 
        :param standby: 
        :param standby_node_port: 
        :param target_port: 

        :schema: VaultServerService
        '''
        if isinstance(active, dict):
            active = VaultServerServiceActive(**active)
        if isinstance(instance_selector, dict):
            instance_selector = VaultServerServiceInstanceSelector(**instance_selector)
        if isinstance(standby, dict):
            standby = VaultServerServiceStandby(**standby)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bff7c12ff40d9f13bc33b80103b5e0a8ca10e68d15db6b9bc6ff485a2868ed9a)
            check_type(argname="argument active", value=active, expected_type=type_hints["active"])
            check_type(argname="argument active_node_port", value=active_node_port, expected_type=type_hints["active_node_port"])
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
            check_type(argname="argument annotations", value=annotations, expected_type=type_hints["annotations"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument external_traffic_policy", value=external_traffic_policy, expected_type=type_hints["external_traffic_policy"])
            check_type(argname="argument instance_selector", value=instance_selector, expected_type=type_hints["instance_selector"])
            check_type(argname="argument ip_families", value=ip_families, expected_type=type_hints["ip_families"])
            check_type(argname="argument ip_family_policy", value=ip_family_policy, expected_type=type_hints["ip_family_policy"])
            check_type(argname="argument node_port", value=node_port, expected_type=type_hints["node_port"])
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
            check_type(argname="argument publish_not_ready_addresses", value=publish_not_ready_addresses, expected_type=type_hints["publish_not_ready_addresses"])
            check_type(argname="argument standby", value=standby, expected_type=type_hints["standby"])
            check_type(argname="argument standby_node_port", value=standby_node_port, expected_type=type_hints["standby_node_port"])
            check_type(argname="argument target_port", value=target_port, expected_type=type_hints["target_port"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if active is not None:
            self._values["active"] = active
        if active_node_port is not None:
            self._values["active_node_port"] = active_node_port
        if additional_values is not None:
            self._values["additional_values"] = additional_values
        if annotations is not None:
            self._values["annotations"] = annotations
        if enabled is not None:
            self._values["enabled"] = enabled
        if external_traffic_policy is not None:
            self._values["external_traffic_policy"] = external_traffic_policy
        if instance_selector is not None:
            self._values["instance_selector"] = instance_selector
        if ip_families is not None:
            self._values["ip_families"] = ip_families
        if ip_family_policy is not None:
            self._values["ip_family_policy"] = ip_family_policy
        if node_port is not None:
            self._values["node_port"] = node_port
        if port is not None:
            self._values["port"] = port
        if publish_not_ready_addresses is not None:
            self._values["publish_not_ready_addresses"] = publish_not_ready_addresses
        if standby is not None:
            self._values["standby"] = standby
        if standby_node_port is not None:
            self._values["standby_node_port"] = standby_node_port
        if target_port is not None:
            self._values["target_port"] = target_port

    @builtins.property
    def active(self) -> typing.Optional["VaultServerServiceActive"]:
        '''
        :schema: VaultServerService#active
        '''
        result = self._values.get("active")
        return typing.cast(typing.Optional["VaultServerServiceActive"], result)

    @builtins.property
    def active_node_port(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: VaultServerService#activeNodePort
        '''
        result = self._values.get("active_node_port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def additional_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: VaultServerService#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def annotations(self) -> typing.Any:
        '''
        :schema: VaultServerService#annotations
        '''
        result = self._values.get("annotations")
        return typing.cast(typing.Any, result)

    @builtins.property
    def enabled(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: VaultServerService#enabled
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def external_traffic_policy(self) -> typing.Optional[builtins.str]:
        '''
        :schema: VaultServerService#externalTrafficPolicy
        '''
        result = self._values.get("external_traffic_policy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def instance_selector(
        self,
    ) -> typing.Optional["VaultServerServiceInstanceSelector"]:
        '''
        :schema: VaultServerService#instanceSelector
        '''
        result = self._values.get("instance_selector")
        return typing.cast(typing.Optional["VaultServerServiceInstanceSelector"], result)

    @builtins.property
    def ip_families(self) -> typing.Optional[typing.List[typing.Any]]:
        '''
        :schema: VaultServerService#ipFamilies
        '''
        result = self._values.get("ip_families")
        return typing.cast(typing.Optional[typing.List[typing.Any]], result)

    @builtins.property
    def ip_family_policy(self) -> typing.Optional[builtins.str]:
        '''
        :schema: VaultServerService#ipFamilyPolicy
        '''
        result = self._values.get("ip_family_policy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def node_port(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: VaultServerService#nodePort
        '''
        result = self._values.get("node_port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def port(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: VaultServerService#port
        '''
        result = self._values.get("port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def publish_not_ready_addresses(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: VaultServerService#publishNotReadyAddresses
        '''
        result = self._values.get("publish_not_ready_addresses")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def standby(self) -> typing.Optional["VaultServerServiceStandby"]:
        '''
        :schema: VaultServerService#standby
        '''
        result = self._values.get("standby")
        return typing.cast(typing.Optional["VaultServerServiceStandby"], result)

    @builtins.property
    def standby_node_port(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: VaultServerService#standbyNodePort
        '''
        result = self._values.get("standby_node_port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def target_port(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: VaultServerService#targetPort
        '''
        result = self._values.get("target_port")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VaultServerService(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="vault.VaultServerServiceAccount",
    jsii_struct_bases=[],
    name_mapping={
        "additional_values": "additionalValues",
        "annotations": "annotations",
        "create": "create",
        "create_secret": "createSecret",
        "extra_labels": "extraLabels",
        "name": "name",
        "service_discovery": "serviceDiscovery",
    },
)
class VaultServerServiceAccount:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        annotations: typing.Any = None,
        create: typing.Optional[builtins.bool] = None,
        create_secret: typing.Optional[builtins.bool] = None,
        extra_labels: typing.Any = None,
        name: typing.Optional[builtins.str] = None,
        service_discovery: typing.Optional[typing.Union["VaultServerServiceAccountServiceDiscovery", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.
        :param annotations: 
        :param create: 
        :param create_secret: 
        :param extra_labels: 
        :param name: 
        :param service_discovery: 

        :schema: VaultServerServiceAccount
        '''
        if isinstance(service_discovery, dict):
            service_discovery = VaultServerServiceAccountServiceDiscovery(**service_discovery)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__92e1c19011364670236a5f52837b99e4e01a47defadace2ea1a8a6632d6a9c21)
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
            check_type(argname="argument annotations", value=annotations, expected_type=type_hints["annotations"])
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
            check_type(argname="argument create_secret", value=create_secret, expected_type=type_hints["create_secret"])
            check_type(argname="argument extra_labels", value=extra_labels, expected_type=type_hints["extra_labels"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument service_discovery", value=service_discovery, expected_type=type_hints["service_discovery"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_values is not None:
            self._values["additional_values"] = additional_values
        if annotations is not None:
            self._values["annotations"] = annotations
        if create is not None:
            self._values["create"] = create
        if create_secret is not None:
            self._values["create_secret"] = create_secret
        if extra_labels is not None:
            self._values["extra_labels"] = extra_labels
        if name is not None:
            self._values["name"] = name
        if service_discovery is not None:
            self._values["service_discovery"] = service_discovery

    @builtins.property
    def additional_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: VaultServerServiceAccount#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def annotations(self) -> typing.Any:
        '''
        :schema: VaultServerServiceAccount#annotations
        '''
        result = self._values.get("annotations")
        return typing.cast(typing.Any, result)

    @builtins.property
    def create(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: VaultServerServiceAccount#create
        '''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def create_secret(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: VaultServerServiceAccount#createSecret
        '''
        result = self._values.get("create_secret")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def extra_labels(self) -> typing.Any:
        '''
        :schema: VaultServerServiceAccount#extraLabels
        '''
        result = self._values.get("extra_labels")
        return typing.cast(typing.Any, result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''
        :schema: VaultServerServiceAccount#name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def service_discovery(
        self,
    ) -> typing.Optional["VaultServerServiceAccountServiceDiscovery"]:
        '''
        :schema: VaultServerServiceAccount#serviceDiscovery
        '''
        result = self._values.get("service_discovery")
        return typing.cast(typing.Optional["VaultServerServiceAccountServiceDiscovery"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VaultServerServiceAccount(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="vault.VaultServerServiceAccountServiceDiscovery",
    jsii_struct_bases=[],
    name_mapping={"additional_values": "additionalValues", "enabled": "enabled"},
)
class VaultServerServiceAccountServiceDiscovery:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        enabled: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.
        :param enabled: 

        :schema: VaultServerServiceAccountServiceDiscovery
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e21ed868d7176a05ef8f4dd0de8562a12365484f151b8b6bfb04c76a426723ff)
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

        :schema: VaultServerServiceAccountServiceDiscovery#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def enabled(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: VaultServerServiceAccountServiceDiscovery#enabled
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VaultServerServiceAccountServiceDiscovery(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="vault.VaultServerServiceActive",
    jsii_struct_bases=[],
    name_mapping={
        "additional_values": "additionalValues",
        "annotations": "annotations",
        "enabled": "enabled",
    },
)
class VaultServerServiceActive:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        annotations: typing.Any = None,
        enabled: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.
        :param annotations: 
        :param enabled: 

        :schema: VaultServerServiceActive
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__07365ba54e29a927d1284608741bd095fb178f8cae81e04e1f9ae3bf1131086c)
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
            check_type(argname="argument annotations", value=annotations, expected_type=type_hints["annotations"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_values is not None:
            self._values["additional_values"] = additional_values
        if annotations is not None:
            self._values["annotations"] = annotations
        if enabled is not None:
            self._values["enabled"] = enabled

    @builtins.property
    def additional_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: VaultServerServiceActive#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def annotations(self) -> typing.Any:
        '''
        :schema: VaultServerServiceActive#annotations
        '''
        result = self._values.get("annotations")
        return typing.cast(typing.Any, result)

    @builtins.property
    def enabled(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: VaultServerServiceActive#enabled
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VaultServerServiceActive(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="vault.VaultServerServiceInstanceSelector",
    jsii_struct_bases=[],
    name_mapping={"additional_values": "additionalValues", "enabled": "enabled"},
)
class VaultServerServiceInstanceSelector:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        enabled: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.
        :param enabled: 

        :schema: VaultServerServiceInstanceSelector
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2b56b3c6566ec85a23c195140771e621eddb7494b6c06ced27f00a4bb248f97b)
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

        :schema: VaultServerServiceInstanceSelector#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def enabled(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: VaultServerServiceInstanceSelector#enabled
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VaultServerServiceInstanceSelector(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="vault.VaultServerServiceStandby",
    jsii_struct_bases=[],
    name_mapping={
        "additional_values": "additionalValues",
        "annotations": "annotations",
        "enabled": "enabled",
    },
)
class VaultServerServiceStandby:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        annotations: typing.Any = None,
        enabled: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.
        :param annotations: 
        :param enabled: 

        :schema: VaultServerServiceStandby
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b4451e329a945bf5d5bb81c184630169508b49787a19e6bede3b8c04f1552f4d)
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
            check_type(argname="argument annotations", value=annotations, expected_type=type_hints["annotations"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_values is not None:
            self._values["additional_values"] = additional_values
        if annotations is not None:
            self._values["annotations"] = annotations
        if enabled is not None:
            self._values["enabled"] = enabled

    @builtins.property
    def additional_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: VaultServerServiceStandby#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def annotations(self) -> typing.Any:
        '''
        :schema: VaultServerServiceStandby#annotations
        '''
        result = self._values.get("annotations")
        return typing.cast(typing.Any, result)

    @builtins.property
    def enabled(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: VaultServerServiceStandby#enabled
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VaultServerServiceStandby(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="vault.VaultServerStandalone",
    jsii_struct_bases=[],
    name_mapping={
        "additional_values": "additionalValues",
        "config": "config",
        "enabled": "enabled",
    },
)
class VaultServerStandalone:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        config: typing.Any = None,
        enabled: typing.Any = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.
        :param config: 
        :param enabled: 

        :schema: VaultServerStandalone
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__18e1b632b45959500760d9c0d6764a164b6ce3293c8c2b7cb3c7b1752e1d9ae5)
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
            check_type(argname="argument config", value=config, expected_type=type_hints["config"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_values is not None:
            self._values["additional_values"] = additional_values
        if config is not None:
            self._values["config"] = config
        if enabled is not None:
            self._values["enabled"] = enabled

    @builtins.property
    def additional_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: VaultServerStandalone#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def config(self) -> typing.Any:
        '''
        :schema: VaultServerStandalone#config
        '''
        result = self._values.get("config")
        return typing.cast(typing.Any, result)

    @builtins.property
    def enabled(self) -> typing.Any:
        '''
        :schema: VaultServerStandalone#enabled
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Any, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VaultServerStandalone(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="vault.VaultServerStatefulSet",
    jsii_struct_bases=[],
    name_mapping={
        "additional_values": "additionalValues",
        "annotations": "annotations",
        "security_context": "securityContext",
    },
)
class VaultServerStatefulSet:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        annotations: typing.Any = None,
        security_context: typing.Optional[typing.Union["VaultServerStatefulSetSecurityContext", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.
        :param annotations: 
        :param security_context: 

        :schema: VaultServerStatefulSet
        '''
        if isinstance(security_context, dict):
            security_context = VaultServerStatefulSetSecurityContext(**security_context)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4159a4d95eadac43311409a9a6b067e1a709b081dd0a96ef64a950b016a164ee)
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
            check_type(argname="argument annotations", value=annotations, expected_type=type_hints["annotations"])
            check_type(argname="argument security_context", value=security_context, expected_type=type_hints["security_context"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_values is not None:
            self._values["additional_values"] = additional_values
        if annotations is not None:
            self._values["annotations"] = annotations
        if security_context is not None:
            self._values["security_context"] = security_context

    @builtins.property
    def additional_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: VaultServerStatefulSet#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def annotations(self) -> typing.Any:
        '''
        :schema: VaultServerStatefulSet#annotations
        '''
        result = self._values.get("annotations")
        return typing.cast(typing.Any, result)

    @builtins.property
    def security_context(
        self,
    ) -> typing.Optional["VaultServerStatefulSetSecurityContext"]:
        '''
        :schema: VaultServerStatefulSet#securityContext
        '''
        result = self._values.get("security_context")
        return typing.cast(typing.Optional["VaultServerStatefulSetSecurityContext"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VaultServerStatefulSet(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="vault.VaultServerStatefulSetSecurityContext",
    jsii_struct_bases=[],
    name_mapping={
        "additional_values": "additionalValues",
        "container": "container",
        "pod": "pod",
    },
)
class VaultServerStatefulSetSecurityContext:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        container: typing.Any = None,
        pod: typing.Any = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.
        :param container: 
        :param pod: 

        :schema: VaultServerStatefulSetSecurityContext
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ee4e307f5f030580a16ba8de81289536fa0b12050f21f787237de579c19f800d)
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
            check_type(argname="argument container", value=container, expected_type=type_hints["container"])
            check_type(argname="argument pod", value=pod, expected_type=type_hints["pod"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_values is not None:
            self._values["additional_values"] = additional_values
        if container is not None:
            self._values["container"] = container
        if pod is not None:
            self._values["pod"] = pod

    @builtins.property
    def additional_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: VaultServerStatefulSetSecurityContext#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def container(self) -> typing.Any:
        '''
        :schema: VaultServerStatefulSetSecurityContext#container
        '''
        result = self._values.get("container")
        return typing.cast(typing.Any, result)

    @builtins.property
    def pod(self) -> typing.Any:
        '''
        :schema: VaultServerStatefulSetSecurityContext#pod
        '''
        result = self._values.get("pod")
        return typing.cast(typing.Any, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VaultServerStatefulSetSecurityContext(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="vault.VaultServerTelemetry",
    jsii_struct_bases=[],
    name_mapping={
        "additional_values": "additionalValues",
        "prometheus_rules": "prometheusRules",
        "service_monitor": "serviceMonitor",
    },
)
class VaultServerTelemetry:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        prometheus_rules: typing.Optional[typing.Union["VaultServerTelemetryPrometheusRules", typing.Dict[builtins.str, typing.Any]]] = None,
        service_monitor: typing.Optional[typing.Union["VaultServerTelemetryServiceMonitor", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.
        :param prometheus_rules: 
        :param service_monitor: 

        :schema: VaultServerTelemetry
        '''
        if isinstance(prometheus_rules, dict):
            prometheus_rules = VaultServerTelemetryPrometheusRules(**prometheus_rules)
        if isinstance(service_monitor, dict):
            service_monitor = VaultServerTelemetryServiceMonitor(**service_monitor)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c45e3527da9225ec164f27d6ae274dd492ae43338f9d0b29c0bd578cf60e0a71)
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
            check_type(argname="argument prometheus_rules", value=prometheus_rules, expected_type=type_hints["prometheus_rules"])
            check_type(argname="argument service_monitor", value=service_monitor, expected_type=type_hints["service_monitor"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_values is not None:
            self._values["additional_values"] = additional_values
        if prometheus_rules is not None:
            self._values["prometheus_rules"] = prometheus_rules
        if service_monitor is not None:
            self._values["service_monitor"] = service_monitor

    @builtins.property
    def additional_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: VaultServerTelemetry#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def prometheus_rules(
        self,
    ) -> typing.Optional["VaultServerTelemetryPrometheusRules"]:
        '''
        :schema: VaultServerTelemetry#prometheusRules
        '''
        result = self._values.get("prometheus_rules")
        return typing.cast(typing.Optional["VaultServerTelemetryPrometheusRules"], result)

    @builtins.property
    def service_monitor(self) -> typing.Optional["VaultServerTelemetryServiceMonitor"]:
        '''
        :schema: VaultServerTelemetry#serviceMonitor
        '''
        result = self._values.get("service_monitor")
        return typing.cast(typing.Optional["VaultServerTelemetryServiceMonitor"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VaultServerTelemetry(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="vault.VaultServerTelemetryPrometheusRules",
    jsii_struct_bases=[],
    name_mapping={
        "additional_values": "additionalValues",
        "enabled": "enabled",
        "rules": "rules",
        "selectors": "selectors",
    },
)
class VaultServerTelemetryPrometheusRules:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        enabled: typing.Optional[builtins.bool] = None,
        rules: typing.Optional[typing.Sequence[typing.Any]] = None,
        selectors: typing.Any = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.
        :param enabled: 
        :param rules: 
        :param selectors: 

        :schema: VaultServerTelemetryPrometheusRules
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5dad67c31e83e3c8f7e424646f03529d1d72a8f80b1b9467904d0675e8235a34)
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument rules", value=rules, expected_type=type_hints["rules"])
            check_type(argname="argument selectors", value=selectors, expected_type=type_hints["selectors"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_values is not None:
            self._values["additional_values"] = additional_values
        if enabled is not None:
            self._values["enabled"] = enabled
        if rules is not None:
            self._values["rules"] = rules
        if selectors is not None:
            self._values["selectors"] = selectors

    @builtins.property
    def additional_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: VaultServerTelemetryPrometheusRules#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def enabled(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: VaultServerTelemetryPrometheusRules#enabled
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def rules(self) -> typing.Optional[typing.List[typing.Any]]:
        '''
        :schema: VaultServerTelemetryPrometheusRules#rules
        '''
        result = self._values.get("rules")
        return typing.cast(typing.Optional[typing.List[typing.Any]], result)

    @builtins.property
    def selectors(self) -> typing.Any:
        '''
        :schema: VaultServerTelemetryPrometheusRules#selectors
        '''
        result = self._values.get("selectors")
        return typing.cast(typing.Any, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VaultServerTelemetryPrometheusRules(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="vault.VaultServerTelemetryServiceMonitor",
    jsii_struct_bases=[],
    name_mapping={
        "additional_values": "additionalValues",
        "authorization": "authorization",
        "enabled": "enabled",
        "interval": "interval",
        "scrape_timeout": "scrapeTimeout",
        "selectors": "selectors",
        "tls_config": "tlsConfig",
    },
)
class VaultServerTelemetryServiceMonitor:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        authorization: typing.Any = None,
        enabled: typing.Optional[builtins.bool] = None,
        interval: typing.Optional[builtins.str] = None,
        scrape_timeout: typing.Optional[builtins.str] = None,
        selectors: typing.Any = None,
        tls_config: typing.Any = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.
        :param authorization: 
        :param enabled: 
        :param interval: 
        :param scrape_timeout: 
        :param selectors: 
        :param tls_config: 

        :schema: VaultServerTelemetryServiceMonitor
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a9eb99b9564a47d1a9e937669bfbeadae798865686a0d64863eb181b63b05308)
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
            check_type(argname="argument authorization", value=authorization, expected_type=type_hints["authorization"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument interval", value=interval, expected_type=type_hints["interval"])
            check_type(argname="argument scrape_timeout", value=scrape_timeout, expected_type=type_hints["scrape_timeout"])
            check_type(argname="argument selectors", value=selectors, expected_type=type_hints["selectors"])
            check_type(argname="argument tls_config", value=tls_config, expected_type=type_hints["tls_config"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_values is not None:
            self._values["additional_values"] = additional_values
        if authorization is not None:
            self._values["authorization"] = authorization
        if enabled is not None:
            self._values["enabled"] = enabled
        if interval is not None:
            self._values["interval"] = interval
        if scrape_timeout is not None:
            self._values["scrape_timeout"] = scrape_timeout
        if selectors is not None:
            self._values["selectors"] = selectors
        if tls_config is not None:
            self._values["tls_config"] = tls_config

    @builtins.property
    def additional_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: VaultServerTelemetryServiceMonitor#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def authorization(self) -> typing.Any:
        '''
        :schema: VaultServerTelemetryServiceMonitor#authorization
        '''
        result = self._values.get("authorization")
        return typing.cast(typing.Any, result)

    @builtins.property
    def enabled(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: VaultServerTelemetryServiceMonitor#enabled
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def interval(self) -> typing.Optional[builtins.str]:
        '''
        :schema: VaultServerTelemetryServiceMonitor#interval
        '''
        result = self._values.get("interval")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def scrape_timeout(self) -> typing.Optional[builtins.str]:
        '''
        :schema: VaultServerTelemetryServiceMonitor#scrapeTimeout
        '''
        result = self._values.get("scrape_timeout")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def selectors(self) -> typing.Any:
        '''
        :schema: VaultServerTelemetryServiceMonitor#selectors
        '''
        result = self._values.get("selectors")
        return typing.cast(typing.Any, result)

    @builtins.property
    def tls_config(self) -> typing.Any:
        '''
        :schema: VaultServerTelemetryServiceMonitor#tlsConfig
        '''
        result = self._values.get("tls_config")
        return typing.cast(typing.Any, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VaultServerTelemetryServiceMonitor(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="vault.VaultUi",
    jsii_struct_bases=[],
    name_mapping={
        "active_vault_pod_only": "activeVaultPodOnly",
        "additional_values": "additionalValues",
        "annotations": "annotations",
        "enabled": "enabled",
        "external_port": "externalPort",
        "external_traffic_policy": "externalTrafficPolicy",
        "publish_not_ready_addresses": "publishNotReadyAddresses",
        "service_ip_families": "serviceIpFamilies",
        "service_ip_family_policy": "serviceIpFamilyPolicy",
        "service_node_port": "serviceNodePort",
        "service_type": "serviceType",
        "target_port": "targetPort",
    },
)
class VaultUi:
    def __init__(
        self,
        *,
        active_vault_pod_only: typing.Optional[builtins.bool] = None,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        annotations: typing.Any = None,
        enabled: typing.Any = None,
        external_port: typing.Optional[jsii.Number] = None,
        external_traffic_policy: typing.Optional[builtins.str] = None,
        publish_not_ready_addresses: typing.Optional[builtins.bool] = None,
        service_ip_families: typing.Optional[typing.Sequence[typing.Any]] = None,
        service_ip_family_policy: typing.Optional[builtins.str] = None,
        service_node_port: typing.Optional[jsii.Number] = None,
        service_type: typing.Optional[builtins.str] = None,
        target_port: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param active_vault_pod_only: 
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.
        :param annotations: 
        :param enabled: 
        :param external_port: 
        :param external_traffic_policy: 
        :param publish_not_ready_addresses: 
        :param service_ip_families: 
        :param service_ip_family_policy: 
        :param service_node_port: 
        :param service_type: 
        :param target_port: 

        :schema: VaultUi
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__06efc428540cbd6c7d538a7f9f2c0dc5424c0b781f95757020a063a84447ccab)
            check_type(argname="argument active_vault_pod_only", value=active_vault_pod_only, expected_type=type_hints["active_vault_pod_only"])
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
            check_type(argname="argument annotations", value=annotations, expected_type=type_hints["annotations"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument external_port", value=external_port, expected_type=type_hints["external_port"])
            check_type(argname="argument external_traffic_policy", value=external_traffic_policy, expected_type=type_hints["external_traffic_policy"])
            check_type(argname="argument publish_not_ready_addresses", value=publish_not_ready_addresses, expected_type=type_hints["publish_not_ready_addresses"])
            check_type(argname="argument service_ip_families", value=service_ip_families, expected_type=type_hints["service_ip_families"])
            check_type(argname="argument service_ip_family_policy", value=service_ip_family_policy, expected_type=type_hints["service_ip_family_policy"])
            check_type(argname="argument service_node_port", value=service_node_port, expected_type=type_hints["service_node_port"])
            check_type(argname="argument service_type", value=service_type, expected_type=type_hints["service_type"])
            check_type(argname="argument target_port", value=target_port, expected_type=type_hints["target_port"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if active_vault_pod_only is not None:
            self._values["active_vault_pod_only"] = active_vault_pod_only
        if additional_values is not None:
            self._values["additional_values"] = additional_values
        if annotations is not None:
            self._values["annotations"] = annotations
        if enabled is not None:
            self._values["enabled"] = enabled
        if external_port is not None:
            self._values["external_port"] = external_port
        if external_traffic_policy is not None:
            self._values["external_traffic_policy"] = external_traffic_policy
        if publish_not_ready_addresses is not None:
            self._values["publish_not_ready_addresses"] = publish_not_ready_addresses
        if service_ip_families is not None:
            self._values["service_ip_families"] = service_ip_families
        if service_ip_family_policy is not None:
            self._values["service_ip_family_policy"] = service_ip_family_policy
        if service_node_port is not None:
            self._values["service_node_port"] = service_node_port
        if service_type is not None:
            self._values["service_type"] = service_type
        if target_port is not None:
            self._values["target_port"] = target_port

    @builtins.property
    def active_vault_pod_only(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: VaultUi#activeVaultPodOnly
        '''
        result = self._values.get("active_vault_pod_only")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def additional_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: VaultUi#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def annotations(self) -> typing.Any:
        '''
        :schema: VaultUi#annotations
        '''
        result = self._values.get("annotations")
        return typing.cast(typing.Any, result)

    @builtins.property
    def enabled(self) -> typing.Any:
        '''
        :schema: VaultUi#enabled
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Any, result)

    @builtins.property
    def external_port(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: VaultUi#externalPort
        '''
        result = self._values.get("external_port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def external_traffic_policy(self) -> typing.Optional[builtins.str]:
        '''
        :schema: VaultUi#externalTrafficPolicy
        '''
        result = self._values.get("external_traffic_policy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def publish_not_ready_addresses(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: VaultUi#publishNotReadyAddresses
        '''
        result = self._values.get("publish_not_ready_addresses")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def service_ip_families(self) -> typing.Optional[typing.List[typing.Any]]:
        '''
        :schema: VaultUi#serviceIPFamilies
        '''
        result = self._values.get("service_ip_families")
        return typing.cast(typing.Optional[typing.List[typing.Any]], result)

    @builtins.property
    def service_ip_family_policy(self) -> typing.Optional[builtins.str]:
        '''
        :schema: VaultUi#serviceIPFamilyPolicy
        '''
        result = self._values.get("service_ip_family_policy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def service_node_port(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: VaultUi#serviceNodePort
        '''
        result = self._values.get("service_node_port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def service_type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: VaultUi#serviceType
        '''
        result = self._values.get("service_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def target_port(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: VaultUi#targetPort
        '''
        result = self._values.get("target_port")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VaultUi(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="vault.VaultValues",
    jsii_struct_bases=[],
    name_mapping={
        "additional_values": "additionalValues",
        "csi": "csi",
        "global_": "global",
        "injector": "injector",
        "server": "server",
        "server_telemetry": "serverTelemetry",
        "ui": "ui",
    },
)
class VaultValues:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        csi: typing.Optional[typing.Union[VaultCsi, typing.Dict[builtins.str, typing.Any]]] = None,
        global_: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        injector: typing.Optional[typing.Union[VaultInjector, typing.Dict[builtins.str, typing.Any]]] = None,
        server: typing.Optional[typing.Union[VaultServer, typing.Dict[builtins.str, typing.Any]]] = None,
        server_telemetry: typing.Optional[typing.Union[VaultServerTelemetry, typing.Dict[builtins.str, typing.Any]]] = None,
        ui: typing.Optional[typing.Union[VaultUi, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.
        :param csi: 
        :param global_: 
        :param injector: 
        :param server: 
        :param server_telemetry: 
        :param ui: 

        :schema: vault
        '''
        if isinstance(csi, dict):
            csi = VaultCsi(**csi)
        if isinstance(injector, dict):
            injector = VaultInjector(**injector)
        if isinstance(server, dict):
            server = VaultServer(**server)
        if isinstance(server_telemetry, dict):
            server_telemetry = VaultServerTelemetry(**server_telemetry)
        if isinstance(ui, dict):
            ui = VaultUi(**ui)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__53f6a35275cf616388f00cf31ba76d20faade7b25d5439c2a15cd7ac40f0cc94)
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
            check_type(argname="argument csi", value=csi, expected_type=type_hints["csi"])
            check_type(argname="argument global_", value=global_, expected_type=type_hints["global_"])
            check_type(argname="argument injector", value=injector, expected_type=type_hints["injector"])
            check_type(argname="argument server", value=server, expected_type=type_hints["server"])
            check_type(argname="argument server_telemetry", value=server_telemetry, expected_type=type_hints["server_telemetry"])
            check_type(argname="argument ui", value=ui, expected_type=type_hints["ui"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_values is not None:
            self._values["additional_values"] = additional_values
        if csi is not None:
            self._values["csi"] = csi
        if global_ is not None:
            self._values["global_"] = global_
        if injector is not None:
            self._values["injector"] = injector
        if server is not None:
            self._values["server"] = server
        if server_telemetry is not None:
            self._values["server_telemetry"] = server_telemetry
        if ui is not None:
            self._values["ui"] = ui

    @builtins.property
    def additional_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: vault#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def csi(self) -> typing.Optional[VaultCsi]:
        '''
        :schema: vault#csi
        '''
        result = self._values.get("csi")
        return typing.cast(typing.Optional[VaultCsi], result)

    @builtins.property
    def global_(self) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''
        :schema: vault#global
        '''
        result = self._values.get("global_")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def injector(self) -> typing.Optional[VaultInjector]:
        '''
        :schema: vault#injector
        '''
        result = self._values.get("injector")
        return typing.cast(typing.Optional[VaultInjector], result)

    @builtins.property
    def server(self) -> typing.Optional[VaultServer]:
        '''
        :schema: vault#server
        '''
        result = self._values.get("server")
        return typing.cast(typing.Optional[VaultServer], result)

    @builtins.property
    def server_telemetry(self) -> typing.Optional[VaultServerTelemetry]:
        '''
        :schema: vault#serverTelemetry
        '''
        result = self._values.get("server_telemetry")
        return typing.cast(typing.Optional[VaultServerTelemetry], result)

    @builtins.property
    def ui(self) -> typing.Optional[VaultUi]:
        '''
        :schema: vault#ui
        '''
        result = self._values.get("ui")
        return typing.cast(typing.Optional[VaultUi], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VaultValues(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "Vault",
    "VaultCsi",
    "VaultCsiAgent",
    "VaultCsiAgentImage",
    "VaultCsiDaemonSet",
    "VaultCsiDaemonSetSecurityContext",
    "VaultCsiDaemonSetUpdateStrategy",
    "VaultCsiImage",
    "VaultCsiLivenessProbe",
    "VaultCsiPod",
    "VaultCsiReadinessProbe",
    "VaultCsiServiceAccount",
    "VaultInjector",
    "VaultInjectorAgentDefaults",
    "VaultInjectorAgentDefaultsTemplateConfig",
    "VaultInjectorAgentImage",
    "VaultInjectorCerts",
    "VaultInjectorImage",
    "VaultInjectorLeaderElector",
    "VaultInjectorLivenessProbe",
    "VaultInjectorMetrics",
    "VaultInjectorReadinessProbe",
    "VaultInjectorSecurityContext",
    "VaultInjectorService",
    "VaultInjectorServiceAccount",
    "VaultInjectorStartupProbe",
    "VaultInjectorWebhook",
    "VaultProps",
    "VaultServer",
    "VaultServerAuditStorage",
    "VaultServerAuthDelegator",
    "VaultServerDataStorage",
    "VaultServerDev",
    "VaultServerEnterpriseLicense",
    "VaultServerHa",
    "VaultServerHaDisruptionBudget",
    "VaultServerHaRaft",
    "VaultServerImage",
    "VaultServerIngress",
    "VaultServerIngressHosts",
    "VaultServerLivenessProbe",
    "VaultServerNetworkPolicy",
    "VaultServerPersistentVolumeClaimRetentionPolicy",
    "VaultServerReadinessProbe",
    "VaultServerRoute",
    "VaultServerService",
    "VaultServerServiceAccount",
    "VaultServerServiceAccountServiceDiscovery",
    "VaultServerServiceActive",
    "VaultServerServiceInstanceSelector",
    "VaultServerServiceStandby",
    "VaultServerStandalone",
    "VaultServerStatefulSet",
    "VaultServerStatefulSetSecurityContext",
    "VaultServerTelemetry",
    "VaultServerTelemetryPrometheusRules",
    "VaultServerTelemetryServiceMonitor",
    "VaultUi",
    "VaultValues",
]

publication.publish()

def _typecheckingstub__c99521cdcd5598c8561c8003f5aa0e03085b813ce11215d8c685ebd55a3cab8d(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    helm_executable: typing.Optional[builtins.str] = None,
    helm_flags: typing.Optional[typing.Sequence[builtins.str]] = None,
    namespace: typing.Optional[builtins.str] = None,
    release_name: typing.Optional[builtins.str] = None,
    values: typing.Optional[typing.Union[VaultValues, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eb3cfc5797c505412f97eb99522136e80ea63c882fa1c85bd1534dc1b1949238(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    agent: typing.Optional[typing.Union[VaultCsiAgent, typing.Dict[builtins.str, typing.Any]]] = None,
    daemon_set: typing.Optional[typing.Union[VaultCsiDaemonSet, typing.Dict[builtins.str, typing.Any]]] = None,
    debug: typing.Optional[builtins.bool] = None,
    enabled: typing.Any = None,
    extra_args: typing.Optional[typing.Sequence[typing.Any]] = None,
    hmac_secret_name: typing.Optional[builtins.str] = None,
    host_network: typing.Optional[builtins.bool] = None,
    image: typing.Optional[typing.Union[VaultCsiImage, typing.Dict[builtins.str, typing.Any]]] = None,
    liveness_probe: typing.Optional[typing.Union[VaultCsiLivenessProbe, typing.Dict[builtins.str, typing.Any]]] = None,
    log_level: typing.Optional[builtins.str] = None,
    pod: typing.Optional[typing.Union[VaultCsiPod, typing.Dict[builtins.str, typing.Any]]] = None,
    priority_class_name: typing.Optional[builtins.str] = None,
    readiness_probe: typing.Optional[typing.Union[VaultCsiReadinessProbe, typing.Dict[builtins.str, typing.Any]]] = None,
    resources: typing.Any = None,
    service_account: typing.Optional[typing.Union[VaultCsiServiceAccount, typing.Dict[builtins.str, typing.Any]]] = None,
    volume_mounts: typing.Optional[typing.Sequence[typing.Any]] = None,
    volumes: typing.Optional[typing.Sequence[typing.Any]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__690de3ce0a44178a547711fad97b34116bf025eaa26d164e1bf37f091c57c7a4(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    enabled: typing.Optional[builtins.bool] = None,
    extra_args: typing.Optional[typing.Sequence[typing.Any]] = None,
    image: typing.Optional[typing.Union[VaultCsiAgentImage, typing.Dict[builtins.str, typing.Any]]] = None,
    log_format: typing.Optional[builtins.str] = None,
    log_level: typing.Optional[builtins.str] = None,
    resources: typing.Any = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5edb9bf8fe04dbac9f643a4daef3c002f026ab0d1e8ada9193595080bc90853c(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    pull_policy: typing.Optional[builtins.str] = None,
    repository: typing.Optional[builtins.str] = None,
    tag: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e597c736e8d7927b2369e5791cf508a392cf09eb1a2c1db663cb0d2a5df0ddf7(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    annotations: typing.Any = None,
    extra_labels: typing.Any = None,
    kubelet_root_dir: typing.Optional[builtins.str] = None,
    providers_dir: typing.Optional[builtins.str] = None,
    security_context: typing.Optional[typing.Union[VaultCsiDaemonSetSecurityContext, typing.Dict[builtins.str, typing.Any]]] = None,
    update_strategy: typing.Optional[typing.Union[VaultCsiDaemonSetUpdateStrategy, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__35220034df45f77f18320222defd5c608c761d2b184d88eca911cc2e4239cbf4(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    container: typing.Any = None,
    pod: typing.Any = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3154182529948dde2e8d0a88d335f923a6e5facfd2d8583c777b31f0b180d72e(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    max_unavailable: typing.Optional[builtins.str] = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__104a4d6b24a0faa09eb09ecf1c1c0457a749ee804cae00ab3a076ded85e0d05c(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    pull_policy: typing.Optional[builtins.str] = None,
    repository: typing.Optional[builtins.str] = None,
    tag: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b0b372a4df8cd386e5e9ae3168dbb804f461e52f17bb1f86638b598f15fca8c0(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    failure_threshold: typing.Optional[jsii.Number] = None,
    initial_delay_seconds: typing.Optional[jsii.Number] = None,
    period_seconds: typing.Optional[jsii.Number] = None,
    success_threshold: typing.Optional[jsii.Number] = None,
    timeout_seconds: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bbcf2f0f1ac2f575f8be9d45a001b987e27e835f0e587a9e0090ed3f51eb2a12(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    affinity: typing.Any = None,
    annotations: typing.Any = None,
    extra_labels: typing.Any = None,
    node_selector: typing.Any = None,
    tolerations: typing.Any = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c59e9ff042ba7058e6b8f7d1e02c2c22f94607384c141d16f4554100fd884601(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    failure_threshold: typing.Optional[jsii.Number] = None,
    initial_delay_seconds: typing.Optional[jsii.Number] = None,
    period_seconds: typing.Optional[jsii.Number] = None,
    success_threshold: typing.Optional[jsii.Number] = None,
    timeout_seconds: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4778e3b6220ebd049d4955a2000aceb362406c165c9cd7ee9f56ca621aa7b0ab(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    annotations: typing.Any = None,
    extra_labels: typing.Any = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cee6dc0abd85a66c574529991e8a568c04956118370ee82269d2e6d03f2fc585(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    affinity: typing.Any = None,
    agent_defaults: typing.Optional[typing.Union[VaultInjectorAgentDefaults, typing.Dict[builtins.str, typing.Any]]] = None,
    agent_image: typing.Optional[typing.Union[VaultInjectorAgentImage, typing.Dict[builtins.str, typing.Any]]] = None,
    annotations: typing.Any = None,
    auth_path: typing.Optional[builtins.str] = None,
    certs: typing.Optional[typing.Union[VaultInjectorCerts, typing.Dict[builtins.str, typing.Any]]] = None,
    enabled: typing.Any = None,
    external_vault_addr: typing.Optional[builtins.str] = None,
    extra_environment_vars: typing.Any = None,
    extra_labels: typing.Any = None,
    failure_policy: typing.Optional[builtins.str] = None,
    host_network: typing.Optional[builtins.bool] = None,
    image: typing.Optional[typing.Union[VaultInjectorImage, typing.Dict[builtins.str, typing.Any]]] = None,
    leader_elector: typing.Optional[typing.Union[VaultInjectorLeaderElector, typing.Dict[builtins.str, typing.Any]]] = None,
    liveness_probe: typing.Optional[typing.Union[VaultInjectorLivenessProbe, typing.Dict[builtins.str, typing.Any]]] = None,
    log_format: typing.Optional[builtins.str] = None,
    log_level: typing.Optional[builtins.str] = None,
    metrics: typing.Optional[typing.Union[VaultInjectorMetrics, typing.Dict[builtins.str, typing.Any]]] = None,
    namespace_selector: typing.Any = None,
    node_selector: typing.Any = None,
    object_selector: typing.Any = None,
    pod_disruption_budget: typing.Any = None,
    port: typing.Optional[jsii.Number] = None,
    priority_class_name: typing.Optional[builtins.str] = None,
    readiness_probe: typing.Optional[typing.Union[VaultInjectorReadinessProbe, typing.Dict[builtins.str, typing.Any]]] = None,
    replicas: typing.Optional[jsii.Number] = None,
    resources: typing.Any = None,
    revoke_on_shutdown: typing.Optional[builtins.bool] = None,
    security_context: typing.Optional[typing.Union[VaultInjectorSecurityContext, typing.Dict[builtins.str, typing.Any]]] = None,
    service: typing.Optional[typing.Union[VaultInjectorService, typing.Dict[builtins.str, typing.Any]]] = None,
    service_account: typing.Optional[typing.Union[VaultInjectorServiceAccount, typing.Dict[builtins.str, typing.Any]]] = None,
    startup_probe: typing.Optional[typing.Union[VaultInjectorStartupProbe, typing.Dict[builtins.str, typing.Any]]] = None,
    strategy: typing.Any = None,
    tolerations: typing.Any = None,
    topology_spread_constraints: typing.Any = None,
    webhook: typing.Optional[typing.Union[VaultInjectorWebhook, typing.Dict[builtins.str, typing.Any]]] = None,
    webhook_annotations: typing.Any = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__51b4fe880e8893046d0a8b11c912ef33be6187b434ec0c25eb05b1201dd91bb3(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    cpu_limit: typing.Optional[builtins.str] = None,
    cpu_request: typing.Optional[builtins.str] = None,
    ephemeral_limit: typing.Optional[builtins.str] = None,
    ephemeral_request: typing.Optional[builtins.str] = None,
    mem_limit: typing.Optional[builtins.str] = None,
    mem_request: typing.Optional[builtins.str] = None,
    template: typing.Optional[builtins.str] = None,
    template_config: typing.Optional[typing.Union[VaultInjectorAgentDefaultsTemplateConfig, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0b695a03fde26ac4adce6f3521db23e50f3690fa72a9382c1e7f675eaaad83c8(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    exit_on_retry_failure: typing.Optional[builtins.bool] = None,
    static_secret_render_interval: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af8a927cb1ea564d82d127069666af1234fe0c65b94f2af0b0d3bd3d4016bc17(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    repository: typing.Optional[builtins.str] = None,
    tag: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__62d62c806a3ca9c6c4fe124a15dc61a274ef728aeec34412374164af440fe54c(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    ca_bundle: typing.Optional[builtins.str] = None,
    cert_name: typing.Optional[builtins.str] = None,
    key_name: typing.Optional[builtins.str] = None,
    secret_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__52536a6ddc366ef4a85b18165e1782de1d0d3ee32a4f0931580deb5932989fa5(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    pull_policy: typing.Optional[builtins.str] = None,
    repository: typing.Optional[builtins.str] = None,
    tag: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c6a258c1d4a6af48484adc17c41c686ecc67607f82897b55514535435e5c3c68(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    enabled: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2e4c4da16af46227522996a8354af8ae5d2b75c3b783771c5f46c3ac673b94cd(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    failure_threshold: typing.Optional[jsii.Number] = None,
    initial_delay_seconds: typing.Optional[jsii.Number] = None,
    period_seconds: typing.Optional[jsii.Number] = None,
    success_threshold: typing.Optional[jsii.Number] = None,
    timeout_seconds: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1653b9a00c4aff25d127c12173f92606f0259c1ad17cc2944057b0ad395f2b75(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    enabled: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fcd88cdfeb775e3076ee4a8865d9dfba0bb474e43b3eb4d8a8c9e8c4c3f68104(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    failure_threshold: typing.Optional[jsii.Number] = None,
    initial_delay_seconds: typing.Optional[jsii.Number] = None,
    period_seconds: typing.Optional[jsii.Number] = None,
    success_threshold: typing.Optional[jsii.Number] = None,
    timeout_seconds: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__93682a70d7ea342aa58eb8fc794987c419d207779748cd3b9dca833af6a4d9a9(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    container: typing.Any = None,
    pod: typing.Any = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5d074e28fdcd505c535aede327d5b429aaa337a41f1f69f1f57b942363357d73(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    annotations: typing.Any = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b1e932448512bbaad52eb94420530e86d4be7ae06c4e32c3325c31b098b59d67(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    annotations: typing.Any = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3d99800e278ee9172c01b656f46a1897ac953c43ea5e73b96df606c202018a69(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    failure_threshold: typing.Optional[jsii.Number] = None,
    initial_delay_seconds: typing.Optional[jsii.Number] = None,
    period_seconds: typing.Optional[jsii.Number] = None,
    success_threshold: typing.Optional[jsii.Number] = None,
    timeout_seconds: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5eefdf91d97ff96a44dae7a3d9bf3e8813e821227a2359e3ecda1fcb0470040b(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    annotations: typing.Any = None,
    failure_policy: typing.Optional[builtins.str] = None,
    match_policy: typing.Optional[builtins.str] = None,
    namespace_selector: typing.Any = None,
    object_selector: typing.Any = None,
    timeout_seconds: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3516748a8734cf1c44155b30bbfa1b0d45edd6e8cd28d2feaf6c783d30b654a2(
    *,
    helm_executable: typing.Optional[builtins.str] = None,
    helm_flags: typing.Optional[typing.Sequence[builtins.str]] = None,
    namespace: typing.Optional[builtins.str] = None,
    release_name: typing.Optional[builtins.str] = None,
    values: typing.Optional[typing.Union[VaultValues, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb5c6e8fee72dc5d759f67b5f13f2dbc50f027bbcf46286412f7ff8e16a1a726(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    affinity: typing.Any = None,
    annotations: typing.Any = None,
    audit_storage: typing.Optional[typing.Union[VaultServerAuditStorage, typing.Dict[builtins.str, typing.Any]]] = None,
    auth_delegator: typing.Optional[typing.Union[VaultServerAuthDelegator, typing.Dict[builtins.str, typing.Any]]] = None,
    data_storage: typing.Optional[typing.Union[VaultServerDataStorage, typing.Dict[builtins.str, typing.Any]]] = None,
    dev: typing.Optional[typing.Union[VaultServerDev, typing.Dict[builtins.str, typing.Any]]] = None,
    enabled: typing.Any = None,
    enterprise_license: typing.Optional[typing.Union[VaultServerEnterpriseLicense, typing.Dict[builtins.str, typing.Any]]] = None,
    extra_args: typing.Optional[builtins.str] = None,
    extra_containers: typing.Optional[typing.Sequence[typing.Any]] = None,
    extra_environment_vars: typing.Any = None,
    extra_init_containers: typing.Optional[typing.Sequence[typing.Any]] = None,
    extra_labels: typing.Any = None,
    extra_ports: typing.Optional[typing.Sequence[typing.Any]] = None,
    extra_secret_environment_vars: typing.Optional[typing.Sequence[typing.Any]] = None,
    extra_volumes: typing.Optional[typing.Sequence[typing.Any]] = None,
    ha: typing.Optional[typing.Union[VaultServerHa, typing.Dict[builtins.str, typing.Any]]] = None,
    host_aliases: typing.Optional[typing.Sequence[typing.Any]] = None,
    host_network: typing.Optional[builtins.bool] = None,
    image: typing.Optional[typing.Union[VaultServerImage, typing.Dict[builtins.str, typing.Any]]] = None,
    include_config_annotation: typing.Optional[builtins.bool] = None,
    ingress: typing.Optional[typing.Union[VaultServerIngress, typing.Dict[builtins.str, typing.Any]]] = None,
    liveness_probe: typing.Optional[typing.Union[VaultServerLivenessProbe, typing.Dict[builtins.str, typing.Any]]] = None,
    log_format: typing.Optional[builtins.str] = None,
    log_level: typing.Optional[builtins.str] = None,
    network_policy: typing.Optional[typing.Union[VaultServerNetworkPolicy, typing.Dict[builtins.str, typing.Any]]] = None,
    node_selector: typing.Any = None,
    persistent_volume_claim_retention_policy: typing.Optional[typing.Union[VaultServerPersistentVolumeClaimRetentionPolicy, typing.Dict[builtins.str, typing.Any]]] = None,
    post_start: typing.Optional[typing.Sequence[typing.Any]] = None,
    pre_stop_sleep_seconds: typing.Optional[jsii.Number] = None,
    priority_class_name: typing.Optional[builtins.str] = None,
    readiness_probe: typing.Optional[typing.Union[VaultServerReadinessProbe, typing.Dict[builtins.str, typing.Any]]] = None,
    resources: typing.Any = None,
    route: typing.Optional[typing.Union[VaultServerRoute, typing.Dict[builtins.str, typing.Any]]] = None,
    service: typing.Optional[typing.Union[VaultServerService, typing.Dict[builtins.str, typing.Any]]] = None,
    service_account: typing.Optional[typing.Union[VaultServerServiceAccount, typing.Dict[builtins.str, typing.Any]]] = None,
    share_process_namespace: typing.Optional[builtins.bool] = None,
    standalone: typing.Optional[typing.Union[VaultServerStandalone, typing.Dict[builtins.str, typing.Any]]] = None,
    stateful_set: typing.Optional[typing.Union[VaultServerStatefulSet, typing.Dict[builtins.str, typing.Any]]] = None,
    termination_grace_period_seconds: typing.Optional[jsii.Number] = None,
    tolerations: typing.Any = None,
    topology_spread_constraints: typing.Any = None,
    update_strategy_type: typing.Optional[builtins.str] = None,
    volume_mounts: typing.Optional[typing.Sequence[typing.Any]] = None,
    volumes: typing.Optional[typing.Sequence[typing.Any]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__26f604d1e3fac6d4ef51fbf7522fcf3357c75d0ec693f8ca0496b3b2b3891026(
    *,
    access_mode: typing.Optional[builtins.str] = None,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    annotations: typing.Any = None,
    enabled: typing.Any = None,
    labels: typing.Any = None,
    mount_path: typing.Optional[builtins.str] = None,
    size: typing.Optional[builtins.str] = None,
    storage_class: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9d17299c62b642e66ed27f3bfc739abd73c55549a7fe2b6ba1a01951463169c7(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    enabled: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dc93d620ebfcadd63222313fd67c9eadcc11d526e8c5f1378be2e756cef1b8da(
    *,
    access_mode: typing.Optional[builtins.str] = None,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    annotations: typing.Any = None,
    enabled: typing.Any = None,
    labels: typing.Any = None,
    mount_path: typing.Optional[builtins.str] = None,
    size: typing.Optional[builtins.str] = None,
    storage_class: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b3c5936407a0ed1495db6e00b8044d1902d3993b67ec7a9a4c004a0e607115c9(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    dev_root_token: typing.Optional[builtins.str] = None,
    enabled: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__792a78e09c28dfc95fc6f611469d8b1c54f288b921a6ab0b50a2275a3686f1d3(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    secret_key: typing.Optional[builtins.str] = None,
    secret_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a85f5b50607467af77b8ac6eb3c03e0b74b08549d47782768b6d9839d6421216(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    api_addr: typing.Optional[builtins.str] = None,
    cluster_addr: typing.Optional[builtins.str] = None,
    config: typing.Any = None,
    disruption_budget: typing.Optional[typing.Union[VaultServerHaDisruptionBudget, typing.Dict[builtins.str, typing.Any]]] = None,
    enabled: typing.Optional[builtins.bool] = None,
    raft: typing.Optional[typing.Union[VaultServerHaRaft, typing.Dict[builtins.str, typing.Any]]] = None,
    replicas: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c4cdcbe702d2f0bd9e2935f65d1cc96c2f004ba04e1791a1ea1d076c32d118b7(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    enabled: typing.Optional[builtins.bool] = None,
    max_unavailable: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__41a2403a61c304b439ba6472e66794a9e0120a6b53ca2b3df820e85e2eea3db9(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    config: typing.Any = None,
    enabled: typing.Optional[builtins.bool] = None,
    set_node_id: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9b580c02f1c1bd2bb2f5fc2ec0a3aa261b9ea3d6061d248a1c57c7dcf9ebd3d0(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    pull_policy: typing.Optional[builtins.str] = None,
    repository: typing.Optional[builtins.str] = None,
    tag: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb1f8c9753a0338e9f81d02a6015fd381fc45e21d50f2f8f36225d4ef7cbb885(
    *,
    active_service: typing.Optional[builtins.bool] = None,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    annotations: typing.Any = None,
    enabled: typing.Optional[builtins.bool] = None,
    extra_paths: typing.Optional[typing.Sequence[typing.Any]] = None,
    hosts: typing.Optional[typing.Sequence[typing.Union[VaultServerIngressHosts, typing.Dict[builtins.str, typing.Any]]]] = None,
    ingress_class_name: typing.Optional[builtins.str] = None,
    labels: typing.Any = None,
    path_type: typing.Optional[builtins.str] = None,
    tls: typing.Optional[typing.Sequence[typing.Any]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__38e71b00967178ddfbcd045d0ad9d940f5ba833795a5dd8f5e8805d4a2bb40d0(
    *,
    host: typing.Optional[builtins.str] = None,
    paths: typing.Optional[typing.Sequence[typing.Any]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7fe9e4444d3e77702169191cdb83762bccdc93f49a00011433290313f3122979(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    enabled: typing.Optional[builtins.bool] = None,
    exec_command: typing.Optional[typing.Sequence[typing.Any]] = None,
    failure_threshold: typing.Optional[jsii.Number] = None,
    initial_delay_seconds: typing.Optional[jsii.Number] = None,
    path: typing.Optional[builtins.str] = None,
    period_seconds: typing.Optional[jsii.Number] = None,
    port: typing.Optional[jsii.Number] = None,
    success_threshold: typing.Optional[jsii.Number] = None,
    timeout_seconds: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fe312061004d7f526d33cf6835c8dbba0d8688c3ba7e40f517ad9995560fd0db(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    egress: typing.Optional[typing.Sequence[typing.Any]] = None,
    enabled: typing.Optional[builtins.bool] = None,
    ingress: typing.Optional[typing.Sequence[typing.Any]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__43acf80ad2563b040e3d648aa3f74c8d3030c26b523f05854687bf1f1b402ce5(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    when_deleted: typing.Optional[builtins.str] = None,
    when_scaled: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__74e65ef403a4182326fb82b2b1c46d75187549d986422f7ff3c51f2273de7981(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    enabled: typing.Optional[builtins.bool] = None,
    failure_threshold: typing.Optional[jsii.Number] = None,
    initial_delay_seconds: typing.Optional[jsii.Number] = None,
    period_seconds: typing.Optional[jsii.Number] = None,
    port: typing.Optional[jsii.Number] = None,
    success_threshold: typing.Optional[jsii.Number] = None,
    timeout_seconds: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__89e18f3aa62665bd680600a3136d7d680bd43c5b9baf6286330f2d0975b87f3a(
    *,
    active_service: typing.Optional[builtins.bool] = None,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    annotations: typing.Any = None,
    enabled: typing.Optional[builtins.bool] = None,
    host: typing.Optional[builtins.str] = None,
    labels: typing.Any = None,
    tls: typing.Any = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bff7c12ff40d9f13bc33b80103b5e0a8ca10e68d15db6b9bc6ff485a2868ed9a(
    *,
    active: typing.Optional[typing.Union[VaultServerServiceActive, typing.Dict[builtins.str, typing.Any]]] = None,
    active_node_port: typing.Optional[jsii.Number] = None,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    annotations: typing.Any = None,
    enabled: typing.Optional[builtins.bool] = None,
    external_traffic_policy: typing.Optional[builtins.str] = None,
    instance_selector: typing.Optional[typing.Union[VaultServerServiceInstanceSelector, typing.Dict[builtins.str, typing.Any]]] = None,
    ip_families: typing.Optional[typing.Sequence[typing.Any]] = None,
    ip_family_policy: typing.Optional[builtins.str] = None,
    node_port: typing.Optional[jsii.Number] = None,
    port: typing.Optional[jsii.Number] = None,
    publish_not_ready_addresses: typing.Optional[builtins.bool] = None,
    standby: typing.Optional[typing.Union[VaultServerServiceStandby, typing.Dict[builtins.str, typing.Any]]] = None,
    standby_node_port: typing.Optional[jsii.Number] = None,
    target_port: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__92e1c19011364670236a5f52837b99e4e01a47defadace2ea1a8a6632d6a9c21(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    annotations: typing.Any = None,
    create: typing.Optional[builtins.bool] = None,
    create_secret: typing.Optional[builtins.bool] = None,
    extra_labels: typing.Any = None,
    name: typing.Optional[builtins.str] = None,
    service_discovery: typing.Optional[typing.Union[VaultServerServiceAccountServiceDiscovery, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e21ed868d7176a05ef8f4dd0de8562a12365484f151b8b6bfb04c76a426723ff(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    enabled: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__07365ba54e29a927d1284608741bd095fb178f8cae81e04e1f9ae3bf1131086c(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    annotations: typing.Any = None,
    enabled: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2b56b3c6566ec85a23c195140771e621eddb7494b6c06ced27f00a4bb248f97b(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    enabled: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b4451e329a945bf5d5bb81c184630169508b49787a19e6bede3b8c04f1552f4d(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    annotations: typing.Any = None,
    enabled: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__18e1b632b45959500760d9c0d6764a164b6ce3293c8c2b7cb3c7b1752e1d9ae5(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    config: typing.Any = None,
    enabled: typing.Any = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4159a4d95eadac43311409a9a6b067e1a709b081dd0a96ef64a950b016a164ee(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    annotations: typing.Any = None,
    security_context: typing.Optional[typing.Union[VaultServerStatefulSetSecurityContext, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ee4e307f5f030580a16ba8de81289536fa0b12050f21f787237de579c19f800d(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    container: typing.Any = None,
    pod: typing.Any = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c45e3527da9225ec164f27d6ae274dd492ae43338f9d0b29c0bd578cf60e0a71(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    prometheus_rules: typing.Optional[typing.Union[VaultServerTelemetryPrometheusRules, typing.Dict[builtins.str, typing.Any]]] = None,
    service_monitor: typing.Optional[typing.Union[VaultServerTelemetryServiceMonitor, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5dad67c31e83e3c8f7e424646f03529d1d72a8f80b1b9467904d0675e8235a34(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    enabled: typing.Optional[builtins.bool] = None,
    rules: typing.Optional[typing.Sequence[typing.Any]] = None,
    selectors: typing.Any = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a9eb99b9564a47d1a9e937669bfbeadae798865686a0d64863eb181b63b05308(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    authorization: typing.Any = None,
    enabled: typing.Optional[builtins.bool] = None,
    interval: typing.Optional[builtins.str] = None,
    scrape_timeout: typing.Optional[builtins.str] = None,
    selectors: typing.Any = None,
    tls_config: typing.Any = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__06efc428540cbd6c7d538a7f9f2c0dc5424c0b781f95757020a063a84447ccab(
    *,
    active_vault_pod_only: typing.Optional[builtins.bool] = None,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    annotations: typing.Any = None,
    enabled: typing.Any = None,
    external_port: typing.Optional[jsii.Number] = None,
    external_traffic_policy: typing.Optional[builtins.str] = None,
    publish_not_ready_addresses: typing.Optional[builtins.bool] = None,
    service_ip_families: typing.Optional[typing.Sequence[typing.Any]] = None,
    service_ip_family_policy: typing.Optional[builtins.str] = None,
    service_node_port: typing.Optional[jsii.Number] = None,
    service_type: typing.Optional[builtins.str] = None,
    target_port: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__53f6a35275cf616388f00cf31ba76d20faade7b25d5439c2a15cd7ac40f0cc94(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    csi: typing.Optional[typing.Union[VaultCsi, typing.Dict[builtins.str, typing.Any]]] = None,
    global_: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    injector: typing.Optional[typing.Union[VaultInjector, typing.Dict[builtins.str, typing.Any]]] = None,
    server: typing.Optional[typing.Union[VaultServer, typing.Dict[builtins.str, typing.Any]]] = None,
    server_telemetry: typing.Optional[typing.Union[VaultServerTelemetry, typing.Dict[builtins.str, typing.Any]]] = None,
    ui: typing.Optional[typing.Union[VaultUi, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass
