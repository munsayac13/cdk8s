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


class Valkey(
    _constructs_77d1e7e8.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="valkey.Valkey",
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
        values: typing.Optional[typing.Union["ValkeyValues", typing.Dict[builtins.str, typing.Any]]] = None,
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
            type_hints = typing.get_type_hints(_typecheckingstub__c250028ee08a9cdbadcf4f0fe970bcfa0b2df57d8787d1e0a444e3bca9d0e377)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = ValkeyProps(
            helm_executable=helm_executable,
            helm_flags=helm_flags,
            namespace=namespace,
            release_name=release_name,
            values=values,
        )

        jsii.create(self.__class__, self, [scope, id, props])


@jsii.enum(jsii_type="valkey.ValkeyArchitecture")
class ValkeyArchitecture(enum.Enum):
    '''Allowed values: ``standalone`` or ``replication``.

    :schema: ValkeyArchitecture
    '''

    STANDALONE = "STANDALONE"
    '''standalone.'''
    REPLICATION = "REPLICATION"
    '''replication.'''


@jsii.data_type(
    jsii_type="valkey.ValkeyAuth",
    jsii_struct_bases=[],
    name_mapping={
        "additional_values": "additionalValues",
        "enabled": "enabled",
        "password": "password",
    },
)
class ValkeyAuth:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        enabled: typing.Optional[builtins.bool] = None,
        password: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.
        :param enabled: 
        :param password: Defaults to a random 10-character alphanumeric string if not set. Default: a random 10-character alphanumeric string if not set

        :schema: ValkeyAuth
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d8557859d94d6bf72cccff7b20b5f4c672fbc50bc3745f00dea1747650e7a581)
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_values is not None:
            self._values["additional_values"] = additional_values
        if enabled is not None:
            self._values["enabled"] = enabled
        if password is not None:
            self._values["password"] = password

    @builtins.property
    def additional_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: ValkeyAuth#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def enabled(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: ValkeyAuth#enabled
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def password(self) -> typing.Optional[builtins.str]:
        '''Defaults to a random 10-character alphanumeric string if not set.

        :default: a random 10-character alphanumeric string if not set

        :schema: ValkeyAuth#password
        '''
        result = self._values.get("password")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ValkeyAuth(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="valkey.ValkeyMetrics",
    jsii_struct_bases=[],
    name_mapping={
        "additional_values": "additionalValues",
        "enabled": "enabled",
        "service_monitor": "serviceMonitor",
    },
)
class ValkeyMetrics:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        enabled: typing.Optional[builtins.bool] = None,
        service_monitor: typing.Optional[typing.Union["ValkeyMetricsServiceMonitor", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.
        :param enabled: Create a side-car container to expose Prometheus metrics.
        :param service_monitor: 

        :schema: ValkeyMetrics
        '''
        if isinstance(service_monitor, dict):
            service_monitor = ValkeyMetricsServiceMonitor(**service_monitor)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__34c4c87db9ddd6ff71ccc9b38db57ec54ff895047b4ffc7faa669d597d4ebed6)
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument service_monitor", value=service_monitor, expected_type=type_hints["service_monitor"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_values is not None:
            self._values["additional_values"] = additional_values
        if enabled is not None:
            self._values["enabled"] = enabled
        if service_monitor is not None:
            self._values["service_monitor"] = service_monitor

    @builtins.property
    def additional_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: ValkeyMetrics#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def enabled(self) -> typing.Optional[builtins.bool]:
        '''Create a side-car container to expose Prometheus metrics.

        :schema: ValkeyMetrics#enabled
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def service_monitor(self) -> typing.Optional["ValkeyMetricsServiceMonitor"]:
        '''
        :schema: ValkeyMetrics#serviceMonitor
        '''
        result = self._values.get("service_monitor")
        return typing.cast(typing.Optional["ValkeyMetricsServiceMonitor"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ValkeyMetrics(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="valkey.ValkeyMetricsServiceMonitor",
    jsii_struct_bases=[],
    name_mapping={"additional_values": "additionalValues", "enabled": "enabled"},
)
class ValkeyMetricsServiceMonitor:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        enabled: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.
        :param enabled: Create a ServiceMonitor to track metrics using Prometheus Operator.

        :schema: ValkeyMetricsServiceMonitor
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cae7306fbf647b3b1bf6170fbaa826e32a5c7537653d954175f49e2d294bd330)
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

        :schema: ValkeyMetricsServiceMonitor#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def enabled(self) -> typing.Optional[builtins.bool]:
        '''Create a ServiceMonitor to track metrics using Prometheus Operator.

        :schema: ValkeyMetricsServiceMonitor#enabled
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ValkeyMetricsServiceMonitor(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="valkey.ValkeyPrimary",
    jsii_struct_bases=[],
    name_mapping={
        "additional_values": "additionalValues",
        "kind": "kind",
        "persistence": "persistence",
    },
)
class ValkeyPrimary:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        kind: typing.Optional["ValkeyPrimaryKind"] = None,
        persistence: typing.Optional[typing.Union["ValkeyPrimaryPersistence", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.
        :param kind: Allowed values: ``Deployment``, ``StatefulSet`` or ``DaemonSet``.
        :param persistence: 

        :schema: ValkeyPrimary
        '''
        if isinstance(persistence, dict):
            persistence = ValkeyPrimaryPersistence(**persistence)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__72379e45f83008f4598fc80c17d1ee33c3757bbacbab81796692760d96676fff)
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
            check_type(argname="argument kind", value=kind, expected_type=type_hints["kind"])
            check_type(argname="argument persistence", value=persistence, expected_type=type_hints["persistence"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_values is not None:
            self._values["additional_values"] = additional_values
        if kind is not None:
            self._values["kind"] = kind
        if persistence is not None:
            self._values["persistence"] = persistence

    @builtins.property
    def additional_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: ValkeyPrimary#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def kind(self) -> typing.Optional["ValkeyPrimaryKind"]:
        '''Allowed values: ``Deployment``, ``StatefulSet`` or ``DaemonSet``.

        :schema: ValkeyPrimary#kind
        '''
        result = self._values.get("kind")
        return typing.cast(typing.Optional["ValkeyPrimaryKind"], result)

    @builtins.property
    def persistence(self) -> typing.Optional["ValkeyPrimaryPersistence"]:
        '''
        :schema: ValkeyPrimary#persistence
        '''
        result = self._values.get("persistence")
        return typing.cast(typing.Optional["ValkeyPrimaryPersistence"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ValkeyPrimary(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="valkey.ValkeyPrimaryKind")
class ValkeyPrimaryKind(enum.Enum):
    '''Allowed values: ``Deployment``, ``StatefulSet`` or ``DaemonSet``.

    :schema: ValkeyPrimaryKind
    '''

    DEPLOYMENT = "DEPLOYMENT"
    '''Deployment.'''
    STATEFUL_SET = "STATEFUL_SET"
    '''StatefulSet.'''
    DAEMON_SET = "DAEMON_SET"
    '''DaemonSet.'''


@jsii.data_type(
    jsii_type="valkey.ValkeyPrimaryPersistence",
    jsii_struct_bases=[],
    name_mapping={
        "additional_values": "additionalValues",
        "enabled": "enabled",
        "size": "size",
    },
)
class ValkeyPrimaryPersistence:
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

        :schema: ValkeyPrimaryPersistence
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__62ccae9fb5808f9a1a9c01c9035abf8f4a7364f0f20d76b2bac7b0d1fe36e519)
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

        :schema: ValkeyPrimaryPersistence#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def enabled(self) -> typing.Optional[builtins.bool]:
        '''Enable persistence using Persistent Volume Claims.

        :schema: ValkeyPrimaryPersistence#enabled
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def size(self) -> typing.Optional[builtins.str]:
        '''
        :schema: ValkeyPrimaryPersistence#size
        '''
        result = self._values.get("size")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ValkeyPrimaryPersistence(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="valkey.ValkeyProps",
    jsii_struct_bases=[],
    name_mapping={
        "helm_executable": "helmExecutable",
        "helm_flags": "helmFlags",
        "namespace": "namespace",
        "release_name": "releaseName",
        "values": "values",
    },
)
class ValkeyProps:
    def __init__(
        self,
        *,
        helm_executable: typing.Optional[builtins.str] = None,
        helm_flags: typing.Optional[typing.Sequence[builtins.str]] = None,
        namespace: typing.Optional[builtins.str] = None,
        release_name: typing.Optional[builtins.str] = None,
        values: typing.Optional[typing.Union["ValkeyValues", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param helm_executable: -
        :param helm_flags: -
        :param namespace: -
        :param release_name: -
        :param values: -
        '''
        if isinstance(values, dict):
            values = ValkeyValues(**values)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bc005dc54f34b5dcadd60a19868b868879800a5bd729131626f6b61a8ab7fb6e)
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
    def values(self) -> typing.Optional["ValkeyValues"]:
        result = self._values.get("values")
        return typing.cast(typing.Optional["ValkeyValues"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ValkeyProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="valkey.ValkeyReplica",
    jsii_struct_bases=[],
    name_mapping={
        "additional_values": "additionalValues",
        "kind": "kind",
        "persistence": "persistence",
        "replica_count": "replicaCount",
    },
)
class ValkeyReplica:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        kind: typing.Optional["ValkeyReplicaKind"] = None,
        persistence: typing.Optional[typing.Union["ValkeyReplicaPersistence", typing.Dict[builtins.str, typing.Any]]] = None,
        replica_count: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.
        :param kind: Allowed values: ``DaemonSet`` or ``StatefulSet``.
        :param persistence: 
        :param replica_count: 

        :schema: ValkeyReplica
        '''
        if isinstance(persistence, dict):
            persistence = ValkeyReplicaPersistence(**persistence)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__af10d7d960c1a638fc77db76b22b37b186fb960d969b64f916db02608ec1d191)
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
            check_type(argname="argument kind", value=kind, expected_type=type_hints["kind"])
            check_type(argname="argument persistence", value=persistence, expected_type=type_hints["persistence"])
            check_type(argname="argument replica_count", value=replica_count, expected_type=type_hints["replica_count"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_values is not None:
            self._values["additional_values"] = additional_values
        if kind is not None:
            self._values["kind"] = kind
        if persistence is not None:
            self._values["persistence"] = persistence
        if replica_count is not None:
            self._values["replica_count"] = replica_count

    @builtins.property
    def additional_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: ValkeyReplica#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def kind(self) -> typing.Optional["ValkeyReplicaKind"]:
        '''Allowed values: ``DaemonSet`` or ``StatefulSet``.

        :schema: ValkeyReplica#kind
        '''
        result = self._values.get("kind")
        return typing.cast(typing.Optional["ValkeyReplicaKind"], result)

    @builtins.property
    def persistence(self) -> typing.Optional["ValkeyReplicaPersistence"]:
        '''
        :schema: ValkeyReplica#persistence
        '''
        result = self._values.get("persistence")
        return typing.cast(typing.Optional["ValkeyReplicaPersistence"], result)

    @builtins.property
    def replica_count(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: ValkeyReplica#replicaCount
        '''
        result = self._values.get("replica_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ValkeyReplica(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="valkey.ValkeyReplicaKind")
class ValkeyReplicaKind(enum.Enum):
    '''Allowed values: ``DaemonSet`` or ``StatefulSet``.

    :schema: ValkeyReplicaKind
    '''

    DAEMON_SET = "DAEMON_SET"
    '''DaemonSet.'''
    STATEFUL_SET = "STATEFUL_SET"
    '''StatefulSet.'''


@jsii.data_type(
    jsii_type="valkey.ValkeyReplicaPersistence",
    jsii_struct_bases=[],
    name_mapping={
        "additional_values": "additionalValues",
        "enabled": "enabled",
        "size": "size",
    },
)
class ValkeyReplicaPersistence:
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

        :schema: ValkeyReplicaPersistence
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__372c8b5168d29cfe8e07f38e3ded3e9ae423323b0cbe70091740102afc6512be)
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

        :schema: ValkeyReplicaPersistence#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def enabled(self) -> typing.Optional[builtins.bool]:
        '''Enable persistence using Persistent Volume Claims.

        :schema: ValkeyReplicaPersistence#enabled
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def size(self) -> typing.Optional[builtins.str]:
        '''
        :schema: ValkeyReplicaPersistence#size
        '''
        result = self._values.get("size")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ValkeyReplicaPersistence(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="valkey.ValkeyValues",
    jsii_struct_bases=[],
    name_mapping={
        "additional_values": "additionalValues",
        "architecture": "architecture",
        "auth": "auth",
        "common": "common",
        "global_": "global",
        "metrics": "metrics",
        "primary": "primary",
        "replica": "replica",
        "volume_permissions": "volumePermissions",
    },
)
class ValkeyValues:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        architecture: typing.Optional[ValkeyArchitecture] = None,
        auth: typing.Optional[typing.Union[ValkeyAuth, typing.Dict[builtins.str, typing.Any]]] = None,
        common: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        global_: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        metrics: typing.Optional[typing.Union[ValkeyMetrics, typing.Dict[builtins.str, typing.Any]]] = None,
        primary: typing.Optional[typing.Union[ValkeyPrimary, typing.Dict[builtins.str, typing.Any]]] = None,
        replica: typing.Optional[typing.Union[ValkeyReplica, typing.Dict[builtins.str, typing.Any]]] = None,
        volume_permissions: typing.Optional[typing.Union["ValkeyVolumePermissions", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.
        :param architecture: Allowed values: ``standalone`` or ``replication``.
        :param auth: 
        :param common: 
        :param global_: 
        :param metrics: 
        :param primary: 
        :param replica: 
        :param volume_permissions: 

        :schema: valkey
        '''
        if isinstance(auth, dict):
            auth = ValkeyAuth(**auth)
        if isinstance(metrics, dict):
            metrics = ValkeyMetrics(**metrics)
        if isinstance(primary, dict):
            primary = ValkeyPrimary(**primary)
        if isinstance(replica, dict):
            replica = ValkeyReplica(**replica)
        if isinstance(volume_permissions, dict):
            volume_permissions = ValkeyVolumePermissions(**volume_permissions)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6329073be9dd75f82c490f041180673610665f79017e4841590296319a32d4c8)
            check_type(argname="argument additional_values", value=additional_values, expected_type=type_hints["additional_values"])
            check_type(argname="argument architecture", value=architecture, expected_type=type_hints["architecture"])
            check_type(argname="argument auth", value=auth, expected_type=type_hints["auth"])
            check_type(argname="argument common", value=common, expected_type=type_hints["common"])
            check_type(argname="argument global_", value=global_, expected_type=type_hints["global_"])
            check_type(argname="argument metrics", value=metrics, expected_type=type_hints["metrics"])
            check_type(argname="argument primary", value=primary, expected_type=type_hints["primary"])
            check_type(argname="argument replica", value=replica, expected_type=type_hints["replica"])
            check_type(argname="argument volume_permissions", value=volume_permissions, expected_type=type_hints["volume_permissions"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_values is not None:
            self._values["additional_values"] = additional_values
        if architecture is not None:
            self._values["architecture"] = architecture
        if auth is not None:
            self._values["auth"] = auth
        if common is not None:
            self._values["common"] = common
        if global_ is not None:
            self._values["global_"] = global_
        if metrics is not None:
            self._values["metrics"] = metrics
        if primary is not None:
            self._values["primary"] = primary
        if replica is not None:
            self._values["replica"] = replica
        if volume_permissions is not None:
            self._values["volume_permissions"] = volume_permissions

    @builtins.property
    def additional_values(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Values that are not available in values.schema.json will not be code generated. You can add such values to this property.

        :schema: valkey#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def architecture(self) -> typing.Optional[ValkeyArchitecture]:
        '''Allowed values: ``standalone`` or ``replication``.

        :schema: valkey#architecture
        '''
        result = self._values.get("architecture")
        return typing.cast(typing.Optional[ValkeyArchitecture], result)

    @builtins.property
    def auth(self) -> typing.Optional[ValkeyAuth]:
        '''
        :schema: valkey#auth
        '''
        result = self._values.get("auth")
        return typing.cast(typing.Optional[ValkeyAuth], result)

    @builtins.property
    def common(self) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''
        :schema: valkey#common
        '''
        result = self._values.get("common")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def global_(self) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''
        :schema: valkey#global
        '''
        result = self._values.get("global_")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def metrics(self) -> typing.Optional[ValkeyMetrics]:
        '''
        :schema: valkey#metrics
        '''
        result = self._values.get("metrics")
        return typing.cast(typing.Optional[ValkeyMetrics], result)

    @builtins.property
    def primary(self) -> typing.Optional[ValkeyPrimary]:
        '''
        :schema: valkey#primary
        '''
        result = self._values.get("primary")
        return typing.cast(typing.Optional[ValkeyPrimary], result)

    @builtins.property
    def replica(self) -> typing.Optional[ValkeyReplica]:
        '''
        :schema: valkey#replica
        '''
        result = self._values.get("replica")
        return typing.cast(typing.Optional[ValkeyReplica], result)

    @builtins.property
    def volume_permissions(self) -> typing.Optional["ValkeyVolumePermissions"]:
        '''
        :schema: valkey#volumePermissions
        '''
        result = self._values.get("volume_permissions")
        return typing.cast(typing.Optional["ValkeyVolumePermissions"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ValkeyValues(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="valkey.ValkeyVolumePermissions",
    jsii_struct_bases=[],
    name_mapping={"additional_values": "additionalValues", "enabled": "enabled"},
)
class ValkeyVolumePermissions:
    def __init__(
        self,
        *,
        additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        enabled: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param additional_values: Values that are not available in values.schema.json will not be code generated. You can add such values to this property.
        :param enabled: Use an init container to set required folder permissions on the data volume before mounting it in the final destination.

        :schema: ValkeyVolumePermissions
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d6ebf4c6193c38497594dc454105eac5bdb4af2968d2b79f875d6cf720cfe189)
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

        :schema: ValkeyVolumePermissions#additionalValues
        '''
        result = self._values.get("additional_values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def enabled(self) -> typing.Optional[builtins.bool]:
        '''Use an init container to set required folder permissions on the data volume before mounting it in the final destination.

        :schema: ValkeyVolumePermissions#enabled
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ValkeyVolumePermissions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "Valkey",
    "ValkeyArchitecture",
    "ValkeyAuth",
    "ValkeyMetrics",
    "ValkeyMetricsServiceMonitor",
    "ValkeyPrimary",
    "ValkeyPrimaryKind",
    "ValkeyPrimaryPersistence",
    "ValkeyProps",
    "ValkeyReplica",
    "ValkeyReplicaKind",
    "ValkeyReplicaPersistence",
    "ValkeyValues",
    "ValkeyVolumePermissions",
]

publication.publish()

def _typecheckingstub__c250028ee08a9cdbadcf4f0fe970bcfa0b2df57d8787d1e0a444e3bca9d0e377(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    helm_executable: typing.Optional[builtins.str] = None,
    helm_flags: typing.Optional[typing.Sequence[builtins.str]] = None,
    namespace: typing.Optional[builtins.str] = None,
    release_name: typing.Optional[builtins.str] = None,
    values: typing.Optional[typing.Union[ValkeyValues, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d8557859d94d6bf72cccff7b20b5f4c672fbc50bc3745f00dea1747650e7a581(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    enabled: typing.Optional[builtins.bool] = None,
    password: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__34c4c87db9ddd6ff71ccc9b38db57ec54ff895047b4ffc7faa669d597d4ebed6(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    enabled: typing.Optional[builtins.bool] = None,
    service_monitor: typing.Optional[typing.Union[ValkeyMetricsServiceMonitor, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cae7306fbf647b3b1bf6170fbaa826e32a5c7537653d954175f49e2d294bd330(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    enabled: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__72379e45f83008f4598fc80c17d1ee33c3757bbacbab81796692760d96676fff(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    kind: typing.Optional[ValkeyPrimaryKind] = None,
    persistence: typing.Optional[typing.Union[ValkeyPrimaryPersistence, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__62ccae9fb5808f9a1a9c01c9035abf8f4a7364f0f20d76b2bac7b0d1fe36e519(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    enabled: typing.Optional[builtins.bool] = None,
    size: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bc005dc54f34b5dcadd60a19868b868879800a5bd729131626f6b61a8ab7fb6e(
    *,
    helm_executable: typing.Optional[builtins.str] = None,
    helm_flags: typing.Optional[typing.Sequence[builtins.str]] = None,
    namespace: typing.Optional[builtins.str] = None,
    release_name: typing.Optional[builtins.str] = None,
    values: typing.Optional[typing.Union[ValkeyValues, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af10d7d960c1a638fc77db76b22b37b186fb960d969b64f916db02608ec1d191(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    kind: typing.Optional[ValkeyReplicaKind] = None,
    persistence: typing.Optional[typing.Union[ValkeyReplicaPersistence, typing.Dict[builtins.str, typing.Any]]] = None,
    replica_count: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__372c8b5168d29cfe8e07f38e3ded3e9ae423323b0cbe70091740102afc6512be(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    enabled: typing.Optional[builtins.bool] = None,
    size: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6329073be9dd75f82c490f041180673610665f79017e4841590296319a32d4c8(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    architecture: typing.Optional[ValkeyArchitecture] = None,
    auth: typing.Optional[typing.Union[ValkeyAuth, typing.Dict[builtins.str, typing.Any]]] = None,
    common: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    global_: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    metrics: typing.Optional[typing.Union[ValkeyMetrics, typing.Dict[builtins.str, typing.Any]]] = None,
    primary: typing.Optional[typing.Union[ValkeyPrimary, typing.Dict[builtins.str, typing.Any]]] = None,
    replica: typing.Optional[typing.Union[ValkeyReplica, typing.Dict[builtins.str, typing.Any]]] = None,
    volume_permissions: typing.Optional[typing.Union[ValkeyVolumePermissions, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d6ebf4c6193c38497594dc454105eac5bdb4af2968d2b79f875d6cf720cfe189(
    *,
    additional_values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    enabled: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass
