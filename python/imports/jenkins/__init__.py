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


class Jenkins(
    _constructs_77d1e7e8.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="jenkins.Jenkins",
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
        values: typing.Optional[typing.Union["JenkinsValues", typing.Dict[builtins.str, typing.Any]]] = None,
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
            type_hints = typing.get_type_hints(_typecheckingstub__b578a09bb9c61f8b4b01ea5f17ebf3048b7442f70e4f2bd4d3012de973bedee6)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = JenkinsProps(
            helm_executable=helm_executable,
            helm_flags=helm_flags,
            namespace=namespace,
            release_name=release_name,
            values=values,
        )

        jsii.create(self.__class__, self, [scope, id, props])


@jsii.data_type(
    jsii_type="jenkins.JenkinsIngress",
    jsii_struct_bases=[],
    name_mapping={
        "additional_values": "additionalValues",
        "enabled": "enabled",
        "hostname": "hostname",
    },
)
class JenkinsIngress:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        enabled: typing.Optional[builtins.bool] = None,
        hostname: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.
        :param enabled: Enable the ingress resource that allows you to access the Jenkins installation.
        :param hostname: 

        :schema: JenkinsIngress
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1b534af6b02506f8c0bc7f793f4760d8c5c73e86ecfd1b372abd93b6047eef35)
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument hostname", value=hostname, expected_type=type_hints["hostname"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_values is not None:
            self._values["additional_values"] = additional_values
        if enabled is not None:
            self._values["enabled"] = enabled
        if hostname is not None:
            self._values["hostname"] = hostname

    @builtins.property
    def additional_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: JenkinsIngress#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def enabled(self) -> typing.Optional[builtins.bool]:
        '''Enable the ingress resource that allows you to access the Jenkins installation.

        :schema: JenkinsIngress#enabled
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def hostname(self) -> typing.Optional[builtins.str]:
        '''
        :schema: JenkinsIngress#hostname
        '''
        result = self._values.get("hostname")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "JenkinsIngress(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="jenkins.JenkinsPersistence",
    jsii_struct_bases=[],
    name_mapping={
        "additional_values": "additionalValues",
        "enabled": "enabled",
        "size": "size",
    },
)
class JenkinsPersistence:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        enabled: typing.Optional[builtins.bool] = None,
        size: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.
        :param enabled: Enable persistence using Persistent Volume Claims.
        :param size: 

        :schema: JenkinsPersistence
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a4b98d10a9abe4dbac065491dd9aa28835a0b554a193b0a414737dec68f56439)
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument size", value=size, expected_type=type_hints["size"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_values is not None:
            self._values["additional_values"] = additional_values
        if enabled is not None:
            self._values["enabled"] = enabled
        if size is not None:
            self._values["size"] = size

    @builtins.property
    def additional_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: JenkinsPersistence#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def enabled(self) -> typing.Optional[builtins.bool]:
        '''Enable persistence using Persistent Volume Claims.

        :schema: JenkinsPersistence#enabled
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def size(self) -> typing.Optional[builtins.str]:
        '''
        :schema: JenkinsPersistence#size
        '''
        result = self._values.get("size")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "JenkinsPersistence(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="jenkins.JenkinsProps",
    jsii_struct_bases=[],
    name_mapping={
        "helm_executable": "helmExecutable",
        "helm_flags": "helmFlags",
        "namespace": "namespace",
        "release_name": "releaseName",
        "values": "values",
    },
)
class JenkinsProps:
    def __init__(
        self,
        *,
        helm_executable: typing.Optional[builtins.str] = None,
        helm_flags: typing.Optional[typing.Sequence[builtins.str]] = None,
        namespace: typing.Optional[builtins.str] = None,
        release_name: typing.Optional[builtins.str] = None,
        values: typing.Optional[typing.Union["JenkinsValues", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param helm_executable: -
        :param helm_flags: -
        :param namespace: -
        :param release_name: -
        :param values: -
        '''
        if isinstance(values, dict):
            values = JenkinsValues(**values)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2be9f7a8bb4171a3df6b3ad3937c361a9ec8964d131ff9db164b78cf41b0b2d5)
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
    def values(self) -> typing.Optional["JenkinsValues"]:
        result = self._values.get("values")
        return typing.cast(typing.Optional["JenkinsValues"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "JenkinsProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="jenkins.JenkinsResources",
    jsii_struct_bases=[],
    name_mapping={"additional_values": "additionalValues", "requests": "requests"},
)
class JenkinsResources:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        requests: typing.Optional[typing.Union["JenkinsResourcesRequests", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.
        :param requests: 

        :schema: JenkinsResources
        '''
        if isinstance(requests, dict):
            requests = JenkinsResourcesRequests(**requests)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0943e39aa174973582f35f405638e4c5234bb1fdf7287524566779ea0d4d3289)
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
            check_type(argname="argument requests", value=requests, expected_type=type_hints["requests"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_values is not None:
            self._values["additional_values"] = additional_values
        if requests is not None:
            self._values["requests"] = requests

    @builtins.property
    def additional_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: JenkinsResources#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def requests(self) -> typing.Optional["JenkinsResourcesRequests"]:
        '''
        :schema: JenkinsResources#requests
        '''
        result = self._values.get("requests")
        return typing.cast(typing.Optional["JenkinsResourcesRequests"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "JenkinsResources(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="jenkins.JenkinsResourcesRequests",
    jsii_struct_bases=[],
    name_mapping={
        "additional_values": "additionalValues",
        "cpu": "cpu",
        "memory": "memory",
    },
)
class JenkinsResourcesRequests:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        cpu: typing.Optional[builtins.str] = None,
        memory: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.
        :param cpu: 
        :param memory: 

        :schema: JenkinsResourcesRequests
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6565051a5bf76677652d4dc9aba2a524b2260147d3b178b1744bcf9f0c25e65a)
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
            check_type(argname="argument cpu", value=cpu, expected_type=type_hints["cpu"])
            check_type(argname="argument memory", value=memory, expected_type=type_hints["memory"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_values is not None:
            self._values["additional_values"] = additional_values
        if cpu is not None:
            self._values["cpu"] = cpu
        if memory is not None:
            self._values["memory"] = memory

    @builtins.property
    def additional_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: JenkinsResourcesRequests#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def cpu(self) -> typing.Optional[builtins.str]:
        '''
        :schema: JenkinsResourcesRequests#cpu
        '''
        result = self._values.get("cpu")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def memory(self) -> typing.Optional[builtins.str]:
        '''
        :schema: JenkinsResourcesRequests#memory
        '''
        result = self._values.get("memory")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "JenkinsResourcesRequests(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="jenkins.JenkinsService",
    jsii_struct_bases=[],
    name_mapping={"additional_values": "additionalValues", "type": "type"},
)
class JenkinsService:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.
        :param type: Allowed values: "ClusterIP", "NodePort" and "LoadBalancer".

        :schema: JenkinsService
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6a633d8c1fc6c1c5847a40a1902e4a1c82e9ed740d99f244dff29e3cd49ab369)
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

        :schema: JenkinsService#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''Allowed values: "ClusterIP", "NodePort" and "LoadBalancer".

        :schema: JenkinsService#type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "JenkinsService(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="jenkins.JenkinsValues",
    jsii_struct_bases=[],
    name_mapping={
        "additional_values": "additionalValues",
        "common": "common",
        "global_": "global",
        "ingress": "ingress",
        "jenkins_password": "jenkinsPassword",
        "jenkins_user": "jenkinsUser",
        "persistence": "persistence",
        "resources": "resources",
        "service": "service",
        "service_account_name": "serviceAccountName",
    },
)
class JenkinsValues:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        common: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        global_: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        ingress: typing.Optional[typing.Union[JenkinsIngress, typing.Dict[builtins.str, typing.Any]]] = None,
        jenkins_password: typing.Optional[builtins.str] = None,
        jenkins_user: typing.Optional[builtins.str] = None,
        persistence: typing.Optional[typing.Union[JenkinsPersistence, typing.Dict[builtins.str, typing.Any]]] = None,
        resources: typing.Optional[typing.Union[JenkinsResources, typing.Dict[builtins.str, typing.Any]]] = None,
        service: typing.Optional[typing.Union[JenkinsService, typing.Dict[builtins.str, typing.Any]]] = None,
        service_account_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.
        :param common: 
        :param global_: 
        :param ingress: 
        :param jenkins_password: Defaults to a random 10-character alphanumeric string if not set. Default: a random 10-character alphanumeric string if not set
        :param jenkins_user: 
        :param persistence: 
        :param resources: 
        :param service: 
        :param service_account_name: Defaults to use default if not set. Default: use default if not set

        :schema: jenkins
        '''
        if isinstance(ingress, dict):
            ingress = JenkinsIngress(**ingress)
        if isinstance(persistence, dict):
            persistence = JenkinsPersistence(**persistence)
        if isinstance(resources, dict):
            resources = JenkinsResources(**resources)
        if isinstance(service, dict):
            service = JenkinsService(**service)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__92479fc8ccfd66fda3a3768703f63ef47578a595f76c74c991814618b3d1a8cf)
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
            check_type(argname="argument common", value=common, expected_type=type_hints["common"])
            check_type(argname="argument global_", value=global_, expected_type=type_hints["global_"])
            check_type(argname="argument ingress", value=ingress, expected_type=type_hints["ingress"])
            check_type(argname="argument jenkins_password", value=jenkins_password, expected_type=type_hints["jenkins_password"])
            check_type(argname="argument jenkins_user", value=jenkins_user, expected_type=type_hints["jenkins_user"])
            check_type(argname="argument persistence", value=persistence, expected_type=type_hints["persistence"])
            check_type(argname="argument resources", value=resources, expected_type=type_hints["resources"])
            check_type(argname="argument service", value=service, expected_type=type_hints["service"])
            check_type(argname="argument service_account_name", value=service_account_name, expected_type=type_hints["service_account_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_values is not None:
            self._values["additional_values"] = additional_values
        if common is not None:
            self._values["common"] = common
        if global_ is not None:
            self._values["global_"] = global_
        if ingress is not None:
            self._values["ingress"] = ingress
        if jenkins_password is not None:
            self._values["jenkins_password"] = jenkins_password
        if jenkins_user is not None:
            self._values["jenkins_user"] = jenkins_user
        if persistence is not None:
            self._values["persistence"] = persistence
        if resources is not None:
            self._values["resources"] = resources
        if service is not None:
            self._values["service"] = service
        if service_account_name is not None:
            self._values["service_account_name"] = service_account_name

    @builtins.property
    def additional_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: jenkins#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def common(self) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''
        :schema: jenkins#common
        '''
        result = self._values.get("common")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def global_(self) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''
        :schema: jenkins#global
        '''
        result = self._values.get("global_")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def ingress(self) -> typing.Optional[JenkinsIngress]:
        '''
        :schema: jenkins#ingress
        '''
        result = self._values.get("ingress")
        return typing.cast(typing.Optional[JenkinsIngress], result)

    @builtins.property
    def jenkins_password(self) -> typing.Optional[builtins.str]:
        '''Defaults to a random 10-character alphanumeric string if not set.

        :default: a random 10-character alphanumeric string if not set

        :schema: jenkins#jenkinsPassword
        '''
        result = self._values.get("jenkins_password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def jenkins_user(self) -> typing.Optional[builtins.str]:
        '''
        :schema: jenkins#jenkinsUser
        '''
        result = self._values.get("jenkins_user")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def persistence(self) -> typing.Optional[JenkinsPersistence]:
        '''
        :schema: jenkins#persistence
        '''
        result = self._values.get("persistence")
        return typing.cast(typing.Optional[JenkinsPersistence], result)

    @builtins.property
    def resources(self) -> typing.Optional[JenkinsResources]:
        '''
        :schema: jenkins#resources
        '''
        result = self._values.get("resources")
        return typing.cast(typing.Optional[JenkinsResources], result)

    @builtins.property
    def service(self) -> typing.Optional[JenkinsService]:
        '''
        :schema: jenkins#service
        '''
        result = self._values.get("service")
        return typing.cast(typing.Optional[JenkinsService], result)

    @builtins.property
    def service_account_name(self) -> typing.Optional[builtins.str]:
        '''Defaults to use default if not set.

        :default: use default if not set

        :schema: jenkins#serviceAccountName
        '''
        result = self._values.get("service_account_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "JenkinsValues(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "Jenkins",
    "JenkinsIngress",
    "JenkinsPersistence",
    "JenkinsProps",
    "JenkinsResources",
    "JenkinsResourcesRequests",
    "JenkinsService",
    "JenkinsValues",
]

publication.publish()

def _typecheckingstub__b578a09bb9c61f8b4b01ea5f17ebf3048b7442f70e4f2bd4d3012de973bedee6(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    helm_executable: typing.Optional[builtins.str] = None,
    helm_flags: typing.Optional[typing.Sequence[builtins.str]] = None,
    namespace: typing.Optional[builtins.str] = None,
    release_name: typing.Optional[builtins.str] = None,
    values: typing.Optional[typing.Union[JenkinsValues, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1b534af6b02506f8c0bc7f793f4760d8c5c73e86ecfd1b372abd93b6047eef35(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    enabled: typing.Optional[builtins.bool] = None,
    hostname: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a4b98d10a9abe4dbac065491dd9aa28835a0b554a193b0a414737dec68f56439(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    enabled: typing.Optional[builtins.bool] = None,
    size: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2be9f7a8bb4171a3df6b3ad3937c361a9ec8964d131ff9db164b78cf41b0b2d5(
    *,
    helm_executable: typing.Optional[builtins.str] = None,
    helm_flags: typing.Optional[typing.Sequence[builtins.str]] = None,
    namespace: typing.Optional[builtins.str] = None,
    release_name: typing.Optional[builtins.str] = None,
    values: typing.Optional[typing.Union[JenkinsValues, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0943e39aa174973582f35f405638e4c5234bb1fdf7287524566779ea0d4d3289(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    requests: typing.Optional[typing.Union[JenkinsResourcesRequests, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6565051a5bf76677652d4dc9aba2a524b2260147d3b178b1744bcf9f0c25e65a(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    cpu: typing.Optional[builtins.str] = None,
    memory: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6a633d8c1fc6c1c5847a40a1902e4a1c82e9ed740d99f244dff29e3cd49ab369(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__92479fc8ccfd66fda3a3768703f63ef47578a595f76c74c991814618b3d1a8cf(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    common: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    global_: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    ingress: typing.Optional[typing.Union[JenkinsIngress, typing.Dict[builtins.str, typing.Any]]] = None,
    jenkins_password: typing.Optional[builtins.str] = None,
    jenkins_user: typing.Optional[builtins.str] = None,
    persistence: typing.Optional[typing.Union[JenkinsPersistence, typing.Dict[builtins.str, typing.Any]]] = None,
    resources: typing.Optional[typing.Union[JenkinsResources, typing.Dict[builtins.str, typing.Any]]] = None,
    service: typing.Optional[typing.Union[JenkinsService, typing.Dict[builtins.str, typing.Any]]] = None,
    service_account_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
