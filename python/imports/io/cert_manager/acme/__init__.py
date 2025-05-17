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

import cdk8s as _cdk8s_d3d9af27
import constructs as _constructs_77d1e7e8


class Challenge(
    _cdk8s_d3d9af27.ApiObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="iocert-manageracme.Challenge",
):
    '''Challenge is a type to represent a Challenge request with an ACME server.

    :schema: Challenge
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        metadata: typing.Union[_cdk8s_d3d9af27.ApiObjectMetadata, typing.Dict[builtins.str, typing.Any]],
        spec: typing.Union["ChallengeSpec", typing.Dict[builtins.str, typing.Any]],
    ) -> None:
        '''Defines a "Challenge" API object.

        :param scope: the scope in which to define this object.
        :param id: a scope-local name for the object.
        :param metadata: 
        :param spec: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c9e7b67fe7fc10175a4d7deaeb248d18de0bbb75e0cf47708d0c404c856d36b1)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = ChallengeProps(metadata=metadata, spec=spec)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="manifest")
    @builtins.classmethod
    def manifest(
        cls,
        *,
        metadata: typing.Union[_cdk8s_d3d9af27.ApiObjectMetadata, typing.Dict[builtins.str, typing.Any]],
        spec: typing.Union["ChallengeSpec", typing.Dict[builtins.str, typing.Any]],
    ) -> typing.Any:
        '''Renders a Kubernetes manifest for "Challenge".

        This can be used to inline resource manifests inside other objects (e.g. as templates).

        :param metadata: 
        :param spec: 
        '''
        props = ChallengeProps(metadata=metadata, spec=spec)

        return typing.cast(typing.Any, jsii.sinvoke(cls, "manifest", [props]))

    @jsii.member(jsii_name="toJson")
    def to_json(self) -> typing.Any:
        '''Renders the object to Kubernetes JSON.'''
        return typing.cast(typing.Any, jsii.invoke(self, "toJson", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="GVK")
    def GVK(cls) -> _cdk8s_d3d9af27.GroupVersionKind:
        '''Returns the apiVersion and kind for "Challenge".'''
        return typing.cast(_cdk8s_d3d9af27.GroupVersionKind, jsii.sget(cls, "GVK"))


@jsii.data_type(
    jsii_type="iocert-manageracme.ChallengeProps",
    jsii_struct_bases=[],
    name_mapping={"metadata": "metadata", "spec": "spec"},
)
class ChallengeProps:
    def __init__(
        self,
        *,
        metadata: typing.Union[_cdk8s_d3d9af27.ApiObjectMetadata, typing.Dict[builtins.str, typing.Any]],
        spec: typing.Union["ChallengeSpec", typing.Dict[builtins.str, typing.Any]],
    ) -> None:
        '''Challenge is a type to represent a Challenge request with an ACME server.

        :param metadata: 
        :param spec: 

        :schema: Challenge
        '''
        if isinstance(metadata, dict):
            metadata = _cdk8s_d3d9af27.ApiObjectMetadata(**metadata)
        if isinstance(spec, dict):
            spec = ChallengeSpec(**spec)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__21a9e1c772a1f0da2500f29eb767b45f194ed7c8956f6d35cb170c541e735509)
            check_type(argname="argument metadata", value=metadata, expected_type=type_hints["metadata"])
            check_type(argname="argument spec", value=spec, expected_type=type_hints["spec"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "metadata": metadata,
            "spec": spec,
        }

    @builtins.property
    def metadata(self) -> _cdk8s_d3d9af27.ApiObjectMetadata:
        '''
        :schema: Challenge#metadata
        '''
        result = self._values.get("metadata")
        assert result is not None, "Required property 'metadata' is missing"
        return typing.cast(_cdk8s_d3d9af27.ApiObjectMetadata, result)

    @builtins.property
    def spec(self) -> "ChallengeSpec":
        '''
        :schema: Challenge#spec
        '''
        result = self._values.get("spec")
        assert result is not None, "Required property 'spec' is missing"
        return typing.cast("ChallengeSpec", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ChallengeProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iocert-manageracme.ChallengeSpec",
    jsii_struct_bases=[],
    name_mapping={
        "authorization_url": "authorizationUrl",
        "dns_name": "dnsName",
        "issuer_ref": "issuerRef",
        "key": "key",
        "solver": "solver",
        "token": "token",
        "type": "type",
        "url": "url",
        "wildcard": "wildcard",
    },
)
class ChallengeSpec:
    def __init__(
        self,
        *,
        authorization_url: builtins.str,
        dns_name: builtins.str,
        issuer_ref: typing.Union["ChallengeSpecIssuerRef", typing.Dict[builtins.str, typing.Any]],
        key: builtins.str,
        solver: typing.Union["ChallengeSpecSolver", typing.Dict[builtins.str, typing.Any]],
        token: builtins.str,
        type: "ChallengeSpecType",
        url: builtins.str,
        wildcard: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param authorization_url: The URL to the ACME Authorization resource that this challenge is a part of.
        :param dns_name: dnsName is the identifier that this challenge is for, e.g. example.com. If the requested DNSName is a 'wildcard', this field MUST be set to the non-wildcard domain, e.g. for ``*.example.com``, it must be ``example.com``.
        :param issuer_ref: References a properly configured ACME-type Issuer which should be used to create this Challenge. If the Issuer does not exist, processing will be retried. If the Issuer is not an 'ACME' Issuer, an error will be returned and the Challenge will be marked as failed.
        :param key: The ACME challenge key for this challenge For HTTP01 challenges, this is the value that must be responded with to complete the HTTP01 challenge in the format: ``<private key JWK thumbprint>.<key from acme server for challenge>``. For DNS01 challenges, this is the base64 encoded SHA256 sum of the ``<private key JWK thumbprint>.<key from acme server for challenge>`` text that must be set as the TXT record content.
        :param solver: Contains the domain solving configuration that should be used to solve this challenge resource.
        :param token: The ACME challenge token for this challenge. This is the raw value returned from the ACME server.
        :param type: The type of ACME challenge this resource represents. One of "HTTP-01" or "DNS-01".
        :param url: The URL of the ACME Challenge resource for this challenge. This can be used to lookup details about the status of this challenge.
        :param wildcard: wildcard will be true if this challenge is for a wildcard identifier, for example '*.example.com'.

        :schema: ChallengeSpec
        '''
        if isinstance(issuer_ref, dict):
            issuer_ref = ChallengeSpecIssuerRef(**issuer_ref)
        if isinstance(solver, dict):
            solver = ChallengeSpecSolver(**solver)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__207844d086707968e4012edfc78d0e652f5f4892740dd9d1a5f633a1d1324d45)
            check_type(argname="argument authorization_url", value=authorization_url, expected_type=type_hints["authorization_url"])
            check_type(argname="argument dns_name", value=dns_name, expected_type=type_hints["dns_name"])
            check_type(argname="argument issuer_ref", value=issuer_ref, expected_type=type_hints["issuer_ref"])
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument solver", value=solver, expected_type=type_hints["solver"])
            check_type(argname="argument token", value=token, expected_type=type_hints["token"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument url", value=url, expected_type=type_hints["url"])
            check_type(argname="argument wildcard", value=wildcard, expected_type=type_hints["wildcard"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "authorization_url": authorization_url,
            "dns_name": dns_name,
            "issuer_ref": issuer_ref,
            "key": key,
            "solver": solver,
            "token": token,
            "type": type,
            "url": url,
        }
        if wildcard is not None:
            self._values["wildcard"] = wildcard

    @builtins.property
    def authorization_url(self) -> builtins.str:
        '''The URL to the ACME Authorization resource that this challenge is a part of.

        :schema: ChallengeSpec#authorizationURL
        '''
        result = self._values.get("authorization_url")
        assert result is not None, "Required property 'authorization_url' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def dns_name(self) -> builtins.str:
        '''dnsName is the identifier that this challenge is for, e.g. example.com. If the requested DNSName is a 'wildcard', this field MUST be set to the non-wildcard domain, e.g. for ``*.example.com``, it must be ``example.com``.

        :schema: ChallengeSpec#dnsName
        '''
        result = self._values.get("dns_name")
        assert result is not None, "Required property 'dns_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def issuer_ref(self) -> "ChallengeSpecIssuerRef":
        '''References a properly configured ACME-type Issuer which should be used to create this Challenge.

        If the Issuer does not exist, processing will be retried.
        If the Issuer is not an 'ACME' Issuer, an error will be returned and the
        Challenge will be marked as failed.

        :schema: ChallengeSpec#issuerRef
        '''
        result = self._values.get("issuer_ref")
        assert result is not None, "Required property 'issuer_ref' is missing"
        return typing.cast("ChallengeSpecIssuerRef", result)

    @builtins.property
    def key(self) -> builtins.str:
        '''The ACME challenge key for this challenge For HTTP01 challenges, this is the value that must be responded with to complete the HTTP01 challenge in the format: ``<private key JWK thumbprint>.<key from acme server for challenge>``. For DNS01 challenges, this is the base64 encoded SHA256 sum of the ``<private key JWK thumbprint>.<key from acme server for challenge>`` text that must be set as the TXT record content.

        :schema: ChallengeSpec#key
        '''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def solver(self) -> "ChallengeSpecSolver":
        '''Contains the domain solving configuration that should be used to solve this challenge resource.

        :schema: ChallengeSpec#solver
        '''
        result = self._values.get("solver")
        assert result is not None, "Required property 'solver' is missing"
        return typing.cast("ChallengeSpecSolver", result)

    @builtins.property
    def token(self) -> builtins.str:
        '''The ACME challenge token for this challenge.

        This is the raw value returned from the ACME server.

        :schema: ChallengeSpec#token
        '''
        result = self._values.get("token")
        assert result is not None, "Required property 'token' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> "ChallengeSpecType":
        '''The type of ACME challenge this resource represents.

        One of "HTTP-01" or "DNS-01".

        :schema: ChallengeSpec#type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast("ChallengeSpecType", result)

    @builtins.property
    def url(self) -> builtins.str:
        '''The URL of the ACME Challenge resource for this challenge.

        This can be used to lookup details about the status of this challenge.

        :schema: ChallengeSpec#url
        '''
        result = self._values.get("url")
        assert result is not None, "Required property 'url' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def wildcard(self) -> typing.Optional[builtins.bool]:
        '''wildcard will be true if this challenge is for a wildcard identifier, for example '*.example.com'.

        :schema: ChallengeSpec#wildcard
        '''
        result = self._values.get("wildcard")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ChallengeSpec(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iocert-manageracme.ChallengeSpecIssuerRef",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "group": "group", "kind": "kind"},
)
class ChallengeSpecIssuerRef:
    def __init__(
        self,
        *,
        name: builtins.str,
        group: typing.Optional[builtins.str] = None,
        kind: typing.Optional[builtins.str] = None,
    ) -> None:
        '''References a properly configured ACME-type Issuer which should be used to create this Challenge.

        If the Issuer does not exist, processing will be retried.
        If the Issuer is not an 'ACME' Issuer, an error will be returned and the
        Challenge will be marked as failed.

        :param name: Name of the resource being referred to.
        :param group: Group of the resource being referred to.
        :param kind: Kind of the resource being referred to.

        :schema: ChallengeSpecIssuerRef
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bf94af1aaabe5ad431383ca2c1cbc6c63dc368710c72420f2fa90004b3da78b0)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument group", value=group, expected_type=type_hints["group"])
            check_type(argname="argument kind", value=kind, expected_type=type_hints["kind"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
        if group is not None:
            self._values["group"] = group
        if kind is not None:
            self._values["kind"] = kind

    @builtins.property
    def name(self) -> builtins.str:
        '''Name of the resource being referred to.

        :schema: ChallengeSpecIssuerRef#name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def group(self) -> typing.Optional[builtins.str]:
        '''Group of the resource being referred to.

        :schema: ChallengeSpecIssuerRef#group
        '''
        result = self._values.get("group")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kind(self) -> typing.Optional[builtins.str]:
        '''Kind of the resource being referred to.

        :schema: ChallengeSpecIssuerRef#kind
        '''
        result = self._values.get("kind")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ChallengeSpecIssuerRef(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iocert-manageracme.ChallengeSpecSolver",
    jsii_struct_bases=[],
    name_mapping={"dns01": "dns01", "http01": "http01", "selector": "selector"},
)
class ChallengeSpecSolver:
    def __init__(
        self,
        *,
        dns01: typing.Optional[typing.Union["ChallengeSpecSolverDns01", typing.Dict[builtins.str, typing.Any]]] = None,
        http01: typing.Optional[typing.Union["ChallengeSpecSolverHttp01", typing.Dict[builtins.str, typing.Any]]] = None,
        selector: typing.Optional[typing.Union["ChallengeSpecSolverSelector", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''Contains the domain solving configuration that should be used to solve this challenge resource.

        :param dns01: Configures cert-manager to attempt to complete authorizations by performing the DNS01 challenge flow.
        :param http01: Configures cert-manager to attempt to complete authorizations by performing the HTTP01 challenge flow. It is not possible to obtain certificates for wildcard domain names (e.g. ``*.example.com``) using the HTTP01 challenge mechanism.
        :param selector: Selector selects a set of DNSNames on the Certificate resource that should be solved using this challenge solver. If not specified, the solver will be treated as the 'default' solver with the lowest priority, i.e. if any other solver has a more specific match, it will be used instead.

        :schema: ChallengeSpecSolver
        '''
        if isinstance(dns01, dict):
            dns01 = ChallengeSpecSolverDns01(**dns01)
        if isinstance(http01, dict):
            http01 = ChallengeSpecSolverHttp01(**http01)
        if isinstance(selector, dict):
            selector = ChallengeSpecSolverSelector(**selector)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7fe91530e269d0e86c228348f7893c1cf5e61f7789b2dca4a58b181c4e324211)
            check_type(argname="argument dns01", value=dns01, expected_type=type_hints["dns01"])
            check_type(argname="argument http01", value=http01, expected_type=type_hints["http01"])
            check_type(argname="argument selector", value=selector, expected_type=type_hints["selector"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if dns01 is not None:
            self._values["dns01"] = dns01
        if http01 is not None:
            self._values["http01"] = http01
        if selector is not None:
            self._values["selector"] = selector

    @builtins.property
    def dns01(self) -> typing.Optional["ChallengeSpecSolverDns01"]:
        '''Configures cert-manager to attempt to complete authorizations by performing the DNS01 challenge flow.

        :schema: ChallengeSpecSolver#dns01
        '''
        result = self._values.get("dns01")
        return typing.cast(typing.Optional["ChallengeSpecSolverDns01"], result)

    @builtins.property
    def http01(self) -> typing.Optional["ChallengeSpecSolverHttp01"]:
        '''Configures cert-manager to attempt to complete authorizations by performing the HTTP01 challenge flow.

        It is not possible to obtain certificates for wildcard domain names
        (e.g. ``*.example.com``) using the HTTP01 challenge mechanism.

        :schema: ChallengeSpecSolver#http01
        '''
        result = self._values.get("http01")
        return typing.cast(typing.Optional["ChallengeSpecSolverHttp01"], result)

    @builtins.property
    def selector(self) -> typing.Optional["ChallengeSpecSolverSelector"]:
        '''Selector selects a set of DNSNames on the Certificate resource that should be solved using this challenge solver.

        If not specified, the solver will be treated as the 'default' solver
        with the lowest priority, i.e. if any other solver has a more specific
        match, it will be used instead.

        :schema: ChallengeSpecSolver#selector
        '''
        result = self._values.get("selector")
        return typing.cast(typing.Optional["ChallengeSpecSolverSelector"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ChallengeSpecSolver(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iocert-manageracme.ChallengeSpecSolverDns01",
    jsii_struct_bases=[],
    name_mapping={
        "acme_dns": "acmeDns",
        "akamai": "akamai",
        "azure_dns": "azureDns",
        "cloud_dns": "cloudDns",
        "cloudflare": "cloudflare",
        "cname_strategy": "cnameStrategy",
        "digitalocean": "digitalocean",
        "rfc2136": "rfc2136",
        "route53": "route53",
        "webhook": "webhook",
    },
)
class ChallengeSpecSolverDns01:
    def __init__(
        self,
        *,
        acme_dns: typing.Optional[typing.Union["ChallengeSpecSolverDns01AcmeDns", typing.Dict[builtins.str, typing.Any]]] = None,
        akamai: typing.Optional[typing.Union["ChallengeSpecSolverDns01Akamai", typing.Dict[builtins.str, typing.Any]]] = None,
        azure_dns: typing.Optional[typing.Union["ChallengeSpecSolverDns01AzureDns", typing.Dict[builtins.str, typing.Any]]] = None,
        cloud_dns: typing.Optional[typing.Union["ChallengeSpecSolverDns01CloudDns", typing.Dict[builtins.str, typing.Any]]] = None,
        cloudflare: typing.Optional[typing.Union["ChallengeSpecSolverDns01Cloudflare", typing.Dict[builtins.str, typing.Any]]] = None,
        cname_strategy: typing.Optional["ChallengeSpecSolverDns01CnameStrategy"] = None,
        digitalocean: typing.Optional[typing.Union["ChallengeSpecSolverDns01Digitalocean", typing.Dict[builtins.str, typing.Any]]] = None,
        rfc2136: typing.Optional[typing.Union["ChallengeSpecSolverDns01Rfc2136", typing.Dict[builtins.str, typing.Any]]] = None,
        route53: typing.Optional[typing.Union["ChallengeSpecSolverDns01Route53", typing.Dict[builtins.str, typing.Any]]] = None,
        webhook: typing.Optional[typing.Union["ChallengeSpecSolverDns01Webhook", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''Configures cert-manager to attempt to complete authorizations by performing the DNS01 challenge flow.

        :param acme_dns: Use the 'ACME DNS' (https://github.com/joohoi/acme-dns) API to manage DNS01 challenge records.
        :param akamai: Use the Akamai DNS zone management API to manage DNS01 challenge records.
        :param azure_dns: Use the Microsoft Azure DNS API to manage DNS01 challenge records.
        :param cloud_dns: Use the Google Cloud DNS API to manage DNS01 challenge records.
        :param cloudflare: Use the Cloudflare API to manage DNS01 challenge records.
        :param cname_strategy: CNAMEStrategy configures how the DNS01 provider should handle CNAME records when found in DNS zones.
        :param digitalocean: Use the DigitalOcean DNS API to manage DNS01 challenge records.
        :param rfc2136: Use RFC2136 ("Dynamic Updates in the Domain Name System") (https://datatracker.ietf.org/doc/rfc2136/) to manage DNS01 challenge records.
        :param route53: Use the AWS Route53 API to manage DNS01 challenge records.
        :param webhook: Configure an external webhook based DNS01 challenge solver to manage DNS01 challenge records.

        :schema: ChallengeSpecSolverDns01
        '''
        if isinstance(acme_dns, dict):
            acme_dns = ChallengeSpecSolverDns01AcmeDns(**acme_dns)
        if isinstance(akamai, dict):
            akamai = ChallengeSpecSolverDns01Akamai(**akamai)
        if isinstance(azure_dns, dict):
            azure_dns = ChallengeSpecSolverDns01AzureDns(**azure_dns)
        if isinstance(cloud_dns, dict):
            cloud_dns = ChallengeSpecSolverDns01CloudDns(**cloud_dns)
        if isinstance(cloudflare, dict):
            cloudflare = ChallengeSpecSolverDns01Cloudflare(**cloudflare)
        if isinstance(digitalocean, dict):
            digitalocean = ChallengeSpecSolverDns01Digitalocean(**digitalocean)
        if isinstance(rfc2136, dict):
            rfc2136 = ChallengeSpecSolverDns01Rfc2136(**rfc2136)
        if isinstance(route53, dict):
            route53 = ChallengeSpecSolverDns01Route53(**route53)
        if isinstance(webhook, dict):
            webhook = ChallengeSpecSolverDns01Webhook(**webhook)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__142c470983c47888a0ad07b89f6066e68870d25c918279cc3c2bce30dd25f04c)
            check_type(argname="argument acme_dns", value=acme_dns, expected_type=type_hints["acme_dns"])
            check_type(argname="argument akamai", value=akamai, expected_type=type_hints["akamai"])
            check_type(argname="argument azure_dns", value=azure_dns, expected_type=type_hints["azure_dns"])
            check_type(argname="argument cloud_dns", value=cloud_dns, expected_type=type_hints["cloud_dns"])
            check_type(argname="argument cloudflare", value=cloudflare, expected_type=type_hints["cloudflare"])
            check_type(argname="argument cname_strategy", value=cname_strategy, expected_type=type_hints["cname_strategy"])
            check_type(argname="argument digitalocean", value=digitalocean, expected_type=type_hints["digitalocean"])
            check_type(argname="argument rfc2136", value=rfc2136, expected_type=type_hints["rfc2136"])
            check_type(argname="argument route53", value=route53, expected_type=type_hints["route53"])
            check_type(argname="argument webhook", value=webhook, expected_type=type_hints["webhook"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if acme_dns is not None:
            self._values["acme_dns"] = acme_dns
        if akamai is not None:
            self._values["akamai"] = akamai
        if azure_dns is not None:
            self._values["azure_dns"] = azure_dns
        if cloud_dns is not None:
            self._values["cloud_dns"] = cloud_dns
        if cloudflare is not None:
            self._values["cloudflare"] = cloudflare
        if cname_strategy is not None:
            self._values["cname_strategy"] = cname_strategy
        if digitalocean is not None:
            self._values["digitalocean"] = digitalocean
        if rfc2136 is not None:
            self._values["rfc2136"] = rfc2136
        if route53 is not None:
            self._values["route53"] = route53
        if webhook is not None:
            self._values["webhook"] = webhook

    @builtins.property
    def acme_dns(self) -> typing.Optional["ChallengeSpecSolverDns01AcmeDns"]:
        '''Use the 'ACME DNS' (https://github.com/joohoi/acme-dns) API to manage DNS01 challenge records.

        :schema: ChallengeSpecSolverDns01#acmeDNS
        '''
        result = self._values.get("acme_dns")
        return typing.cast(typing.Optional["ChallengeSpecSolverDns01AcmeDns"], result)

    @builtins.property
    def akamai(self) -> typing.Optional["ChallengeSpecSolverDns01Akamai"]:
        '''Use the Akamai DNS zone management API to manage DNS01 challenge records.

        :schema: ChallengeSpecSolverDns01#akamai
        '''
        result = self._values.get("akamai")
        return typing.cast(typing.Optional["ChallengeSpecSolverDns01Akamai"], result)

    @builtins.property
    def azure_dns(self) -> typing.Optional["ChallengeSpecSolverDns01AzureDns"]:
        '''Use the Microsoft Azure DNS API to manage DNS01 challenge records.

        :schema: ChallengeSpecSolverDns01#azureDNS
        '''
        result = self._values.get("azure_dns")
        return typing.cast(typing.Optional["ChallengeSpecSolverDns01AzureDns"], result)

    @builtins.property
    def cloud_dns(self) -> typing.Optional["ChallengeSpecSolverDns01CloudDns"]:
        '''Use the Google Cloud DNS API to manage DNS01 challenge records.

        :schema: ChallengeSpecSolverDns01#cloudDNS
        '''
        result = self._values.get("cloud_dns")
        return typing.cast(typing.Optional["ChallengeSpecSolverDns01CloudDns"], result)

    @builtins.property
    def cloudflare(self) -> typing.Optional["ChallengeSpecSolverDns01Cloudflare"]:
        '''Use the Cloudflare API to manage DNS01 challenge records.

        :schema: ChallengeSpecSolverDns01#cloudflare
        '''
        result = self._values.get("cloudflare")
        return typing.cast(typing.Optional["ChallengeSpecSolverDns01Cloudflare"], result)

    @builtins.property
    def cname_strategy(
        self,
    ) -> typing.Optional["ChallengeSpecSolverDns01CnameStrategy"]:
        '''CNAMEStrategy configures how the DNS01 provider should handle CNAME records when found in DNS zones.

        :schema: ChallengeSpecSolverDns01#cnameStrategy
        '''
        result = self._values.get("cname_strategy")
        return typing.cast(typing.Optional["ChallengeSpecSolverDns01CnameStrategy"], result)

    @builtins.property
    def digitalocean(self) -> typing.Optional["ChallengeSpecSolverDns01Digitalocean"]:
        '''Use the DigitalOcean DNS API to manage DNS01 challenge records.

        :schema: ChallengeSpecSolverDns01#digitalocean
        '''
        result = self._values.get("digitalocean")
        return typing.cast(typing.Optional["ChallengeSpecSolverDns01Digitalocean"], result)

    @builtins.property
    def rfc2136(self) -> typing.Optional["ChallengeSpecSolverDns01Rfc2136"]:
        '''Use RFC2136 ("Dynamic Updates in the Domain Name System") (https://datatracker.ietf.org/doc/rfc2136/) to manage DNS01 challenge records.

        :schema: ChallengeSpecSolverDns01#rfc2136
        '''
        result = self._values.get("rfc2136")
        return typing.cast(typing.Optional["ChallengeSpecSolverDns01Rfc2136"], result)

    @builtins.property
    def route53(self) -> typing.Optional["ChallengeSpecSolverDns01Route53"]:
        '''Use the AWS Route53 API to manage DNS01 challenge records.

        :schema: ChallengeSpecSolverDns01#route53
        '''
        result = self._values.get("route53")
        return typing.cast(typing.Optional["ChallengeSpecSolverDns01Route53"], result)

    @builtins.property
    def webhook(self) -> typing.Optional["ChallengeSpecSolverDns01Webhook"]:
        '''Configure an external webhook based DNS01 challenge solver to manage DNS01 challenge records.

        :schema: ChallengeSpecSolverDns01#webhook
        '''
        result = self._values.get("webhook")
        return typing.cast(typing.Optional["ChallengeSpecSolverDns01Webhook"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ChallengeSpecSolverDns01(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iocert-manageracme.ChallengeSpecSolverDns01AcmeDns",
    jsii_struct_bases=[],
    name_mapping={"account_secret_ref": "accountSecretRef", "host": "host"},
)
class ChallengeSpecSolverDns01AcmeDns:
    def __init__(
        self,
        *,
        account_secret_ref: typing.Union["ChallengeSpecSolverDns01AcmeDnsAccountSecretRef", typing.Dict[builtins.str, typing.Any]],
        host: builtins.str,
    ) -> None:
        '''Use the 'ACME DNS' (https://github.com/joohoi/acme-dns) API to manage DNS01 challenge records.

        :param account_secret_ref: A reference to a specific 'key' within a Secret resource. In some instances, ``key`` is a required field.
        :param host: 

        :schema: ChallengeSpecSolverDns01AcmeDns
        '''
        if isinstance(account_secret_ref, dict):
            account_secret_ref = ChallengeSpecSolverDns01AcmeDnsAccountSecretRef(**account_secret_ref)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__21db0ea3ffdfe07fd48344501eb8ce6530983242b8be2bf699e0d915a0129fda)
            check_type(argname="argument account_secret_ref", value=account_secret_ref, expected_type=type_hints["account_secret_ref"])
            check_type(argname="argument host", value=host, expected_type=type_hints["host"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "account_secret_ref": account_secret_ref,
            "host": host,
        }

    @builtins.property
    def account_secret_ref(self) -> "ChallengeSpecSolverDns01AcmeDnsAccountSecretRef":
        '''A reference to a specific 'key' within a Secret resource.

        In some instances, ``key`` is a required field.

        :schema: ChallengeSpecSolverDns01AcmeDns#accountSecretRef
        '''
        result = self._values.get("account_secret_ref")
        assert result is not None, "Required property 'account_secret_ref' is missing"
        return typing.cast("ChallengeSpecSolverDns01AcmeDnsAccountSecretRef", result)

    @builtins.property
    def host(self) -> builtins.str:
        '''
        :schema: ChallengeSpecSolverDns01AcmeDns#host
        '''
        result = self._values.get("host")
        assert result is not None, "Required property 'host' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ChallengeSpecSolverDns01AcmeDns(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iocert-manageracme.ChallengeSpecSolverDns01AcmeDnsAccountSecretRef",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "key": "key"},
)
class ChallengeSpecSolverDns01AcmeDnsAccountSecretRef:
    def __init__(
        self,
        *,
        name: builtins.str,
        key: typing.Optional[builtins.str] = None,
    ) -> None:
        '''A reference to a specific 'key' within a Secret resource.

        In some instances, ``key`` is a required field.

        :param name: Name of the resource being referred to. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names
        :param key: The key of the entry in the Secret resource's ``data`` field to be used. Some instances of this field may be defaulted, in others it may be required.

        :schema: ChallengeSpecSolverDns01AcmeDnsAccountSecretRef
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__986030aa12ea799599fe8422f90cd82f8530e8664e66be261f1333fdcb063ba2)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
        if key is not None:
            self._values["key"] = key

    @builtins.property
    def name(self) -> builtins.str:
        '''Name of the resource being referred to.

        More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names

        :schema: ChallengeSpecSolverDns01AcmeDnsAccountSecretRef#name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''The key of the entry in the Secret resource's ``data`` field to be used.

        Some instances of this field may be defaulted, in others it may be
        required.

        :schema: ChallengeSpecSolverDns01AcmeDnsAccountSecretRef#key
        '''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ChallengeSpecSolverDns01AcmeDnsAccountSecretRef(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iocert-manageracme.ChallengeSpecSolverDns01Akamai",
    jsii_struct_bases=[],
    name_mapping={
        "access_token_secret_ref": "accessTokenSecretRef",
        "client_secret_secret_ref": "clientSecretSecretRef",
        "client_token_secret_ref": "clientTokenSecretRef",
        "service_consumer_domain": "serviceConsumerDomain",
    },
)
class ChallengeSpecSolverDns01Akamai:
    def __init__(
        self,
        *,
        access_token_secret_ref: typing.Union["ChallengeSpecSolverDns01AkamaiAccessTokenSecretRef", typing.Dict[builtins.str, typing.Any]],
        client_secret_secret_ref: typing.Union["ChallengeSpecSolverDns01AkamaiClientSecretSecretRef", typing.Dict[builtins.str, typing.Any]],
        client_token_secret_ref: typing.Union["ChallengeSpecSolverDns01AkamaiClientTokenSecretRef", typing.Dict[builtins.str, typing.Any]],
        service_consumer_domain: builtins.str,
    ) -> None:
        '''Use the Akamai DNS zone management API to manage DNS01 challenge records.

        :param access_token_secret_ref: A reference to a specific 'key' within a Secret resource. In some instances, ``key`` is a required field.
        :param client_secret_secret_ref: A reference to a specific 'key' within a Secret resource. In some instances, ``key`` is a required field.
        :param client_token_secret_ref: A reference to a specific 'key' within a Secret resource. In some instances, ``key`` is a required field.
        :param service_consumer_domain: 

        :schema: ChallengeSpecSolverDns01Akamai
        '''
        if isinstance(access_token_secret_ref, dict):
            access_token_secret_ref = ChallengeSpecSolverDns01AkamaiAccessTokenSecretRef(**access_token_secret_ref)
        if isinstance(client_secret_secret_ref, dict):
            client_secret_secret_ref = ChallengeSpecSolverDns01AkamaiClientSecretSecretRef(**client_secret_secret_ref)
        if isinstance(client_token_secret_ref, dict):
            client_token_secret_ref = ChallengeSpecSolverDns01AkamaiClientTokenSecretRef(**client_token_secret_ref)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__734e95330244f4212829fe485864844bf3a43524b395afbdb7a074350d789b00)
            check_type(argname="argument access_token_secret_ref", value=access_token_secret_ref, expected_type=type_hints["access_token_secret_ref"])
            check_type(argname="argument client_secret_secret_ref", value=client_secret_secret_ref, expected_type=type_hints["client_secret_secret_ref"])
            check_type(argname="argument client_token_secret_ref", value=client_token_secret_ref, expected_type=type_hints["client_token_secret_ref"])
            check_type(argname="argument service_consumer_domain", value=service_consumer_domain, expected_type=type_hints["service_consumer_domain"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "access_token_secret_ref": access_token_secret_ref,
            "client_secret_secret_ref": client_secret_secret_ref,
            "client_token_secret_ref": client_token_secret_ref,
            "service_consumer_domain": service_consumer_domain,
        }

    @builtins.property
    def access_token_secret_ref(
        self,
    ) -> "ChallengeSpecSolverDns01AkamaiAccessTokenSecretRef":
        '''A reference to a specific 'key' within a Secret resource.

        In some instances, ``key`` is a required field.

        :schema: ChallengeSpecSolverDns01Akamai#accessTokenSecretRef
        '''
        result = self._values.get("access_token_secret_ref")
        assert result is not None, "Required property 'access_token_secret_ref' is missing"
        return typing.cast("ChallengeSpecSolverDns01AkamaiAccessTokenSecretRef", result)

    @builtins.property
    def client_secret_secret_ref(
        self,
    ) -> "ChallengeSpecSolverDns01AkamaiClientSecretSecretRef":
        '''A reference to a specific 'key' within a Secret resource.

        In some instances, ``key`` is a required field.

        :schema: ChallengeSpecSolverDns01Akamai#clientSecretSecretRef
        '''
        result = self._values.get("client_secret_secret_ref")
        assert result is not None, "Required property 'client_secret_secret_ref' is missing"
        return typing.cast("ChallengeSpecSolverDns01AkamaiClientSecretSecretRef", result)

    @builtins.property
    def client_token_secret_ref(
        self,
    ) -> "ChallengeSpecSolverDns01AkamaiClientTokenSecretRef":
        '''A reference to a specific 'key' within a Secret resource.

        In some instances, ``key`` is a required field.

        :schema: ChallengeSpecSolverDns01Akamai#clientTokenSecretRef
        '''
        result = self._values.get("client_token_secret_ref")
        assert result is not None, "Required property 'client_token_secret_ref' is missing"
        return typing.cast("ChallengeSpecSolverDns01AkamaiClientTokenSecretRef", result)

    @builtins.property
    def service_consumer_domain(self) -> builtins.str:
        '''
        :schema: ChallengeSpecSolverDns01Akamai#serviceConsumerDomain
        '''
        result = self._values.get("service_consumer_domain")
        assert result is not None, "Required property 'service_consumer_domain' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ChallengeSpecSolverDns01Akamai(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iocert-manageracme.ChallengeSpecSolverDns01AkamaiAccessTokenSecretRef",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "key": "key"},
)
class ChallengeSpecSolverDns01AkamaiAccessTokenSecretRef:
    def __init__(
        self,
        *,
        name: builtins.str,
        key: typing.Optional[builtins.str] = None,
    ) -> None:
        '''A reference to a specific 'key' within a Secret resource.

        In some instances, ``key`` is a required field.

        :param name: Name of the resource being referred to. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names
        :param key: The key of the entry in the Secret resource's ``data`` field to be used. Some instances of this field may be defaulted, in others it may be required.

        :schema: ChallengeSpecSolverDns01AkamaiAccessTokenSecretRef
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__257e1438acbbc299ef2d6df55ccc7d2078ad4e13ead5c6d41b4fd0ecd2718a61)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
        if key is not None:
            self._values["key"] = key

    @builtins.property
    def name(self) -> builtins.str:
        '''Name of the resource being referred to.

        More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names

        :schema: ChallengeSpecSolverDns01AkamaiAccessTokenSecretRef#name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''The key of the entry in the Secret resource's ``data`` field to be used.

        Some instances of this field may be defaulted, in others it may be
        required.

        :schema: ChallengeSpecSolverDns01AkamaiAccessTokenSecretRef#key
        '''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ChallengeSpecSolverDns01AkamaiAccessTokenSecretRef(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iocert-manageracme.ChallengeSpecSolverDns01AkamaiClientSecretSecretRef",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "key": "key"},
)
class ChallengeSpecSolverDns01AkamaiClientSecretSecretRef:
    def __init__(
        self,
        *,
        name: builtins.str,
        key: typing.Optional[builtins.str] = None,
    ) -> None:
        '''A reference to a specific 'key' within a Secret resource.

        In some instances, ``key`` is a required field.

        :param name: Name of the resource being referred to. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names
        :param key: The key of the entry in the Secret resource's ``data`` field to be used. Some instances of this field may be defaulted, in others it may be required.

        :schema: ChallengeSpecSolverDns01AkamaiClientSecretSecretRef
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e70693cc55de32af0b3ab9b24c3832c94eba49113cc0925dc71952ca1c01db42)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
        if key is not None:
            self._values["key"] = key

    @builtins.property
    def name(self) -> builtins.str:
        '''Name of the resource being referred to.

        More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names

        :schema: ChallengeSpecSolverDns01AkamaiClientSecretSecretRef#name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''The key of the entry in the Secret resource's ``data`` field to be used.

        Some instances of this field may be defaulted, in others it may be
        required.

        :schema: ChallengeSpecSolverDns01AkamaiClientSecretSecretRef#key
        '''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ChallengeSpecSolverDns01AkamaiClientSecretSecretRef(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iocert-manageracme.ChallengeSpecSolverDns01AkamaiClientTokenSecretRef",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "key": "key"},
)
class ChallengeSpecSolverDns01AkamaiClientTokenSecretRef:
    def __init__(
        self,
        *,
        name: builtins.str,
        key: typing.Optional[builtins.str] = None,
    ) -> None:
        '''A reference to a specific 'key' within a Secret resource.

        In some instances, ``key`` is a required field.

        :param name: Name of the resource being referred to. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names
        :param key: The key of the entry in the Secret resource's ``data`` field to be used. Some instances of this field may be defaulted, in others it may be required.

        :schema: ChallengeSpecSolverDns01AkamaiClientTokenSecretRef
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__776d36f7cda6b157c5d5a3f65e67ff629861adda10f1ec45ccc09c44caaa01be)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
        if key is not None:
            self._values["key"] = key

    @builtins.property
    def name(self) -> builtins.str:
        '''Name of the resource being referred to.

        More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names

        :schema: ChallengeSpecSolverDns01AkamaiClientTokenSecretRef#name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''The key of the entry in the Secret resource's ``data`` field to be used.

        Some instances of this field may be defaulted, in others it may be
        required.

        :schema: ChallengeSpecSolverDns01AkamaiClientTokenSecretRef#key
        '''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ChallengeSpecSolverDns01AkamaiClientTokenSecretRef(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iocert-manageracme.ChallengeSpecSolverDns01AzureDns",
    jsii_struct_bases=[],
    name_mapping={
        "resource_group_name": "resourceGroupName",
        "subscription_id": "subscriptionId",
        "client_id": "clientId",
        "client_secret_secret_ref": "clientSecretSecretRef",
        "environment": "environment",
        "hosted_zone_name": "hostedZoneName",
        "managed_identity": "managedIdentity",
        "tenant_id": "tenantId",
    },
)
class ChallengeSpecSolverDns01AzureDns:
    def __init__(
        self,
        *,
        resource_group_name: builtins.str,
        subscription_id: builtins.str,
        client_id: typing.Optional[builtins.str] = None,
        client_secret_secret_ref: typing.Optional[typing.Union["ChallengeSpecSolverDns01AzureDnsClientSecretSecretRef", typing.Dict[builtins.str, typing.Any]]] = None,
        environment: typing.Optional["ChallengeSpecSolverDns01AzureDnsEnvironment"] = None,
        hosted_zone_name: typing.Optional[builtins.str] = None,
        managed_identity: typing.Optional[typing.Union["ChallengeSpecSolverDns01AzureDnsManagedIdentity", typing.Dict[builtins.str, typing.Any]]] = None,
        tenant_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Use the Microsoft Azure DNS API to manage DNS01 challenge records.

        :param resource_group_name: resource group the DNS zone is located in.
        :param subscription_id: ID of the Azure subscription.
        :param client_id: Auth: Azure Service Principal: The ClientID of the Azure Service Principal used to authenticate with Azure DNS. If set, ClientSecret and TenantID must also be set.
        :param client_secret_secret_ref: Auth: Azure Service Principal: A reference to a Secret containing the password associated with the Service Principal. If set, ClientID and TenantID must also be set.
        :param environment: name of the Azure environment (default AzurePublicCloud).
        :param hosted_zone_name: name of the DNS zone that should be used.
        :param managed_identity: Auth: Azure Workload Identity or Azure Managed Service Identity: Settings to enable Azure Workload Identity or Azure Managed Service Identity If set, ClientID, ClientSecret and TenantID must not be set.
        :param tenant_id: Auth: Azure Service Principal: The TenantID of the Azure Service Principal used to authenticate with Azure DNS. If set, ClientID and ClientSecret must also be set.

        :schema: ChallengeSpecSolverDns01AzureDns
        '''
        if isinstance(client_secret_secret_ref, dict):
            client_secret_secret_ref = ChallengeSpecSolverDns01AzureDnsClientSecretSecretRef(**client_secret_secret_ref)
        if isinstance(managed_identity, dict):
            managed_identity = ChallengeSpecSolverDns01AzureDnsManagedIdentity(**managed_identity)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0c9f416728c3596e733c1b71ae04174983e3a388ddfd6d382db4fc61d5fd910a)
            check_type(argname="argument resource_group_name", value=resource_group_name, expected_type=type_hints["resource_group_name"])
            check_type(argname="argument subscription_id", value=subscription_id, expected_type=type_hints["subscription_id"])
            check_type(argname="argument client_id", value=client_id, expected_type=type_hints["client_id"])
            check_type(argname="argument client_secret_secret_ref", value=client_secret_secret_ref, expected_type=type_hints["client_secret_secret_ref"])
            check_type(argname="argument environment", value=environment, expected_type=type_hints["environment"])
            check_type(argname="argument hosted_zone_name", value=hosted_zone_name, expected_type=type_hints["hosted_zone_name"])
            check_type(argname="argument managed_identity", value=managed_identity, expected_type=type_hints["managed_identity"])
            check_type(argname="argument tenant_id", value=tenant_id, expected_type=type_hints["tenant_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "resource_group_name": resource_group_name,
            "subscription_id": subscription_id,
        }
        if client_id is not None:
            self._values["client_id"] = client_id
        if client_secret_secret_ref is not None:
            self._values["client_secret_secret_ref"] = client_secret_secret_ref
        if environment is not None:
            self._values["environment"] = environment
        if hosted_zone_name is not None:
            self._values["hosted_zone_name"] = hosted_zone_name
        if managed_identity is not None:
            self._values["managed_identity"] = managed_identity
        if tenant_id is not None:
            self._values["tenant_id"] = tenant_id

    @builtins.property
    def resource_group_name(self) -> builtins.str:
        '''resource group the DNS zone is located in.

        :schema: ChallengeSpecSolverDns01AzureDns#resourceGroupName
        '''
        result = self._values.get("resource_group_name")
        assert result is not None, "Required property 'resource_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def subscription_id(self) -> builtins.str:
        '''ID of the Azure subscription.

        :schema: ChallengeSpecSolverDns01AzureDns#subscriptionID
        '''
        result = self._values.get("subscription_id")
        assert result is not None, "Required property 'subscription_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def client_id(self) -> typing.Optional[builtins.str]:
        '''Auth: Azure Service Principal: The ClientID of the Azure Service Principal used to authenticate with Azure DNS.

        If set, ClientSecret and TenantID must also be set.

        :schema: ChallengeSpecSolverDns01AzureDns#clientID
        '''
        result = self._values.get("client_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def client_secret_secret_ref(
        self,
    ) -> typing.Optional["ChallengeSpecSolverDns01AzureDnsClientSecretSecretRef"]:
        '''Auth: Azure Service Principal: A reference to a Secret containing the password associated with the Service Principal.

        If set, ClientID and TenantID must also be set.

        :schema: ChallengeSpecSolverDns01AzureDns#clientSecretSecretRef
        '''
        result = self._values.get("client_secret_secret_ref")
        return typing.cast(typing.Optional["ChallengeSpecSolverDns01AzureDnsClientSecretSecretRef"], result)

    @builtins.property
    def environment(
        self,
    ) -> typing.Optional["ChallengeSpecSolverDns01AzureDnsEnvironment"]:
        '''name of the Azure environment (default AzurePublicCloud).

        :schema: ChallengeSpecSolverDns01AzureDns#environment
        '''
        result = self._values.get("environment")
        return typing.cast(typing.Optional["ChallengeSpecSolverDns01AzureDnsEnvironment"], result)

    @builtins.property
    def hosted_zone_name(self) -> typing.Optional[builtins.str]:
        '''name of the DNS zone that should be used.

        :schema: ChallengeSpecSolverDns01AzureDns#hostedZoneName
        '''
        result = self._values.get("hosted_zone_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def managed_identity(
        self,
    ) -> typing.Optional["ChallengeSpecSolverDns01AzureDnsManagedIdentity"]:
        '''Auth: Azure Workload Identity or Azure Managed Service Identity: Settings to enable Azure Workload Identity or Azure Managed Service Identity If set, ClientID, ClientSecret and TenantID must not be set.

        :schema: ChallengeSpecSolverDns01AzureDns#managedIdentity
        '''
        result = self._values.get("managed_identity")
        return typing.cast(typing.Optional["ChallengeSpecSolverDns01AzureDnsManagedIdentity"], result)

    @builtins.property
    def tenant_id(self) -> typing.Optional[builtins.str]:
        '''Auth: Azure Service Principal: The TenantID of the Azure Service Principal used to authenticate with Azure DNS.

        If set, ClientID and ClientSecret must also be set.

        :schema: ChallengeSpecSolverDns01AzureDns#tenantID
        '''
        result = self._values.get("tenant_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ChallengeSpecSolverDns01AzureDns(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iocert-manageracme.ChallengeSpecSolverDns01AzureDnsClientSecretSecretRef",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "key": "key"},
)
class ChallengeSpecSolverDns01AzureDnsClientSecretSecretRef:
    def __init__(
        self,
        *,
        name: builtins.str,
        key: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Auth: Azure Service Principal: A reference to a Secret containing the password associated with the Service Principal.

        If set, ClientID and TenantID must also be set.

        :param name: Name of the resource being referred to. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names
        :param key: The key of the entry in the Secret resource's ``data`` field to be used. Some instances of this field may be defaulted, in others it may be required.

        :schema: ChallengeSpecSolverDns01AzureDnsClientSecretSecretRef
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__81efc815086edcc6e2a218249043f32bae8c25dc3499f00b976be78f97b297e3)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
        if key is not None:
            self._values["key"] = key

    @builtins.property
    def name(self) -> builtins.str:
        '''Name of the resource being referred to.

        More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names

        :schema: ChallengeSpecSolverDns01AzureDnsClientSecretSecretRef#name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''The key of the entry in the Secret resource's ``data`` field to be used.

        Some instances of this field may be defaulted, in others it may be
        required.

        :schema: ChallengeSpecSolverDns01AzureDnsClientSecretSecretRef#key
        '''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ChallengeSpecSolverDns01AzureDnsClientSecretSecretRef(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="iocert-manageracme.ChallengeSpecSolverDns01AzureDnsEnvironment")
class ChallengeSpecSolverDns01AzureDnsEnvironment(enum.Enum):
    '''name of the Azure environment (default AzurePublicCloud).

    :schema: ChallengeSpecSolverDns01AzureDnsEnvironment
    '''

    AZURE_PUBLIC_CLOUD = "AZURE_PUBLIC_CLOUD"
    '''AzurePublicCloud.'''
    AZURE_CHINA_CLOUD = "AZURE_CHINA_CLOUD"
    '''AzureChinaCloud.'''
    AZURE_GERMAN_CLOUD = "AZURE_GERMAN_CLOUD"
    '''AzureGermanCloud.'''
    AZURE_US_GOVERNMENT_CLOUD = "AZURE_US_GOVERNMENT_CLOUD"
    '''AzureUSGovernmentCloud.'''


@jsii.data_type(
    jsii_type="iocert-manageracme.ChallengeSpecSolverDns01AzureDnsManagedIdentity",
    jsii_struct_bases=[],
    name_mapping={
        "client_id": "clientId",
        "resource_id": "resourceId",
        "tenant_id": "tenantId",
    },
)
class ChallengeSpecSolverDns01AzureDnsManagedIdentity:
    def __init__(
        self,
        *,
        client_id: typing.Optional[builtins.str] = None,
        resource_id: typing.Optional[builtins.str] = None,
        tenant_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Auth: Azure Workload Identity or Azure Managed Service Identity: Settings to enable Azure Workload Identity or Azure Managed Service Identity If set, ClientID, ClientSecret and TenantID must not be set.

        :param client_id: client ID of the managed identity, can not be used at the same time as resourceID.
        :param resource_id: resource ID of the managed identity, can not be used at the same time as clientID Cannot be used for Azure Managed Service Identity.
        :param tenant_id: tenant ID of the managed identity, can not be used at the same time as resourceID.

        :schema: ChallengeSpecSolverDns01AzureDnsManagedIdentity
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__75354e7c5ed12ae459903b20162ed781424cb666f5ffc8055d8454b256d9d047)
            check_type(argname="argument client_id", value=client_id, expected_type=type_hints["client_id"])
            check_type(argname="argument resource_id", value=resource_id, expected_type=type_hints["resource_id"])
            check_type(argname="argument tenant_id", value=tenant_id, expected_type=type_hints["tenant_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if client_id is not None:
            self._values["client_id"] = client_id
        if resource_id is not None:
            self._values["resource_id"] = resource_id
        if tenant_id is not None:
            self._values["tenant_id"] = tenant_id

    @builtins.property
    def client_id(self) -> typing.Optional[builtins.str]:
        '''client ID of the managed identity, can not be used at the same time as resourceID.

        :schema: ChallengeSpecSolverDns01AzureDnsManagedIdentity#clientID
        '''
        result = self._values.get("client_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def resource_id(self) -> typing.Optional[builtins.str]:
        '''resource ID of the managed identity, can not be used at the same time as clientID Cannot be used for Azure Managed Service Identity.

        :schema: ChallengeSpecSolverDns01AzureDnsManagedIdentity#resourceID
        '''
        result = self._values.get("resource_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tenant_id(self) -> typing.Optional[builtins.str]:
        '''tenant ID of the managed identity, can not be used at the same time as resourceID.

        :schema: ChallengeSpecSolverDns01AzureDnsManagedIdentity#tenantID
        '''
        result = self._values.get("tenant_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ChallengeSpecSolverDns01AzureDnsManagedIdentity(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iocert-manageracme.ChallengeSpecSolverDns01CloudDns",
    jsii_struct_bases=[],
    name_mapping={
        "project": "project",
        "hosted_zone_name": "hostedZoneName",
        "service_account_secret_ref": "serviceAccountSecretRef",
    },
)
class ChallengeSpecSolverDns01CloudDns:
    def __init__(
        self,
        *,
        project: builtins.str,
        hosted_zone_name: typing.Optional[builtins.str] = None,
        service_account_secret_ref: typing.Optional[typing.Union["ChallengeSpecSolverDns01CloudDnsServiceAccountSecretRef", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''Use the Google Cloud DNS API to manage DNS01 challenge records.

        :param project: 
        :param hosted_zone_name: HostedZoneName is an optional field that tells cert-manager in which Cloud DNS zone the challenge record has to be created. If left empty cert-manager will automatically choose a zone.
        :param service_account_secret_ref: A reference to a specific 'key' within a Secret resource. In some instances, ``key`` is a required field.

        :schema: ChallengeSpecSolverDns01CloudDns
        '''
        if isinstance(service_account_secret_ref, dict):
            service_account_secret_ref = ChallengeSpecSolverDns01CloudDnsServiceAccountSecretRef(**service_account_secret_ref)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__819643347ab362ace9c9e97d35cc6222cc568953d39007b282b7cc242a1a9075)
            check_type(argname="argument project", value=project, expected_type=type_hints["project"])
            check_type(argname="argument hosted_zone_name", value=hosted_zone_name, expected_type=type_hints["hosted_zone_name"])
            check_type(argname="argument service_account_secret_ref", value=service_account_secret_ref, expected_type=type_hints["service_account_secret_ref"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "project": project,
        }
        if hosted_zone_name is not None:
            self._values["hosted_zone_name"] = hosted_zone_name
        if service_account_secret_ref is not None:
            self._values["service_account_secret_ref"] = service_account_secret_ref

    @builtins.property
    def project(self) -> builtins.str:
        '''
        :schema: ChallengeSpecSolverDns01CloudDns#project
        '''
        result = self._values.get("project")
        assert result is not None, "Required property 'project' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def hosted_zone_name(self) -> typing.Optional[builtins.str]:
        '''HostedZoneName is an optional field that tells cert-manager in which Cloud DNS zone the challenge record has to be created.

        If left empty cert-manager will automatically choose a zone.

        :schema: ChallengeSpecSolverDns01CloudDns#hostedZoneName
        '''
        result = self._values.get("hosted_zone_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def service_account_secret_ref(
        self,
    ) -> typing.Optional["ChallengeSpecSolverDns01CloudDnsServiceAccountSecretRef"]:
        '''A reference to a specific 'key' within a Secret resource.

        In some instances, ``key`` is a required field.

        :schema: ChallengeSpecSolverDns01CloudDns#serviceAccountSecretRef
        '''
        result = self._values.get("service_account_secret_ref")
        return typing.cast(typing.Optional["ChallengeSpecSolverDns01CloudDnsServiceAccountSecretRef"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ChallengeSpecSolverDns01CloudDns(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iocert-manageracme.ChallengeSpecSolverDns01CloudDnsServiceAccountSecretRef",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "key": "key"},
)
class ChallengeSpecSolverDns01CloudDnsServiceAccountSecretRef:
    def __init__(
        self,
        *,
        name: builtins.str,
        key: typing.Optional[builtins.str] = None,
    ) -> None:
        '''A reference to a specific 'key' within a Secret resource.

        In some instances, ``key`` is a required field.

        :param name: Name of the resource being referred to. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names
        :param key: The key of the entry in the Secret resource's ``data`` field to be used. Some instances of this field may be defaulted, in others it may be required.

        :schema: ChallengeSpecSolverDns01CloudDnsServiceAccountSecretRef
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b2ef723db7f6487468dee108aff10a8190c97f734b1c32b82407ac1ba86477e6)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
        if key is not None:
            self._values["key"] = key

    @builtins.property
    def name(self) -> builtins.str:
        '''Name of the resource being referred to.

        More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names

        :schema: ChallengeSpecSolverDns01CloudDnsServiceAccountSecretRef#name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''The key of the entry in the Secret resource's ``data`` field to be used.

        Some instances of this field may be defaulted, in others it may be
        required.

        :schema: ChallengeSpecSolverDns01CloudDnsServiceAccountSecretRef#key
        '''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ChallengeSpecSolverDns01CloudDnsServiceAccountSecretRef(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iocert-manageracme.ChallengeSpecSolverDns01Cloudflare",
    jsii_struct_bases=[],
    name_mapping={
        "api_key_secret_ref": "apiKeySecretRef",
        "api_token_secret_ref": "apiTokenSecretRef",
        "email": "email",
    },
)
class ChallengeSpecSolverDns01Cloudflare:
    def __init__(
        self,
        *,
        api_key_secret_ref: typing.Optional[typing.Union["ChallengeSpecSolverDns01CloudflareApiKeySecretRef", typing.Dict[builtins.str, typing.Any]]] = None,
        api_token_secret_ref: typing.Optional[typing.Union["ChallengeSpecSolverDns01CloudflareApiTokenSecretRef", typing.Dict[builtins.str, typing.Any]]] = None,
        email: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Use the Cloudflare API to manage DNS01 challenge records.

        :param api_key_secret_ref: API key to use to authenticate with Cloudflare. Note: using an API token to authenticate is now the recommended method as it allows greater control of permissions.
        :param api_token_secret_ref: API token used to authenticate with Cloudflare.
        :param email: Email of the account, only required when using API key based authentication.

        :schema: ChallengeSpecSolverDns01Cloudflare
        '''
        if isinstance(api_key_secret_ref, dict):
            api_key_secret_ref = ChallengeSpecSolverDns01CloudflareApiKeySecretRef(**api_key_secret_ref)
        if isinstance(api_token_secret_ref, dict):
            api_token_secret_ref = ChallengeSpecSolverDns01CloudflareApiTokenSecretRef(**api_token_secret_ref)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__18354a1c6f09f77d8ee3e6b15f576df12059d0e4e4b1bfa6211982da44e87d14)
            check_type(argname="argument api_key_secret_ref", value=api_key_secret_ref, expected_type=type_hints["api_key_secret_ref"])
            check_type(argname="argument api_token_secret_ref", value=api_token_secret_ref, expected_type=type_hints["api_token_secret_ref"])
            check_type(argname="argument email", value=email, expected_type=type_hints["email"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if api_key_secret_ref is not None:
            self._values["api_key_secret_ref"] = api_key_secret_ref
        if api_token_secret_ref is not None:
            self._values["api_token_secret_ref"] = api_token_secret_ref
        if email is not None:
            self._values["email"] = email

    @builtins.property
    def api_key_secret_ref(
        self,
    ) -> typing.Optional["ChallengeSpecSolverDns01CloudflareApiKeySecretRef"]:
        '''API key to use to authenticate with Cloudflare.

        Note: using an API token to authenticate is now the recommended method
        as it allows greater control of permissions.

        :schema: ChallengeSpecSolverDns01Cloudflare#apiKeySecretRef
        '''
        result = self._values.get("api_key_secret_ref")
        return typing.cast(typing.Optional["ChallengeSpecSolverDns01CloudflareApiKeySecretRef"], result)

    @builtins.property
    def api_token_secret_ref(
        self,
    ) -> typing.Optional["ChallengeSpecSolverDns01CloudflareApiTokenSecretRef"]:
        '''API token used to authenticate with Cloudflare.

        :schema: ChallengeSpecSolverDns01Cloudflare#apiTokenSecretRef
        '''
        result = self._values.get("api_token_secret_ref")
        return typing.cast(typing.Optional["ChallengeSpecSolverDns01CloudflareApiTokenSecretRef"], result)

    @builtins.property
    def email(self) -> typing.Optional[builtins.str]:
        '''Email of the account, only required when using API key based authentication.

        :schema: ChallengeSpecSolverDns01Cloudflare#email
        '''
        result = self._values.get("email")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ChallengeSpecSolverDns01Cloudflare(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iocert-manageracme.ChallengeSpecSolverDns01CloudflareApiKeySecretRef",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "key": "key"},
)
class ChallengeSpecSolverDns01CloudflareApiKeySecretRef:
    def __init__(
        self,
        *,
        name: builtins.str,
        key: typing.Optional[builtins.str] = None,
    ) -> None:
        '''API key to use to authenticate with Cloudflare.

        Note: using an API token to authenticate is now the recommended method
        as it allows greater control of permissions.

        :param name: Name of the resource being referred to. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names
        :param key: The key of the entry in the Secret resource's ``data`` field to be used. Some instances of this field may be defaulted, in others it may be required.

        :schema: ChallengeSpecSolverDns01CloudflareApiKeySecretRef
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5436bd913867de2bc24a3933fe356518fd6c5e4243d1bcdc163bc2dfcf10cb06)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
        if key is not None:
            self._values["key"] = key

    @builtins.property
    def name(self) -> builtins.str:
        '''Name of the resource being referred to.

        More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names

        :schema: ChallengeSpecSolverDns01CloudflareApiKeySecretRef#name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''The key of the entry in the Secret resource's ``data`` field to be used.

        Some instances of this field may be defaulted, in others it may be
        required.

        :schema: ChallengeSpecSolverDns01CloudflareApiKeySecretRef#key
        '''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ChallengeSpecSolverDns01CloudflareApiKeySecretRef(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iocert-manageracme.ChallengeSpecSolverDns01CloudflareApiTokenSecretRef",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "key": "key"},
)
class ChallengeSpecSolverDns01CloudflareApiTokenSecretRef:
    def __init__(
        self,
        *,
        name: builtins.str,
        key: typing.Optional[builtins.str] = None,
    ) -> None:
        '''API token used to authenticate with Cloudflare.

        :param name: Name of the resource being referred to. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names
        :param key: The key of the entry in the Secret resource's ``data`` field to be used. Some instances of this field may be defaulted, in others it may be required.

        :schema: ChallengeSpecSolverDns01CloudflareApiTokenSecretRef
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9a75677ce3e59cb343bbbaa112e9c83f123ceb805a0c4dcbaf92c339dce4c80e)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
        if key is not None:
            self._values["key"] = key

    @builtins.property
    def name(self) -> builtins.str:
        '''Name of the resource being referred to.

        More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names

        :schema: ChallengeSpecSolverDns01CloudflareApiTokenSecretRef#name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''The key of the entry in the Secret resource's ``data`` field to be used.

        Some instances of this field may be defaulted, in others it may be
        required.

        :schema: ChallengeSpecSolverDns01CloudflareApiTokenSecretRef#key
        '''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ChallengeSpecSolverDns01CloudflareApiTokenSecretRef(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="iocert-manageracme.ChallengeSpecSolverDns01CnameStrategy")
class ChallengeSpecSolverDns01CnameStrategy(enum.Enum):
    '''CNAMEStrategy configures how the DNS01 provider should handle CNAME records when found in DNS zones.

    :schema: ChallengeSpecSolverDns01CnameStrategy
    '''

    NONE = "NONE"
    '''None.'''
    FOLLOW = "FOLLOW"
    '''Follow.'''


@jsii.data_type(
    jsii_type="iocert-manageracme.ChallengeSpecSolverDns01Digitalocean",
    jsii_struct_bases=[],
    name_mapping={"token_secret_ref": "tokenSecretRef"},
)
class ChallengeSpecSolverDns01Digitalocean:
    def __init__(
        self,
        *,
        token_secret_ref: typing.Union["ChallengeSpecSolverDns01DigitaloceanTokenSecretRef", typing.Dict[builtins.str, typing.Any]],
    ) -> None:
        '''Use the DigitalOcean DNS API to manage DNS01 challenge records.

        :param token_secret_ref: A reference to a specific 'key' within a Secret resource. In some instances, ``key`` is a required field.

        :schema: ChallengeSpecSolverDns01Digitalocean
        '''
        if isinstance(token_secret_ref, dict):
            token_secret_ref = ChallengeSpecSolverDns01DigitaloceanTokenSecretRef(**token_secret_ref)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c9e736a96f44fcedb899e4f053b97f9aadf82bdc61f987147f813d3eb5253edd)
            check_type(argname="argument token_secret_ref", value=token_secret_ref, expected_type=type_hints["token_secret_ref"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "token_secret_ref": token_secret_ref,
        }

    @builtins.property
    def token_secret_ref(self) -> "ChallengeSpecSolverDns01DigitaloceanTokenSecretRef":
        '''A reference to a specific 'key' within a Secret resource.

        In some instances, ``key`` is a required field.

        :schema: ChallengeSpecSolverDns01Digitalocean#tokenSecretRef
        '''
        result = self._values.get("token_secret_ref")
        assert result is not None, "Required property 'token_secret_ref' is missing"
        return typing.cast("ChallengeSpecSolverDns01DigitaloceanTokenSecretRef", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ChallengeSpecSolverDns01Digitalocean(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iocert-manageracme.ChallengeSpecSolverDns01DigitaloceanTokenSecretRef",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "key": "key"},
)
class ChallengeSpecSolverDns01DigitaloceanTokenSecretRef:
    def __init__(
        self,
        *,
        name: builtins.str,
        key: typing.Optional[builtins.str] = None,
    ) -> None:
        '''A reference to a specific 'key' within a Secret resource.

        In some instances, ``key`` is a required field.

        :param name: Name of the resource being referred to. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names
        :param key: The key of the entry in the Secret resource's ``data`` field to be used. Some instances of this field may be defaulted, in others it may be required.

        :schema: ChallengeSpecSolverDns01DigitaloceanTokenSecretRef
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__01f2c57e77addbe75dc86b4d371f50e479a6f9dc8aa791934442a075d6bfe5da)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
        if key is not None:
            self._values["key"] = key

    @builtins.property
    def name(self) -> builtins.str:
        '''Name of the resource being referred to.

        More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names

        :schema: ChallengeSpecSolverDns01DigitaloceanTokenSecretRef#name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''The key of the entry in the Secret resource's ``data`` field to be used.

        Some instances of this field may be defaulted, in others it may be
        required.

        :schema: ChallengeSpecSolverDns01DigitaloceanTokenSecretRef#key
        '''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ChallengeSpecSolverDns01DigitaloceanTokenSecretRef(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iocert-manageracme.ChallengeSpecSolverDns01Rfc2136",
    jsii_struct_bases=[],
    name_mapping={
        "nameserver": "nameserver",
        "tsig_algorithm": "tsigAlgorithm",
        "tsig_key_name": "tsigKeyName",
        "tsig_secret_secret_ref": "tsigSecretSecretRef",
    },
)
class ChallengeSpecSolverDns01Rfc2136:
    def __init__(
        self,
        *,
        nameserver: builtins.str,
        tsig_algorithm: typing.Optional[builtins.str] = None,
        tsig_key_name: typing.Optional[builtins.str] = None,
        tsig_secret_secret_ref: typing.Optional[typing.Union["ChallengeSpecSolverDns01Rfc2136TsigSecretSecretRef", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''Use RFC2136 ("Dynamic Updates in the Domain Name System") (https://datatracker.ietf.org/doc/rfc2136/) to manage DNS01 challenge records.

        :param nameserver: The IP address or hostname of an authoritative DNS server supporting RFC2136 in the form host:port. If the host is an IPv6 address it must be enclosed in square brackets (e.g [2001:db8::1]) ; port is optional. This field is required.
        :param tsig_algorithm: The TSIG Algorithm configured in the DNS supporting RFC2136. Used only when ``tsigSecretSecretRef`` and ``tsigKeyName`` are defined. Supported values are (case-insensitive): ``HMACMD5`` (default), ``HMACSHA1``, ``HMACSHA256`` or ``HMACSHA512``.
        :param tsig_key_name: The TSIG Key name configured in the DNS. If ``tsigSecretSecretRef`` is defined, this field is required.
        :param tsig_secret_secret_ref: The name of the secret containing the TSIG value. If ``tsigKeyName`` is defined, this field is required.

        :schema: ChallengeSpecSolverDns01Rfc2136
        '''
        if isinstance(tsig_secret_secret_ref, dict):
            tsig_secret_secret_ref = ChallengeSpecSolverDns01Rfc2136TsigSecretSecretRef(**tsig_secret_secret_ref)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__158fe4c810428e7ad9d57f33d26355d668258cf3c182eadd6959722c45eaaf6f)
            check_type(argname="argument nameserver", value=nameserver, expected_type=type_hints["nameserver"])
            check_type(argname="argument tsig_algorithm", value=tsig_algorithm, expected_type=type_hints["tsig_algorithm"])
            check_type(argname="argument tsig_key_name", value=tsig_key_name, expected_type=type_hints["tsig_key_name"])
            check_type(argname="argument tsig_secret_secret_ref", value=tsig_secret_secret_ref, expected_type=type_hints["tsig_secret_secret_ref"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "nameserver": nameserver,
        }
        if tsig_algorithm is not None:
            self._values["tsig_algorithm"] = tsig_algorithm
        if tsig_key_name is not None:
            self._values["tsig_key_name"] = tsig_key_name
        if tsig_secret_secret_ref is not None:
            self._values["tsig_secret_secret_ref"] = tsig_secret_secret_ref

    @builtins.property
    def nameserver(self) -> builtins.str:
        '''The IP address or hostname of an authoritative DNS server supporting RFC2136 in the form host:port.

        If the host is an IPv6 address it must be
        enclosed in square brackets (e.g [2001:db8::1]) ; port is optional.
        This field is required.

        :schema: ChallengeSpecSolverDns01Rfc2136#nameserver
        '''
        result = self._values.get("nameserver")
        assert result is not None, "Required property 'nameserver' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def tsig_algorithm(self) -> typing.Optional[builtins.str]:
        '''The TSIG Algorithm configured in the DNS supporting RFC2136.

        Used only
        when ``tsigSecretSecretRef`` and ``tsigKeyName`` are defined.
        Supported values are (case-insensitive): ``HMACMD5`` (default),
        ``HMACSHA1``, ``HMACSHA256`` or ``HMACSHA512``.

        :schema: ChallengeSpecSolverDns01Rfc2136#tsigAlgorithm
        '''
        result = self._values.get("tsig_algorithm")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tsig_key_name(self) -> typing.Optional[builtins.str]:
        '''The TSIG Key name configured in the DNS.

        If ``tsigSecretSecretRef`` is defined, this field is required.

        :schema: ChallengeSpecSolverDns01Rfc2136#tsigKeyName
        '''
        result = self._values.get("tsig_key_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tsig_secret_secret_ref(
        self,
    ) -> typing.Optional["ChallengeSpecSolverDns01Rfc2136TsigSecretSecretRef"]:
        '''The name of the secret containing the TSIG value.

        If ``tsigKeyName`` is defined, this field is required.

        :schema: ChallengeSpecSolverDns01Rfc2136#tsigSecretSecretRef
        '''
        result = self._values.get("tsig_secret_secret_ref")
        return typing.cast(typing.Optional["ChallengeSpecSolverDns01Rfc2136TsigSecretSecretRef"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ChallengeSpecSolverDns01Rfc2136(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iocert-manageracme.ChallengeSpecSolverDns01Rfc2136TsigSecretSecretRef",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "key": "key"},
)
class ChallengeSpecSolverDns01Rfc2136TsigSecretSecretRef:
    def __init__(
        self,
        *,
        name: builtins.str,
        key: typing.Optional[builtins.str] = None,
    ) -> None:
        '''The name of the secret containing the TSIG value.

        If ``tsigKeyName`` is defined, this field is required.

        :param name: Name of the resource being referred to. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names
        :param key: The key of the entry in the Secret resource's ``data`` field to be used. Some instances of this field may be defaulted, in others it may be required.

        :schema: ChallengeSpecSolverDns01Rfc2136TsigSecretSecretRef
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aaae4e30208cda828258ac55090d346880712829510d2a7afecd39687c000996)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
        if key is not None:
            self._values["key"] = key

    @builtins.property
    def name(self) -> builtins.str:
        '''Name of the resource being referred to.

        More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names

        :schema: ChallengeSpecSolverDns01Rfc2136TsigSecretSecretRef#name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''The key of the entry in the Secret resource's ``data`` field to be used.

        Some instances of this field may be defaulted, in others it may be
        required.

        :schema: ChallengeSpecSolverDns01Rfc2136TsigSecretSecretRef#key
        '''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ChallengeSpecSolverDns01Rfc2136TsigSecretSecretRef(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iocert-manageracme.ChallengeSpecSolverDns01Route53",
    jsii_struct_bases=[],
    name_mapping={
        "access_key_id": "accessKeyId",
        "access_key_id_secret_ref": "accessKeyIdSecretRef",
        "auth": "auth",
        "hosted_zone_id": "hostedZoneId",
        "region": "region",
        "role": "role",
        "secret_access_key_secret_ref": "secretAccessKeySecretRef",
    },
)
class ChallengeSpecSolverDns01Route53:
    def __init__(
        self,
        *,
        access_key_id: typing.Optional[builtins.str] = None,
        access_key_id_secret_ref: typing.Optional[typing.Union["ChallengeSpecSolverDns01Route53AccessKeyIdSecretRef", typing.Dict[builtins.str, typing.Any]]] = None,
        auth: typing.Optional[typing.Union["ChallengeSpecSolverDns01Route53Auth", typing.Dict[builtins.str, typing.Any]]] = None,
        hosted_zone_id: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        role: typing.Optional[builtins.str] = None,
        secret_access_key_secret_ref: typing.Optional[typing.Union["ChallengeSpecSolverDns01Route53SecretAccessKeySecretRef", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''Use the AWS Route53 API to manage DNS01 challenge records.

        :param access_key_id: The AccessKeyID is used for authentication. Cannot be set when SecretAccessKeyID is set. If neither the Access Key nor Key ID are set, we fall-back to using env vars, shared credentials file or AWS Instance metadata, see: https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/configuring-sdk.html#specifying-credentials
        :param access_key_id_secret_ref: The SecretAccessKey is used for authentication. If set, pull the AWS access key ID from a key within a Kubernetes Secret. Cannot be set when AccessKeyID is set. If neither the Access Key nor Key ID are set, we fall-back to using env vars, shared credentials file or AWS Instance metadata, see: https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/configuring-sdk.html#specifying-credentials
        :param auth: Auth configures how cert-manager authenticates.
        :param hosted_zone_id: If set, the provider will manage only this zone in Route53 and will not do a lookup using the route53:ListHostedZonesByName api call.
        :param region: Override the AWS region. Route53 is a global service and does not have regional endpoints but the region specified here (or via environment variables) is used as a hint to help compute the correct AWS credential scope and partition when it connects to Route53. See: - `Amazon Route 53 endpoints and quotas <https://docs.aws.amazon.com/general/latest/gr/r53.html>`_ - `Global services <https://docs.aws.amazon.com/whitepapers/latest/aws-fault-isolation-boundaries/global-services.html>`_ If you omit this region field, cert-manager will use the region from AWS_REGION and AWS_DEFAULT_REGION environment variables, if they are set in the cert-manager controller Pod. The ``region`` field is not needed if you use `IAM Roles for Service Accounts (IRSA) <https://docs.aws.amazon.com/eks/latest/userguide/iam-roles-for-service-accounts.html>`_. Instead an AWS_REGION environment variable is added to the cert-manager controller Pod by: `Amazon EKS Pod Identity Webhook <https://github.com/aws/amazon-eks-pod-identity-webhook>`_. In this case this ``region`` field value is ignored. The ``region`` field is not needed if you use `EKS Pod Identities <https://docs.aws.amazon.com/eks/latest/userguide/pod-identities.html>`_. Instead an AWS_REGION environment variable is added to the cert-manager controller Pod by: `Amazon EKS Pod Identity Agent <https://github.com/aws/eks-pod-identity-agent>`_, In this case this ``region`` field value is ignored.
        :param role: Role is a Role ARN which the Route53 provider will assume using either the explicit credentials AccessKeyID/SecretAccessKey or the inferred credentials from environment variables, shared credentials file or AWS Instance metadata.
        :param secret_access_key_secret_ref: The SecretAccessKey is used for authentication. If neither the Access Key nor Key ID are set, we fall-back to using env vars, shared credentials file or AWS Instance metadata, see: https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/configuring-sdk.html#specifying-credentials

        :schema: ChallengeSpecSolverDns01Route53
        '''
        if isinstance(access_key_id_secret_ref, dict):
            access_key_id_secret_ref = ChallengeSpecSolverDns01Route53AccessKeyIdSecretRef(**access_key_id_secret_ref)
        if isinstance(auth, dict):
            auth = ChallengeSpecSolverDns01Route53Auth(**auth)
        if isinstance(secret_access_key_secret_ref, dict):
            secret_access_key_secret_ref = ChallengeSpecSolverDns01Route53SecretAccessKeySecretRef(**secret_access_key_secret_ref)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f2ce54f74f48a04e478bd66fba9cfbb31158b769cdf7f9177d19878c8a130b15)
            check_type(argname="argument access_key_id", value=access_key_id, expected_type=type_hints["access_key_id"])
            check_type(argname="argument access_key_id_secret_ref", value=access_key_id_secret_ref, expected_type=type_hints["access_key_id_secret_ref"])
            check_type(argname="argument auth", value=auth, expected_type=type_hints["auth"])
            check_type(argname="argument hosted_zone_id", value=hosted_zone_id, expected_type=type_hints["hosted_zone_id"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument role", value=role, expected_type=type_hints["role"])
            check_type(argname="argument secret_access_key_secret_ref", value=secret_access_key_secret_ref, expected_type=type_hints["secret_access_key_secret_ref"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if access_key_id is not None:
            self._values["access_key_id"] = access_key_id
        if access_key_id_secret_ref is not None:
            self._values["access_key_id_secret_ref"] = access_key_id_secret_ref
        if auth is not None:
            self._values["auth"] = auth
        if hosted_zone_id is not None:
            self._values["hosted_zone_id"] = hosted_zone_id
        if region is not None:
            self._values["region"] = region
        if role is not None:
            self._values["role"] = role
        if secret_access_key_secret_ref is not None:
            self._values["secret_access_key_secret_ref"] = secret_access_key_secret_ref

    @builtins.property
    def access_key_id(self) -> typing.Optional[builtins.str]:
        '''The AccessKeyID is used for authentication.

        Cannot be set when SecretAccessKeyID is set.
        If neither the Access Key nor Key ID are set, we fall-back to using env
        vars, shared credentials file or AWS Instance metadata,
        see: https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/configuring-sdk.html#specifying-credentials

        :schema: ChallengeSpecSolverDns01Route53#accessKeyID
        '''
        result = self._values.get("access_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def access_key_id_secret_ref(
        self,
    ) -> typing.Optional["ChallengeSpecSolverDns01Route53AccessKeyIdSecretRef"]:
        '''The SecretAccessKey is used for authentication.

        If set, pull the AWS
        access key ID from a key within a Kubernetes Secret.
        Cannot be set when AccessKeyID is set.
        If neither the Access Key nor Key ID are set, we fall-back to using env
        vars, shared credentials file or AWS Instance metadata,
        see: https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/configuring-sdk.html#specifying-credentials

        :schema: ChallengeSpecSolverDns01Route53#accessKeyIDSecretRef
        '''
        result = self._values.get("access_key_id_secret_ref")
        return typing.cast(typing.Optional["ChallengeSpecSolverDns01Route53AccessKeyIdSecretRef"], result)

    @builtins.property
    def auth(self) -> typing.Optional["ChallengeSpecSolverDns01Route53Auth"]:
        '''Auth configures how cert-manager authenticates.

        :schema: ChallengeSpecSolverDns01Route53#auth
        '''
        result = self._values.get("auth")
        return typing.cast(typing.Optional["ChallengeSpecSolverDns01Route53Auth"], result)

    @builtins.property
    def hosted_zone_id(self) -> typing.Optional[builtins.str]:
        '''If set, the provider will manage only this zone in Route53 and will not do a lookup using the route53:ListHostedZonesByName api call.

        :schema: ChallengeSpecSolverDns01Route53#hostedZoneID
        '''
        result = self._values.get("hosted_zone_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''Override the AWS region.

        Route53 is a global service and does not have regional endpoints but the
        region specified here (or via environment variables) is used as a hint to
        help compute the correct AWS credential scope and partition when it
        connects to Route53. See:

        - `Amazon Route 53 endpoints and quotas <https://docs.aws.amazon.com/general/latest/gr/r53.html>`_
        - `Global services <https://docs.aws.amazon.com/whitepapers/latest/aws-fault-isolation-boundaries/global-services.html>`_

        If you omit this region field, cert-manager will use the region from
        AWS_REGION and AWS_DEFAULT_REGION environment variables, if they are set
        in the cert-manager controller Pod.

        The ``region`` field is not needed if you use `IAM Roles for Service Accounts (IRSA) <https://docs.aws.amazon.com/eks/latest/userguide/iam-roles-for-service-accounts.html>`_.
        Instead an AWS_REGION environment variable is added to the cert-manager controller Pod by:
        `Amazon EKS Pod Identity Webhook <https://github.com/aws/amazon-eks-pod-identity-webhook>`_.
        In this case this ``region`` field value is ignored.

        The ``region`` field is not needed if you use `EKS Pod Identities <https://docs.aws.amazon.com/eks/latest/userguide/pod-identities.html>`_.
        Instead an AWS_REGION environment variable is added to the cert-manager controller Pod by:
        `Amazon EKS Pod Identity Agent <https://github.com/aws/eks-pod-identity-agent>`_,
        In this case this ``region`` field value is ignored.

        :schema: ChallengeSpecSolverDns01Route53#region
        '''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def role(self) -> typing.Optional[builtins.str]:
        '''Role is a Role ARN which the Route53 provider will assume using either the explicit credentials AccessKeyID/SecretAccessKey or the inferred credentials from environment variables, shared credentials file or AWS Instance metadata.

        :schema: ChallengeSpecSolverDns01Route53#role
        '''
        result = self._values.get("role")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def secret_access_key_secret_ref(
        self,
    ) -> typing.Optional["ChallengeSpecSolverDns01Route53SecretAccessKeySecretRef"]:
        '''The SecretAccessKey is used for authentication.

        If neither the Access Key nor Key ID are set, we fall-back to using env
        vars, shared credentials file or AWS Instance metadata,
        see: https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/configuring-sdk.html#specifying-credentials

        :schema: ChallengeSpecSolverDns01Route53#secretAccessKeySecretRef
        '''
        result = self._values.get("secret_access_key_secret_ref")
        return typing.cast(typing.Optional["ChallengeSpecSolverDns01Route53SecretAccessKeySecretRef"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ChallengeSpecSolverDns01Route53(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iocert-manageracme.ChallengeSpecSolverDns01Route53AccessKeyIdSecretRef",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "key": "key"},
)
class ChallengeSpecSolverDns01Route53AccessKeyIdSecretRef:
    def __init__(
        self,
        *,
        name: builtins.str,
        key: typing.Optional[builtins.str] = None,
    ) -> None:
        '''The SecretAccessKey is used for authentication.

        If set, pull the AWS
        access key ID from a key within a Kubernetes Secret.
        Cannot be set when AccessKeyID is set.
        If neither the Access Key nor Key ID are set, we fall-back to using env
        vars, shared credentials file or AWS Instance metadata,
        see: https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/configuring-sdk.html#specifying-credentials

        :param name: Name of the resource being referred to. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names
        :param key: The key of the entry in the Secret resource's ``data`` field to be used. Some instances of this field may be defaulted, in others it may be required.

        :schema: ChallengeSpecSolverDns01Route53AccessKeyIdSecretRef
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9b8062c5dc050e665f953dfc20f85c0b0c3ea44178dc696d17442d86f39cfa60)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
        if key is not None:
            self._values["key"] = key

    @builtins.property
    def name(self) -> builtins.str:
        '''Name of the resource being referred to.

        More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names

        :schema: ChallengeSpecSolverDns01Route53AccessKeyIdSecretRef#name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''The key of the entry in the Secret resource's ``data`` field to be used.

        Some instances of this field may be defaulted, in others it may be
        required.

        :schema: ChallengeSpecSolverDns01Route53AccessKeyIdSecretRef#key
        '''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ChallengeSpecSolverDns01Route53AccessKeyIdSecretRef(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iocert-manageracme.ChallengeSpecSolverDns01Route53Auth",
    jsii_struct_bases=[],
    name_mapping={"kubernetes": "kubernetes"},
)
class ChallengeSpecSolverDns01Route53Auth:
    def __init__(
        self,
        *,
        kubernetes: typing.Union["ChallengeSpecSolverDns01Route53AuthKubernetes", typing.Dict[builtins.str, typing.Any]],
    ) -> None:
        '''Auth configures how cert-manager authenticates.

        :param kubernetes: Kubernetes authenticates with Route53 using AssumeRoleWithWebIdentity by passing a bound ServiceAccount token.

        :schema: ChallengeSpecSolverDns01Route53Auth
        '''
        if isinstance(kubernetes, dict):
            kubernetes = ChallengeSpecSolverDns01Route53AuthKubernetes(**kubernetes)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6d8142270d4ff247e957ac2eccae2a3bbb9c605f7402c5037b65872d3cba552c)
            check_type(argname="argument kubernetes", value=kubernetes, expected_type=type_hints["kubernetes"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "kubernetes": kubernetes,
        }

    @builtins.property
    def kubernetes(self) -> "ChallengeSpecSolverDns01Route53AuthKubernetes":
        '''Kubernetes authenticates with Route53 using AssumeRoleWithWebIdentity by passing a bound ServiceAccount token.

        :schema: ChallengeSpecSolverDns01Route53Auth#kubernetes
        '''
        result = self._values.get("kubernetes")
        assert result is not None, "Required property 'kubernetes' is missing"
        return typing.cast("ChallengeSpecSolverDns01Route53AuthKubernetes", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ChallengeSpecSolverDns01Route53Auth(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iocert-manageracme.ChallengeSpecSolverDns01Route53AuthKubernetes",
    jsii_struct_bases=[],
    name_mapping={"service_account_ref": "serviceAccountRef"},
)
class ChallengeSpecSolverDns01Route53AuthKubernetes:
    def __init__(
        self,
        *,
        service_account_ref: typing.Union["ChallengeSpecSolverDns01Route53AuthKubernetesServiceAccountRef", typing.Dict[builtins.str, typing.Any]],
    ) -> None:
        '''Kubernetes authenticates with Route53 using AssumeRoleWithWebIdentity by passing a bound ServiceAccount token.

        :param service_account_ref: A reference to a service account that will be used to request a bound token (also known as "projected token"). To use this field, you must configure an RBAC rule to let cert-manager request a token.

        :schema: ChallengeSpecSolverDns01Route53AuthKubernetes
        '''
        if isinstance(service_account_ref, dict):
            service_account_ref = ChallengeSpecSolverDns01Route53AuthKubernetesServiceAccountRef(**service_account_ref)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e950406ddb9dde980e95eec152441496b970ad499cff6fb3b151822b5eaf010b)
            check_type(argname="argument service_account_ref", value=service_account_ref, expected_type=type_hints["service_account_ref"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "service_account_ref": service_account_ref,
        }

    @builtins.property
    def service_account_ref(
        self,
    ) -> "ChallengeSpecSolverDns01Route53AuthKubernetesServiceAccountRef":
        '''A reference to a service account that will be used to request a bound token (also known as "projected token").

        To use this field, you must
        configure an RBAC rule to let cert-manager request a token.

        :schema: ChallengeSpecSolverDns01Route53AuthKubernetes#serviceAccountRef
        '''
        result = self._values.get("service_account_ref")
        assert result is not None, "Required property 'service_account_ref' is missing"
        return typing.cast("ChallengeSpecSolverDns01Route53AuthKubernetesServiceAccountRef", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ChallengeSpecSolverDns01Route53AuthKubernetes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iocert-manageracme.ChallengeSpecSolverDns01Route53AuthKubernetesServiceAccountRef",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "audiences": "audiences"},
)
class ChallengeSpecSolverDns01Route53AuthKubernetesServiceAccountRef:
    def __init__(
        self,
        *,
        name: builtins.str,
        audiences: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''A reference to a service account that will be used to request a bound token (also known as "projected token").

        To use this field, you must
        configure an RBAC rule to let cert-manager request a token.

        :param name: Name of the ServiceAccount used to request a token.
        :param audiences: TokenAudiences is an optional list of audiences to include in the token passed to AWS. The default token consisting of the issuer's namespace and name is always included. If unset the audience defaults to ``sts.amazonaws.com``.

        :schema: ChallengeSpecSolverDns01Route53AuthKubernetesServiceAccountRef
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5366db8305705ed9e7c4fc89f220afa5ebdfd36b335bd6df7449a72c5fcfcd48)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument audiences", value=audiences, expected_type=type_hints["audiences"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
        if audiences is not None:
            self._values["audiences"] = audiences

    @builtins.property
    def name(self) -> builtins.str:
        '''Name of the ServiceAccount used to request a token.

        :schema: ChallengeSpecSolverDns01Route53AuthKubernetesServiceAccountRef#name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def audiences(self) -> typing.Optional[typing.List[builtins.str]]:
        '''TokenAudiences is an optional list of audiences to include in the token passed to AWS.

        The default token consisting of the issuer's namespace
        and name is always included.
        If unset the audience defaults to ``sts.amazonaws.com``.

        :schema: ChallengeSpecSolverDns01Route53AuthKubernetesServiceAccountRef#audiences
        '''
        result = self._values.get("audiences")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ChallengeSpecSolverDns01Route53AuthKubernetesServiceAccountRef(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iocert-manageracme.ChallengeSpecSolverDns01Route53SecretAccessKeySecretRef",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "key": "key"},
)
class ChallengeSpecSolverDns01Route53SecretAccessKeySecretRef:
    def __init__(
        self,
        *,
        name: builtins.str,
        key: typing.Optional[builtins.str] = None,
    ) -> None:
        '''The SecretAccessKey is used for authentication.

        If neither the Access Key nor Key ID are set, we fall-back to using env
        vars, shared credentials file or AWS Instance metadata,
        see: https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/configuring-sdk.html#specifying-credentials

        :param name: Name of the resource being referred to. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names
        :param key: The key of the entry in the Secret resource's ``data`` field to be used. Some instances of this field may be defaulted, in others it may be required.

        :schema: ChallengeSpecSolverDns01Route53SecretAccessKeySecretRef
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6b260ed8f11172bdeb2d478d0f0917d5a3b8237600d2c4f3c3235bf505ec0dff)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
        if key is not None:
            self._values["key"] = key

    @builtins.property
    def name(self) -> builtins.str:
        '''Name of the resource being referred to.

        More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names

        :schema: ChallengeSpecSolverDns01Route53SecretAccessKeySecretRef#name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''The key of the entry in the Secret resource's ``data`` field to be used.

        Some instances of this field may be defaulted, in others it may be
        required.

        :schema: ChallengeSpecSolverDns01Route53SecretAccessKeySecretRef#key
        '''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ChallengeSpecSolverDns01Route53SecretAccessKeySecretRef(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iocert-manageracme.ChallengeSpecSolverDns01Webhook",
    jsii_struct_bases=[],
    name_mapping={
        "group_name": "groupName",
        "solver_name": "solverName",
        "config": "config",
    },
)
class ChallengeSpecSolverDns01Webhook:
    def __init__(
        self,
        *,
        group_name: builtins.str,
        solver_name: builtins.str,
        config: typing.Any = None,
    ) -> None:
        '''Configure an external webhook based DNS01 challenge solver to manage DNS01 challenge records.

        :param group_name: The API group name that should be used when POSTing ChallengePayload resources to the webhook apiserver. This should be the same as the GroupName specified in the webhook provider implementation.
        :param solver_name: The name of the solver to use, as defined in the webhook provider implementation. This will typically be the name of the provider, e.g. 'cloudflare'.
        :param config: Additional configuration that should be passed to the webhook apiserver when challenges are processed. This can contain arbitrary JSON data. Secret values should not be specified in this stanza. If secret values are needed (e.g. credentials for a DNS service), you should use a SecretKeySelector to reference a Secret resource. For details on the schema of this field, consult the webhook provider implementation's documentation.

        :schema: ChallengeSpecSolverDns01Webhook
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__37000b3447a23ae5e8b634d74fa2ffae23402a83f8a90df74b5e1b307303006f)
            check_type(argname="argument group_name", value=group_name, expected_type=type_hints["group_name"])
            check_type(argname="argument solver_name", value=solver_name, expected_type=type_hints["solver_name"])
            check_type(argname="argument config", value=config, expected_type=type_hints["config"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "group_name": group_name,
            "solver_name": solver_name,
        }
        if config is not None:
            self._values["config"] = config

    @builtins.property
    def group_name(self) -> builtins.str:
        '''The API group name that should be used when POSTing ChallengePayload resources to the webhook apiserver.

        This should be the same as the GroupName specified in the webhook
        provider implementation.

        :schema: ChallengeSpecSolverDns01Webhook#groupName
        '''
        result = self._values.get("group_name")
        assert result is not None, "Required property 'group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def solver_name(self) -> builtins.str:
        '''The name of the solver to use, as defined in the webhook provider implementation.

        This will typically be the name of the provider, e.g. 'cloudflare'.

        :schema: ChallengeSpecSolverDns01Webhook#solverName
        '''
        result = self._values.get("solver_name")
        assert result is not None, "Required property 'solver_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def config(self) -> typing.Any:
        '''Additional configuration that should be passed to the webhook apiserver when challenges are processed.

        This can contain arbitrary JSON data.
        Secret values should not be specified in this stanza.
        If secret values are needed (e.g. credentials for a DNS service), you
        should use a SecretKeySelector to reference a Secret resource.
        For details on the schema of this field, consult the webhook provider
        implementation's documentation.

        :schema: ChallengeSpecSolverDns01Webhook#config
        '''
        result = self._values.get("config")
        return typing.cast(typing.Any, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ChallengeSpecSolverDns01Webhook(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iocert-manageracme.ChallengeSpecSolverHttp01",
    jsii_struct_bases=[],
    name_mapping={"gateway_http_route": "gatewayHttpRoute", "ingress": "ingress"},
)
class ChallengeSpecSolverHttp01:
    def __init__(
        self,
        *,
        gateway_http_route: typing.Optional[typing.Union["ChallengeSpecSolverHttp01GatewayHttpRoute", typing.Dict[builtins.str, typing.Any]]] = None,
        ingress: typing.Optional[typing.Union["ChallengeSpecSolverHttp01Ingress", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''Configures cert-manager to attempt to complete authorizations by performing the HTTP01 challenge flow.

        It is not possible to obtain certificates for wildcard domain names
        (e.g. ``*.example.com``) using the HTTP01 challenge mechanism.

        :param gateway_http_route: The Gateway API is a sig-network community API that models service networking in Kubernetes (https://gateway-api.sigs.k8s.io/). The Gateway solver will create HTTPRoutes with the specified labels in the same namespace as the challenge. This solver is experimental, and fields / behaviour may change in the future.
        :param ingress: The ingress based HTTP01 challenge solver will solve challenges by creating or modifying Ingress resources in order to route requests for '/.well-known/acme-challenge/XYZ' to 'challenge solver' pods that are provisioned by cert-manager for each Challenge to be completed.

        :schema: ChallengeSpecSolverHttp01
        '''
        if isinstance(gateway_http_route, dict):
            gateway_http_route = ChallengeSpecSolverHttp01GatewayHttpRoute(**gateway_http_route)
        if isinstance(ingress, dict):
            ingress = ChallengeSpecSolverHttp01Ingress(**ingress)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7e9169fc4dabcd2e9e67f308a34cada555025d0f8cf0bafdec1f75a9f59f27f8)
            check_type(argname="argument gateway_http_route", value=gateway_http_route, expected_type=type_hints["gateway_http_route"])
            check_type(argname="argument ingress", value=ingress, expected_type=type_hints["ingress"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if gateway_http_route is not None:
            self._values["gateway_http_route"] = gateway_http_route
        if ingress is not None:
            self._values["ingress"] = ingress

    @builtins.property
    def gateway_http_route(
        self,
    ) -> typing.Optional["ChallengeSpecSolverHttp01GatewayHttpRoute"]:
        '''The Gateway API is a sig-network community API that models service networking in Kubernetes (https://gateway-api.sigs.k8s.io/). The Gateway solver will create HTTPRoutes with the specified labels in the same namespace as the challenge. This solver is experimental, and fields / behaviour may change in the future.

        :schema: ChallengeSpecSolverHttp01#gatewayHTTPRoute
        '''
        result = self._values.get("gateway_http_route")
        return typing.cast(typing.Optional["ChallengeSpecSolverHttp01GatewayHttpRoute"], result)

    @builtins.property
    def ingress(self) -> typing.Optional["ChallengeSpecSolverHttp01Ingress"]:
        '''The ingress based HTTP01 challenge solver will solve challenges by creating or modifying Ingress resources in order to route requests for '/.well-known/acme-challenge/XYZ' to 'challenge solver' pods that are provisioned by cert-manager for each Challenge to be completed.

        :schema: ChallengeSpecSolverHttp01#ingress
        '''
        result = self._values.get("ingress")
        return typing.cast(typing.Optional["ChallengeSpecSolverHttp01Ingress"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ChallengeSpecSolverHttp01(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iocert-manageracme.ChallengeSpecSolverHttp01GatewayHttpRoute",
    jsii_struct_bases=[],
    name_mapping={
        "labels": "labels",
        "parent_refs": "parentRefs",
        "pod_template": "podTemplate",
        "service_type": "serviceType",
    },
)
class ChallengeSpecSolverHttp01GatewayHttpRoute:
    def __init__(
        self,
        *,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        parent_refs: typing.Optional[typing.Sequence[typing.Union["ChallengeSpecSolverHttp01GatewayHttpRouteParentRefs", typing.Dict[builtins.str, typing.Any]]]] = None,
        pod_template: typing.Optional[typing.Union["ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplate", typing.Dict[builtins.str, typing.Any]]] = None,
        service_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''The Gateway API is a sig-network community API that models service networking in Kubernetes (https://gateway-api.sigs.k8s.io/). The Gateway solver will create HTTPRoutes with the specified labels in the same namespace as the challenge. This solver is experimental, and fields / behaviour may change in the future.

        :param labels: Custom labels that will be applied to HTTPRoutes created by cert-manager while solving HTTP-01 challenges.
        :param parent_refs: When solving an HTTP-01 challenge, cert-manager creates an HTTPRoute. cert-manager needs to know which parentRefs should be used when creating the HTTPRoute. Usually, the parentRef references a Gateway. See: https://gateway-api.sigs.k8s.io/api-types/httproute/#attaching-to-gateways
        :param pod_template: Optional pod template used to configure the ACME challenge solver pods used for HTTP01 challenges.
        :param service_type: Optional service type for Kubernetes solver service. Supported values are NodePort or ClusterIP. If unset, defaults to NodePort.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoute
        '''
        if isinstance(pod_template, dict):
            pod_template = ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplate(**pod_template)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__67eb71473fe7bcb8103baad885c5d62bd34367e424399142abb055efebfa2c1a)
            check_type(argname="argument labels", value=labels, expected_type=type_hints["labels"])
            check_type(argname="argument parent_refs", value=parent_refs, expected_type=type_hints["parent_refs"])
            check_type(argname="argument pod_template", value=pod_template, expected_type=type_hints["pod_template"])
            check_type(argname="argument service_type", value=service_type, expected_type=type_hints["service_type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if labels is not None:
            self._values["labels"] = labels
        if parent_refs is not None:
            self._values["parent_refs"] = parent_refs
        if pod_template is not None:
            self._values["pod_template"] = pod_template
        if service_type is not None:
            self._values["service_type"] = service_type

    @builtins.property
    def labels(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Custom labels that will be applied to HTTPRoutes created by cert-manager while solving HTTP-01 challenges.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoute#labels
        '''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def parent_refs(
        self,
    ) -> typing.Optional[typing.List["ChallengeSpecSolverHttp01GatewayHttpRouteParentRefs"]]:
        '''When solving an HTTP-01 challenge, cert-manager creates an HTTPRoute.

        cert-manager needs to know which parentRefs should be used when creating
        the HTTPRoute. Usually, the parentRef references a Gateway. See:
        https://gateway-api.sigs.k8s.io/api-types/httproute/#attaching-to-gateways

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoute#parentRefs
        '''
        result = self._values.get("parent_refs")
        return typing.cast(typing.Optional[typing.List["ChallengeSpecSolverHttp01GatewayHttpRouteParentRefs"]], result)

    @builtins.property
    def pod_template(
        self,
    ) -> typing.Optional["ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplate"]:
        '''Optional pod template used to configure the ACME challenge solver pods used for HTTP01 challenges.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoute#podTemplate
        '''
        result = self._values.get("pod_template")
        return typing.cast(typing.Optional["ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplate"], result)

    @builtins.property
    def service_type(self) -> typing.Optional[builtins.str]:
        '''Optional service type for Kubernetes solver service.

        Supported values
        are NodePort or ClusterIP. If unset, defaults to NodePort.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoute#serviceType
        '''
        result = self._values.get("service_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ChallengeSpecSolverHttp01GatewayHttpRoute(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iocert-manageracme.ChallengeSpecSolverHttp01GatewayHttpRouteParentRefs",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "group": "group",
        "kind": "kind",
        "namespace": "namespace",
        "port": "port",
        "section_name": "sectionName",
    },
)
class ChallengeSpecSolverHttp01GatewayHttpRouteParentRefs:
    def __init__(
        self,
        *,
        name: builtins.str,
        group: typing.Optional[builtins.str] = None,
        kind: typing.Optional[builtins.str] = None,
        namespace: typing.Optional[builtins.str] = None,
        port: typing.Optional[jsii.Number] = None,
        section_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''ParentReference identifies an API object (usually a Gateway) that can be considered a parent of this resource (usually a route).

        There are two kinds of parent resources
        with "Core" support:

        - Gateway (Gateway conformance profile)
        - Service (Mesh conformance profile, ClusterIP Services only)

        This API may be extended in the future to support additional kinds of parent
        resources.

        The API object must be valid in the cluster; the Group and Kind must
        be registered in the cluster for this reference to be valid.

        :param name: Name is the name of the referent. Support: Core
        :param group: Group is the group of the referent. When unspecified, "gateway.networking.k8s.io" is inferred. To set the core API group (such as for a "Service" kind referent), Group must be explicitly set to "" (empty string). Support: Core
        :param kind: Kind is kind of the referent. There are two kinds of parent resources with "Core" support: - Gateway (Gateway conformance profile) - Service (Mesh conformance profile, ClusterIP Services only) Support for other resources is Implementation-Specific.
        :param namespace: Namespace is the namespace of the referent. When unspecified, this refers to the local namespace of the Route. Note that there are specific rules for ParentRefs which cross namespace boundaries. Cross-namespace references are only valid if they are explicitly allowed by something in the namespace they are referring to. For example: Gateway has the AllowedRoutes field, and ReferenceGrant provides a generic way to enable any other kind of cross-namespace reference. `gateway:experimental:description <gateway:experimental:description>`_ ParentRefs from a Route to a Service in the same namespace are "producer" routes, which apply default routing rules to inbound connections from any namespace to the Service. ParentRefs from a Route to a Service in a different namespace are "consumer" routes, and these routing rules are only applied to outbound connections originating from the same namespace as the Route, for which the intended destination of the connections are a Service targeted as a ParentRef of the Route. </gateway:experimental:description> Support: Core
        :param port: Port is the network port this Route targets. It can be interpreted differently based on the type of parent resource. When the parent resource is a Gateway, this targets all listeners listening on the specified port that also support this kind of Route(and select this Route). It's not recommended to set ``Port`` unless the networking behaviors specified in a Route must apply to a specific port as opposed to a listener(s) whose port(s) may be changed. When both Port and SectionName are specified, the name and port of the selected listener must match both specified values. `gateway:experimental:description <gateway:experimental:description>`_ When the parent resource is a Service, this targets a specific port in the Service spec. When both Port (experimental) and SectionName are specified, the name and port of the selected port must match both specified values. </gateway:experimental:description> Implementations MAY choose to support other parent resources. Implementations supporting other types of parent resources MUST clearly document how/if Port is interpreted. For the purpose of status, an attachment is considered successful as long as the parent resource accepts it partially. For example, Gateway listeners can restrict which Routes can attach to them by Route kind, namespace, or hostname. If 1 of 2 Gateway listeners accept attachment from the referencing Route, the Route MUST be considered successfully attached. If no Gateway listeners accept attachment from this Route, the Route MUST be considered detached from the Gateway. Support: Extended
        :param section_name: SectionName is the name of a section within the target resource. In the following resources, SectionName is interpreted as the following: - Gateway: Listener name. When both Port (experimental) and SectionName are specified, the name and port of the selected listener must match both specified values. - Service: Port name. When both Port (experimental) and SectionName are specified, the name and port of the selected listener must match both specified values. Implementations MAY choose to support attaching Routes to other resources. If that is the case, they MUST clearly document how SectionName is interpreted. When unspecified (empty string), this will reference the entire resource. For the purpose of status, an attachment is considered successful if at least one section in the parent resource accepts it. For example, Gateway listeners can restrict which Routes can attach to them by Route kind, namespace, or hostname. If 1 of 2 Gateway listeners accept attachment from the referencing Route, the Route MUST be considered successfully attached. If no Gateway listeners accept attachment from this Route, the Route MUST be considered detached from the Gateway. Support: Core

        :schema: ChallengeSpecSolverHttp01GatewayHttpRouteParentRefs
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7e20cdceec1388053ef677a629fa0ab843e3f28ae32b3301382869b5d5c0c736)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument group", value=group, expected_type=type_hints["group"])
            check_type(argname="argument kind", value=kind, expected_type=type_hints["kind"])
            check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
            check_type(argname="argument section_name", value=section_name, expected_type=type_hints["section_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
        if group is not None:
            self._values["group"] = group
        if kind is not None:
            self._values["kind"] = kind
        if namespace is not None:
            self._values["namespace"] = namespace
        if port is not None:
            self._values["port"] = port
        if section_name is not None:
            self._values["section_name"] = section_name

    @builtins.property
    def name(self) -> builtins.str:
        '''Name is the name of the referent.

        Support: Core

        :schema: ChallengeSpecSolverHttp01GatewayHttpRouteParentRefs#name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def group(self) -> typing.Optional[builtins.str]:
        '''Group is the group of the referent.

        When unspecified, "gateway.networking.k8s.io" is inferred.
        To set the core API group (such as for a "Service" kind referent),
        Group must be explicitly set to "" (empty string).

        Support: Core

        :schema: ChallengeSpecSolverHttp01GatewayHttpRouteParentRefs#group
        '''
        result = self._values.get("group")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kind(self) -> typing.Optional[builtins.str]:
        '''Kind is kind of the referent.

        There are two kinds of parent resources with "Core" support:

        - Gateway (Gateway conformance profile)
        - Service (Mesh conformance profile, ClusterIP Services only)

        Support for other resources is Implementation-Specific.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRouteParentRefs#kind
        '''
        result = self._values.get("kind")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def namespace(self) -> typing.Optional[builtins.str]:
        '''Namespace is the namespace of the referent. When unspecified, this refers to the local namespace of the Route.

        Note that there are specific rules for ParentRefs which cross namespace
        boundaries. Cross-namespace references are only valid if they are explicitly
        allowed by something in the namespace they are referring to. For example:
        Gateway has the AllowedRoutes field, and ReferenceGrant provides a
        generic way to enable any other kind of cross-namespace reference.

        `gateway:experimental:description <gateway:experimental:description>`_
        ParentRefs from a Route to a Service in the same namespace are "producer"
        routes, which apply default routing rules to inbound connections from
        any namespace to the Service.

        ParentRefs from a Route to a Service in a different namespace are
        "consumer" routes, and these routing rules are only applied to outbound
        connections originating from the same namespace as the Route, for which
        the intended destination of the connections are a Service targeted as a
        ParentRef of the Route.
        </gateway:experimental:description>

        Support: Core

        :schema: ChallengeSpecSolverHttp01GatewayHttpRouteParentRefs#namespace
        '''
        result = self._values.get("namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def port(self) -> typing.Optional[jsii.Number]:
        '''Port is the network port this Route targets. It can be interpreted differently based on the type of parent resource.

        When the parent resource is a Gateway, this targets all listeners
        listening on the specified port that also support this kind of Route(and
        select this Route). It's not recommended to set ``Port`` unless the
        networking behaviors specified in a Route must apply to a specific port
        as opposed to a listener(s) whose port(s) may be changed. When both Port
        and SectionName are specified, the name and port of the selected listener
        must match both specified values.

        `gateway:experimental:description <gateway:experimental:description>`_
        When the parent resource is a Service, this targets a specific port in the
        Service spec. When both Port (experimental) and SectionName are specified,
        the name and port of the selected port must match both specified values.
        </gateway:experimental:description>

        Implementations MAY choose to support other parent resources.
        Implementations supporting other types of parent resources MUST clearly
        document how/if Port is interpreted.

        For the purpose of status, an attachment is considered successful as
        long as the parent resource accepts it partially. For example, Gateway
        listeners can restrict which Routes can attach to them by Route kind,
        namespace, or hostname. If 1 of 2 Gateway listeners accept attachment
        from the referencing Route, the Route MUST be considered successfully
        attached. If no Gateway listeners accept attachment from this Route,
        the Route MUST be considered detached from the Gateway.

        Support: Extended

        :schema: ChallengeSpecSolverHttp01GatewayHttpRouteParentRefs#port
        '''
        result = self._values.get("port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def section_name(self) -> typing.Optional[builtins.str]:
        '''SectionName is the name of a section within the target resource.

        In the
        following resources, SectionName is interpreted as the following:

        - Gateway: Listener name. When both Port (experimental) and SectionName
          are specified, the name and port of the selected listener must match
          both specified values.
        - Service: Port name. When both Port (experimental) and SectionName
          are specified, the name and port of the selected listener must match
          both specified values.

        Implementations MAY choose to support attaching Routes to other resources.
        If that is the case, they MUST clearly document how SectionName is
        interpreted.

        When unspecified (empty string), this will reference the entire resource.
        For the purpose of status, an attachment is considered successful if at
        least one section in the parent resource accepts it. For example, Gateway
        listeners can restrict which Routes can attach to them by Route kind,
        namespace, or hostname. If 1 of 2 Gateway listeners accept attachment from
        the referencing Route, the Route MUST be considered successfully
        attached. If no Gateway listeners accept attachment from this Route, the
        Route MUST be considered detached from the Gateway.

        Support: Core

        :schema: ChallengeSpecSolverHttp01GatewayHttpRouteParentRefs#sectionName
        '''
        result = self._values.get("section_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ChallengeSpecSolverHttp01GatewayHttpRouteParentRefs(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iocert-manageracme.ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplate",
    jsii_struct_bases=[],
    name_mapping={"metadata": "metadata", "spec": "spec"},
)
class ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplate:
    def __init__(
        self,
        *,
        metadata: typing.Optional[typing.Union["ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateMetadata", typing.Dict[builtins.str, typing.Any]]] = None,
        spec: typing.Optional[typing.Union["ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpec", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''Optional pod template used to configure the ACME challenge solver pods used for HTTP01 challenges.

        :param metadata: ObjectMeta overrides for the pod used to solve HTTP01 challenges. Only the 'labels' and 'annotations' fields may be set. If labels or annotations overlap with in-built values, the values here will override the in-built values.
        :param spec: PodSpec defines overrides for the HTTP01 challenge solver pod. Check ACMEChallengeSolverHTTP01IngressPodSpec to find out currently supported fields. All other fields will be ignored.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplate
        '''
        if isinstance(metadata, dict):
            metadata = ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateMetadata(**metadata)
        if isinstance(spec, dict):
            spec = ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpec(**spec)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2170caad41c1ea3d466134b6fa2dc16589aba28cc876249b884c7efcf2920731)
            check_type(argname="argument metadata", value=metadata, expected_type=type_hints["metadata"])
            check_type(argname="argument spec", value=spec, expected_type=type_hints["spec"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if metadata is not None:
            self._values["metadata"] = metadata
        if spec is not None:
            self._values["spec"] = spec

    @builtins.property
    def metadata(
        self,
    ) -> typing.Optional["ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateMetadata"]:
        '''ObjectMeta overrides for the pod used to solve HTTP01 challenges.

        Only the 'labels' and 'annotations' fields may be set.
        If labels or annotations overlap with in-built values, the values here
        will override the in-built values.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplate#metadata
        '''
        result = self._values.get("metadata")
        return typing.cast(typing.Optional["ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateMetadata"], result)

    @builtins.property
    def spec(
        self,
    ) -> typing.Optional["ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpec"]:
        '''PodSpec defines overrides for the HTTP01 challenge solver pod.

        Check ACMEChallengeSolverHTTP01IngressPodSpec to find out currently supported fields.
        All other fields will be ignored.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplate#spec
        '''
        result = self._values.get("spec")
        return typing.cast(typing.Optional["ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpec"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplate(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iocert-manageracme.ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateMetadata",
    jsii_struct_bases=[],
    name_mapping={"annotations": "annotations", "labels": "labels"},
)
class ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateMetadata:
    def __init__(
        self,
        *,
        annotations: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''ObjectMeta overrides for the pod used to solve HTTP01 challenges.

        Only the 'labels' and 'annotations' fields may be set.
        If labels or annotations overlap with in-built values, the values here
        will override the in-built values.

        :param annotations: Annotations that should be added to the created ACME HTTP01 solver pods.
        :param labels: Labels that should be added to the created ACME HTTP01 solver pods.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateMetadata
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4fa9766367c3825852fad4e60091ddeb21795ac5a36842381f9972cd35dedb46)
            check_type(argname="argument annotations", value=annotations, expected_type=type_hints["annotations"])
            check_type(argname="argument labels", value=labels, expected_type=type_hints["labels"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if annotations is not None:
            self._values["annotations"] = annotations
        if labels is not None:
            self._values["labels"] = labels

    @builtins.property
    def annotations(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Annotations that should be added to the created ACME HTTP01 solver pods.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateMetadata#annotations
        '''
        result = self._values.get("annotations")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def labels(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Labels that should be added to the created ACME HTTP01 solver pods.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateMetadata#labels
        '''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateMetadata(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iocert-manageracme.ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpec",
    jsii_struct_bases=[],
    name_mapping={
        "affinity": "affinity",
        "image_pull_secrets": "imagePullSecrets",
        "node_selector": "nodeSelector",
        "priority_class_name": "priorityClassName",
        "security_context": "securityContext",
        "service_account_name": "serviceAccountName",
        "tolerations": "tolerations",
    },
)
class ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpec:
    def __init__(
        self,
        *,
        affinity: typing.Optional[typing.Union["ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinity", typing.Dict[builtins.str, typing.Any]]] = None,
        image_pull_secrets: typing.Optional[typing.Sequence[typing.Union["ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecImagePullSecrets", typing.Dict[builtins.str, typing.Any]]]] = None,
        node_selector: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        priority_class_name: typing.Optional[builtins.str] = None,
        security_context: typing.Optional[typing.Union["ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecSecurityContext", typing.Dict[builtins.str, typing.Any]]] = None,
        service_account_name: typing.Optional[builtins.str] = None,
        tolerations: typing.Optional[typing.Sequence[typing.Union["ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecTolerations", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''PodSpec defines overrides for the HTTP01 challenge solver pod.

        Check ACMEChallengeSolverHTTP01IngressPodSpec to find out currently supported fields.
        All other fields will be ignored.

        :param affinity: If specified, the pod's scheduling constraints.
        :param image_pull_secrets: If specified, the pod's imagePullSecrets.
        :param node_selector: NodeSelector is a selector which must be true for the pod to fit on a node. Selector which must match a node's labels for the pod to be scheduled on that node. More info: https://kubernetes.io/docs/concepts/configuration/assign-pod-node/
        :param priority_class_name: If specified, the pod's priorityClassName.
        :param security_context: If specified, the pod's security context.
        :param service_account_name: If specified, the pod's service account.
        :param tolerations: If specified, the pod's tolerations.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpec
        '''
        if isinstance(affinity, dict):
            affinity = ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinity(**affinity)
        if isinstance(security_context, dict):
            security_context = ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecSecurityContext(**security_context)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a8bcf60fa559acd074963cffaa8da5d4b55540e82d07fb32fd0309d430ef6de9)
            check_type(argname="argument affinity", value=affinity, expected_type=type_hints["affinity"])
            check_type(argname="argument image_pull_secrets", value=image_pull_secrets, expected_type=type_hints["image_pull_secrets"])
            check_type(argname="argument node_selector", value=node_selector, expected_type=type_hints["node_selector"])
            check_type(argname="argument priority_class_name", value=priority_class_name, expected_type=type_hints["priority_class_name"])
            check_type(argname="argument security_context", value=security_context, expected_type=type_hints["security_context"])
            check_type(argname="argument service_account_name", value=service_account_name, expected_type=type_hints["service_account_name"])
            check_type(argname="argument tolerations", value=tolerations, expected_type=type_hints["tolerations"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if affinity is not None:
            self._values["affinity"] = affinity
        if image_pull_secrets is not None:
            self._values["image_pull_secrets"] = image_pull_secrets
        if node_selector is not None:
            self._values["node_selector"] = node_selector
        if priority_class_name is not None:
            self._values["priority_class_name"] = priority_class_name
        if security_context is not None:
            self._values["security_context"] = security_context
        if service_account_name is not None:
            self._values["service_account_name"] = service_account_name
        if tolerations is not None:
            self._values["tolerations"] = tolerations

    @builtins.property
    def affinity(
        self,
    ) -> typing.Optional["ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinity"]:
        '''If specified, the pod's scheduling constraints.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpec#affinity
        '''
        result = self._values.get("affinity")
        return typing.cast(typing.Optional["ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinity"], result)

    @builtins.property
    def image_pull_secrets(
        self,
    ) -> typing.Optional[typing.List["ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecImagePullSecrets"]]:
        '''If specified, the pod's imagePullSecrets.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpec#imagePullSecrets
        '''
        result = self._values.get("image_pull_secrets")
        return typing.cast(typing.Optional[typing.List["ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecImagePullSecrets"]], result)

    @builtins.property
    def node_selector(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''NodeSelector is a selector which must be true for the pod to fit on a node.

        Selector which must match a node's labels for the pod to be scheduled on that node.
        More info: https://kubernetes.io/docs/concepts/configuration/assign-pod-node/

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpec#nodeSelector
        '''
        result = self._values.get("node_selector")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def priority_class_name(self) -> typing.Optional[builtins.str]:
        '''If specified, the pod's priorityClassName.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpec#priorityClassName
        '''
        result = self._values.get("priority_class_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def security_context(
        self,
    ) -> typing.Optional["ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecSecurityContext"]:
        '''If specified, the pod's security context.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpec#securityContext
        '''
        result = self._values.get("security_context")
        return typing.cast(typing.Optional["ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecSecurityContext"], result)

    @builtins.property
    def service_account_name(self) -> typing.Optional[builtins.str]:
        '''If specified, the pod's service account.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpec#serviceAccountName
        '''
        result = self._values.get("service_account_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tolerations(
        self,
    ) -> typing.Optional[typing.List["ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecTolerations"]]:
        '''If specified, the pod's tolerations.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpec#tolerations
        '''
        result = self._values.get("tolerations")
        return typing.cast(typing.Optional[typing.List["ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecTolerations"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpec(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iocert-manageracme.ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinity",
    jsii_struct_bases=[],
    name_mapping={
        "node_affinity": "nodeAffinity",
        "pod_affinity": "podAffinity",
        "pod_anti_affinity": "podAntiAffinity",
    },
)
class ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinity:
    def __init__(
        self,
        *,
        node_affinity: typing.Optional[typing.Union["ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityNodeAffinity", typing.Dict[builtins.str, typing.Any]]] = None,
        pod_affinity: typing.Optional[typing.Union["ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAffinity", typing.Dict[builtins.str, typing.Any]]] = None,
        pod_anti_affinity: typing.Optional[typing.Union["ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAntiAffinity", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''If specified, the pod's scheduling constraints.

        :param node_affinity: Describes node affinity scheduling rules for the pod.
        :param pod_affinity: Describes pod affinity scheduling rules (e.g. co-locate this pod in the same node, zone, etc. as some other pod(s)).
        :param pod_anti_affinity: Describes pod anti-affinity scheduling rules (e.g. avoid putting this pod in the same node, zone, etc. as some other pod(s)).

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinity
        '''
        if isinstance(node_affinity, dict):
            node_affinity = ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityNodeAffinity(**node_affinity)
        if isinstance(pod_affinity, dict):
            pod_affinity = ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAffinity(**pod_affinity)
        if isinstance(pod_anti_affinity, dict):
            pod_anti_affinity = ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAntiAffinity(**pod_anti_affinity)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__29e71ab8ec2bc758e9486a82bbe9f80bde371959649b92fea23cd9cb8c401ef5)
            check_type(argname="argument node_affinity", value=node_affinity, expected_type=type_hints["node_affinity"])
            check_type(argname="argument pod_affinity", value=pod_affinity, expected_type=type_hints["pod_affinity"])
            check_type(argname="argument pod_anti_affinity", value=pod_anti_affinity, expected_type=type_hints["pod_anti_affinity"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if node_affinity is not None:
            self._values["node_affinity"] = node_affinity
        if pod_affinity is not None:
            self._values["pod_affinity"] = pod_affinity
        if pod_anti_affinity is not None:
            self._values["pod_anti_affinity"] = pod_anti_affinity

    @builtins.property
    def node_affinity(
        self,
    ) -> typing.Optional["ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityNodeAffinity"]:
        '''Describes node affinity scheduling rules for the pod.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinity#nodeAffinity
        '''
        result = self._values.get("node_affinity")
        return typing.cast(typing.Optional["ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityNodeAffinity"], result)

    @builtins.property
    def pod_affinity(
        self,
    ) -> typing.Optional["ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAffinity"]:
        '''Describes pod affinity scheduling rules (e.g. co-locate this pod in the same node, zone, etc. as some other pod(s)).

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinity#podAffinity
        '''
        result = self._values.get("pod_affinity")
        return typing.cast(typing.Optional["ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAffinity"], result)

    @builtins.property
    def pod_anti_affinity(
        self,
    ) -> typing.Optional["ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAntiAffinity"]:
        '''Describes pod anti-affinity scheduling rules (e.g. avoid putting this pod in the same node, zone, etc. as some other pod(s)).

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinity#podAntiAffinity
        '''
        result = self._values.get("pod_anti_affinity")
        return typing.cast(typing.Optional["ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAntiAffinity"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinity(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iocert-manageracme.ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityNodeAffinity",
    jsii_struct_bases=[],
    name_mapping={
        "preferred_during_scheduling_ignored_during_execution": "preferredDuringSchedulingIgnoredDuringExecution",
        "required_during_scheduling_ignored_during_execution": "requiredDuringSchedulingIgnoredDuringExecution",
    },
)
class ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityNodeAffinity:
    def __init__(
        self,
        *,
        preferred_during_scheduling_ignored_during_execution: typing.Optional[typing.Sequence[typing.Union["ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecution", typing.Dict[builtins.str, typing.Any]]]] = None,
        required_during_scheduling_ignored_during_execution: typing.Optional[typing.Union["ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecution", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''Describes node affinity scheduling rules for the pod.

        :param preferred_during_scheduling_ignored_during_execution: The scheduler will prefer to schedule pods to nodes that satisfy the affinity expressions specified by this field, but it may choose a node that violates one or more of the expressions. The node that is most preferred is the one with the greatest sum of weights, i.e. for each node that meets all of the scheduling requirements (resource request, requiredDuringScheduling affinity expressions, etc.), compute a sum by iterating through the elements of this field and adding "weight" to the sum if the node matches the corresponding matchExpressions; the node(s) with the highest sum are the most preferred.
        :param required_during_scheduling_ignored_during_execution: If the affinity requirements specified by this field are not met at scheduling time, the pod will not be scheduled onto the node. If the affinity requirements specified by this field cease to be met at some point during pod execution (e.g. due to an update), the system may or may not try to eventually evict the pod from its node.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityNodeAffinity
        '''
        if isinstance(required_during_scheduling_ignored_during_execution, dict):
            required_during_scheduling_ignored_during_execution = ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecution(**required_during_scheduling_ignored_during_execution)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__795d8af6cb5c20c20fc3bb10d70ecc9bfcf91506cda07402c9e9ed95e3646004)
            check_type(argname="argument preferred_during_scheduling_ignored_during_execution", value=preferred_during_scheduling_ignored_during_execution, expected_type=type_hints["preferred_during_scheduling_ignored_during_execution"])
            check_type(argname="argument required_during_scheduling_ignored_during_execution", value=required_during_scheduling_ignored_during_execution, expected_type=type_hints["required_during_scheduling_ignored_during_execution"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if preferred_during_scheduling_ignored_during_execution is not None:
            self._values["preferred_during_scheduling_ignored_during_execution"] = preferred_during_scheduling_ignored_during_execution
        if required_during_scheduling_ignored_during_execution is not None:
            self._values["required_during_scheduling_ignored_during_execution"] = required_during_scheduling_ignored_during_execution

    @builtins.property
    def preferred_during_scheduling_ignored_during_execution(
        self,
    ) -> typing.Optional[typing.List["ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecution"]]:
        '''The scheduler will prefer to schedule pods to nodes that satisfy the affinity expressions specified by this field, but it may choose a node that violates one or more of the expressions.

        The node that is
        most preferred is the one with the greatest sum of weights, i.e.
        for each node that meets all of the scheduling requirements (resource
        request, requiredDuringScheduling affinity expressions, etc.),
        compute a sum by iterating through the elements of this field and adding
        "weight" to the sum if the node matches the corresponding matchExpressions; the
        node(s) with the highest sum are the most preferred.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityNodeAffinity#preferredDuringSchedulingIgnoredDuringExecution
        '''
        result = self._values.get("preferred_during_scheduling_ignored_during_execution")
        return typing.cast(typing.Optional[typing.List["ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecution"]], result)

    @builtins.property
    def required_during_scheduling_ignored_during_execution(
        self,
    ) -> typing.Optional["ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecution"]:
        '''If the affinity requirements specified by this field are not met at scheduling time, the pod will not be scheduled onto the node.

        If the affinity requirements specified by this field cease to be met
        at some point during pod execution (e.g. due to an update), the system
        may or may not try to eventually evict the pod from its node.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityNodeAffinity#requiredDuringSchedulingIgnoredDuringExecution
        '''
        result = self._values.get("required_during_scheduling_ignored_during_execution")
        return typing.cast(typing.Optional["ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecution"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityNodeAffinity(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iocert-manageracme.ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecution",
    jsii_struct_bases=[],
    name_mapping={"preference": "preference", "weight": "weight"},
)
class ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecution:
    def __init__(
        self,
        *,
        preference: typing.Union["ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecutionPreference", typing.Dict[builtins.str, typing.Any]],
        weight: jsii.Number,
    ) -> None:
        '''An empty preferred scheduling term matches all objects with implicit weight 0 (i.e. it's a no-op). A null preferred scheduling term matches no objects (i.e. is also a no-op).

        :param preference: A node selector term, associated with the corresponding weight.
        :param weight: Weight associated with matching the corresponding nodeSelectorTerm, in the range 1-100.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecution
        '''
        if isinstance(preference, dict):
            preference = ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecutionPreference(**preference)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2cc393d624fc77e432aea3f0093aa885bceed517b6e5d8be1383ef207a2db1b0)
            check_type(argname="argument preference", value=preference, expected_type=type_hints["preference"])
            check_type(argname="argument weight", value=weight, expected_type=type_hints["weight"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "preference": preference,
            "weight": weight,
        }

    @builtins.property
    def preference(
        self,
    ) -> "ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecutionPreference":
        '''A node selector term, associated with the corresponding weight.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecution#preference
        '''
        result = self._values.get("preference")
        assert result is not None, "Required property 'preference' is missing"
        return typing.cast("ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecutionPreference", result)

    @builtins.property
    def weight(self) -> jsii.Number:
        '''Weight associated with matching the corresponding nodeSelectorTerm, in the range 1-100.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecution#weight
        '''
        result = self._values.get("weight")
        assert result is not None, "Required property 'weight' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecution(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iocert-manageracme.ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecutionPreference",
    jsii_struct_bases=[],
    name_mapping={
        "match_expressions": "matchExpressions",
        "match_fields": "matchFields",
    },
)
class ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecutionPreference:
    def __init__(
        self,
        *,
        match_expressions: typing.Optional[typing.Sequence[typing.Union["ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecutionPreferenceMatchExpressions", typing.Dict[builtins.str, typing.Any]]]] = None,
        match_fields: typing.Optional[typing.Sequence[typing.Union["ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecutionPreferenceMatchFields", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''A node selector term, associated with the corresponding weight.

        :param match_expressions: A list of node selector requirements by node's labels.
        :param match_fields: A list of node selector requirements by node's fields.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecutionPreference
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__62b588fd6a3409b2b40309210b10f24c524e5df01d16cd5b026b93d7572c7096)
            check_type(argname="argument match_expressions", value=match_expressions, expected_type=type_hints["match_expressions"])
            check_type(argname="argument match_fields", value=match_fields, expected_type=type_hints["match_fields"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if match_expressions is not None:
            self._values["match_expressions"] = match_expressions
        if match_fields is not None:
            self._values["match_fields"] = match_fields

    @builtins.property
    def match_expressions(
        self,
    ) -> typing.Optional[typing.List["ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecutionPreferenceMatchExpressions"]]:
        '''A list of node selector requirements by node's labels.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecutionPreference#matchExpressions
        '''
        result = self._values.get("match_expressions")
        return typing.cast(typing.Optional[typing.List["ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecutionPreferenceMatchExpressions"]], result)

    @builtins.property
    def match_fields(
        self,
    ) -> typing.Optional[typing.List["ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecutionPreferenceMatchFields"]]:
        '''A list of node selector requirements by node's fields.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecutionPreference#matchFields
        '''
        result = self._values.get("match_fields")
        return typing.cast(typing.Optional[typing.List["ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecutionPreferenceMatchFields"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecutionPreference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iocert-manageracme.ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecutionPreferenceMatchExpressions",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "operator": "operator", "values": "values"},
)
class ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecutionPreferenceMatchExpressions:
    def __init__(
        self,
        *,
        key: builtins.str,
        operator: builtins.str,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''A node selector requirement is a selector that contains values, a key, and an operator that relates the key and values.

        :param key: The label key that the selector applies to.
        :param operator: Represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists, DoesNotExist. Gt, and Lt.
        :param values: An array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. If the operator is Gt or Lt, the values array must have a single element, which will be interpreted as an integer. This array is replaced during a strategic merge patch.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecutionPreferenceMatchExpressions
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0098e3bbe9cc056fef987159f88e9563f7b5714b1588e94195c33f0a6e5a1f4a)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "key": key,
            "operator": operator,
        }
        if values is not None:
            self._values["values"] = values

    @builtins.property
    def key(self) -> builtins.str:
        '''The label key that the selector applies to.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecutionPreferenceMatchExpressions#key
        '''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def operator(self) -> builtins.str:
        '''Represents a key's relationship to a set of values.

        Valid operators are In, NotIn, Exists, DoesNotExist. Gt, and Lt.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecutionPreferenceMatchExpressions#operator
        '''
        result = self._values.get("operator")
        assert result is not None, "Required property 'operator' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''An array of string values.

        If the operator is In or NotIn,
        the values array must be non-empty. If the operator is Exists or DoesNotExist,
        the values array must be empty. If the operator is Gt or Lt, the values
        array must have a single element, which will be interpreted as an integer.
        This array is replaced during a strategic merge patch.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecutionPreferenceMatchExpressions#values
        '''
        result = self._values.get("values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecutionPreferenceMatchExpressions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iocert-manageracme.ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecutionPreferenceMatchFields",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "operator": "operator", "values": "values"},
)
class ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecutionPreferenceMatchFields:
    def __init__(
        self,
        *,
        key: builtins.str,
        operator: builtins.str,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''A node selector requirement is a selector that contains values, a key, and an operator that relates the key and values.

        :param key: The label key that the selector applies to.
        :param operator: Represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists, DoesNotExist. Gt, and Lt.
        :param values: An array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. If the operator is Gt or Lt, the values array must have a single element, which will be interpreted as an integer. This array is replaced during a strategic merge patch.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecutionPreferenceMatchFields
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__646d9b5516e80c7bb7753ac9a9e54a545cb137aa7a2f6a4da01739e77a3f8c17)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "key": key,
            "operator": operator,
        }
        if values is not None:
            self._values["values"] = values

    @builtins.property
    def key(self) -> builtins.str:
        '''The label key that the selector applies to.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecutionPreferenceMatchFields#key
        '''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def operator(self) -> builtins.str:
        '''Represents a key's relationship to a set of values.

        Valid operators are In, NotIn, Exists, DoesNotExist. Gt, and Lt.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecutionPreferenceMatchFields#operator
        '''
        result = self._values.get("operator")
        assert result is not None, "Required property 'operator' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''An array of string values.

        If the operator is In or NotIn,
        the values array must be non-empty. If the operator is Exists or DoesNotExist,
        the values array must be empty. If the operator is Gt or Lt, the values
        array must have a single element, which will be interpreted as an integer.
        This array is replaced during a strategic merge patch.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecutionPreferenceMatchFields#values
        '''
        result = self._values.get("values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecutionPreferenceMatchFields(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iocert-manageracme.ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecution",
    jsii_struct_bases=[],
    name_mapping={"node_selector_terms": "nodeSelectorTerms"},
)
class ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecution:
    def __init__(
        self,
        *,
        node_selector_terms: typing.Sequence[typing.Union["ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionNodeSelectorTerms", typing.Dict[builtins.str, typing.Any]]],
    ) -> None:
        '''If the affinity requirements specified by this field are not met at scheduling time, the pod will not be scheduled onto the node.

        If the affinity requirements specified by this field cease to be met
        at some point during pod execution (e.g. due to an update), the system
        may or may not try to eventually evict the pod from its node.

        :param node_selector_terms: Required. A list of node selector terms. The terms are ORed.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecution
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__74cb1280f62c99f848d6543a528900668ec769966fcb0657c8cc495491177faa)
            check_type(argname="argument node_selector_terms", value=node_selector_terms, expected_type=type_hints["node_selector_terms"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "node_selector_terms": node_selector_terms,
        }

    @builtins.property
    def node_selector_terms(
        self,
    ) -> typing.List["ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionNodeSelectorTerms"]:
        '''Required.

        A list of node selector terms. The terms are ORed.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecution#nodeSelectorTerms
        '''
        result = self._values.get("node_selector_terms")
        assert result is not None, "Required property 'node_selector_terms' is missing"
        return typing.cast(typing.List["ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionNodeSelectorTerms"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecution(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iocert-manageracme.ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionNodeSelectorTerms",
    jsii_struct_bases=[],
    name_mapping={
        "match_expressions": "matchExpressions",
        "match_fields": "matchFields",
    },
)
class ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionNodeSelectorTerms:
    def __init__(
        self,
        *,
        match_expressions: typing.Optional[typing.Sequence[typing.Union["ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionNodeSelectorTermsMatchExpressions", typing.Dict[builtins.str, typing.Any]]]] = None,
        match_fields: typing.Optional[typing.Sequence[typing.Union["ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionNodeSelectorTermsMatchFields", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''A null or empty node selector term matches no objects.

        The requirements of
        them are ANDed.
        The TopologySelectorTerm type implements a subset of the NodeSelectorTerm.

        :param match_expressions: A list of node selector requirements by node's labels.
        :param match_fields: A list of node selector requirements by node's fields.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionNodeSelectorTerms
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3ccbf453c628c14ef4e41deb4f8c2c87966fbe1eda076107596587738cd86177)
            check_type(argname="argument match_expressions", value=match_expressions, expected_type=type_hints["match_expressions"])
            check_type(argname="argument match_fields", value=match_fields, expected_type=type_hints["match_fields"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if match_expressions is not None:
            self._values["match_expressions"] = match_expressions
        if match_fields is not None:
            self._values["match_fields"] = match_fields

    @builtins.property
    def match_expressions(
        self,
    ) -> typing.Optional[typing.List["ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionNodeSelectorTermsMatchExpressions"]]:
        '''A list of node selector requirements by node's labels.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionNodeSelectorTerms#matchExpressions
        '''
        result = self._values.get("match_expressions")
        return typing.cast(typing.Optional[typing.List["ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionNodeSelectorTermsMatchExpressions"]], result)

    @builtins.property
    def match_fields(
        self,
    ) -> typing.Optional[typing.List["ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionNodeSelectorTermsMatchFields"]]:
        '''A list of node selector requirements by node's fields.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionNodeSelectorTerms#matchFields
        '''
        result = self._values.get("match_fields")
        return typing.cast(typing.Optional[typing.List["ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionNodeSelectorTermsMatchFields"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionNodeSelectorTerms(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iocert-manageracme.ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionNodeSelectorTermsMatchExpressions",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "operator": "operator", "values": "values"},
)
class ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionNodeSelectorTermsMatchExpressions:
    def __init__(
        self,
        *,
        key: builtins.str,
        operator: builtins.str,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''A node selector requirement is a selector that contains values, a key, and an operator that relates the key and values.

        :param key: The label key that the selector applies to.
        :param operator: Represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists, DoesNotExist. Gt, and Lt.
        :param values: An array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. If the operator is Gt or Lt, the values array must have a single element, which will be interpreted as an integer. This array is replaced during a strategic merge patch.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionNodeSelectorTermsMatchExpressions
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__80e0f14fc3a9f8a109f8187cf59be5bfa20a08fa5fa4cbe9db6f93ee2b02a95e)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "key": key,
            "operator": operator,
        }
        if values is not None:
            self._values["values"] = values

    @builtins.property
    def key(self) -> builtins.str:
        '''The label key that the selector applies to.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionNodeSelectorTermsMatchExpressions#key
        '''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def operator(self) -> builtins.str:
        '''Represents a key's relationship to a set of values.

        Valid operators are In, NotIn, Exists, DoesNotExist. Gt, and Lt.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionNodeSelectorTermsMatchExpressions#operator
        '''
        result = self._values.get("operator")
        assert result is not None, "Required property 'operator' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''An array of string values.

        If the operator is In or NotIn,
        the values array must be non-empty. If the operator is Exists or DoesNotExist,
        the values array must be empty. If the operator is Gt or Lt, the values
        array must have a single element, which will be interpreted as an integer.
        This array is replaced during a strategic merge patch.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionNodeSelectorTermsMatchExpressions#values
        '''
        result = self._values.get("values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionNodeSelectorTermsMatchExpressions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iocert-manageracme.ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionNodeSelectorTermsMatchFields",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "operator": "operator", "values": "values"},
)
class ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionNodeSelectorTermsMatchFields:
    def __init__(
        self,
        *,
        key: builtins.str,
        operator: builtins.str,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''A node selector requirement is a selector that contains values, a key, and an operator that relates the key and values.

        :param key: The label key that the selector applies to.
        :param operator: Represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists, DoesNotExist. Gt, and Lt.
        :param values: An array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. If the operator is Gt or Lt, the values array must have a single element, which will be interpreted as an integer. This array is replaced during a strategic merge patch.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionNodeSelectorTermsMatchFields
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d5e485057f380eafea0393fc8c6d8ff975433ddf4622886bb65e808a15570c4d)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "key": key,
            "operator": operator,
        }
        if values is not None:
            self._values["values"] = values

    @builtins.property
    def key(self) -> builtins.str:
        '''The label key that the selector applies to.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionNodeSelectorTermsMatchFields#key
        '''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def operator(self) -> builtins.str:
        '''Represents a key's relationship to a set of values.

        Valid operators are In, NotIn, Exists, DoesNotExist. Gt, and Lt.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionNodeSelectorTermsMatchFields#operator
        '''
        result = self._values.get("operator")
        assert result is not None, "Required property 'operator' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''An array of string values.

        If the operator is In or NotIn,
        the values array must be non-empty. If the operator is Exists or DoesNotExist,
        the values array must be empty. If the operator is Gt or Lt, the values
        array must have a single element, which will be interpreted as an integer.
        This array is replaced during a strategic merge patch.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionNodeSelectorTermsMatchFields#values
        '''
        result = self._values.get("values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionNodeSelectorTermsMatchFields(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iocert-manageracme.ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAffinity",
    jsii_struct_bases=[],
    name_mapping={
        "preferred_during_scheduling_ignored_during_execution": "preferredDuringSchedulingIgnoredDuringExecution",
        "required_during_scheduling_ignored_during_execution": "requiredDuringSchedulingIgnoredDuringExecution",
    },
)
class ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAffinity:
    def __init__(
        self,
        *,
        preferred_during_scheduling_ignored_during_execution: typing.Optional[typing.Sequence[typing.Union["ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecution", typing.Dict[builtins.str, typing.Any]]]] = None,
        required_during_scheduling_ignored_during_execution: typing.Optional[typing.Sequence[typing.Union["ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAffinityRequiredDuringSchedulingIgnoredDuringExecution", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Describes pod affinity scheduling rules (e.g. co-locate this pod in the same node, zone, etc. as some other pod(s)).

        :param preferred_during_scheduling_ignored_during_execution: The scheduler will prefer to schedule pods to nodes that satisfy the affinity expressions specified by this field, but it may choose a node that violates one or more of the expressions. The node that is most preferred is the one with the greatest sum of weights, i.e. for each node that meets all of the scheduling requirements (resource request, requiredDuringScheduling affinity expressions, etc.), compute a sum by iterating through the elements of this field and adding "weight" to the sum if the node has pods which matches the corresponding podAffinityTerm; the node(s) with the highest sum are the most preferred.
        :param required_during_scheduling_ignored_during_execution: If the affinity requirements specified by this field are not met at scheduling time, the pod will not be scheduled onto the node. If the affinity requirements specified by this field cease to be met at some point during pod execution (e.g. due to a pod label update), the system may or may not try to eventually evict the pod from its node. When there are multiple elements, the lists of nodes corresponding to each podAffinityTerm are intersected, i.e. all terms must be satisfied.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAffinity
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__33b10d922b1a76975d3df2760ea198d948c1a6da497b852fa641491023c4a950)
            check_type(argname="argument preferred_during_scheduling_ignored_during_execution", value=preferred_during_scheduling_ignored_during_execution, expected_type=type_hints["preferred_during_scheduling_ignored_during_execution"])
            check_type(argname="argument required_during_scheduling_ignored_during_execution", value=required_during_scheduling_ignored_during_execution, expected_type=type_hints["required_during_scheduling_ignored_during_execution"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if preferred_during_scheduling_ignored_during_execution is not None:
            self._values["preferred_during_scheduling_ignored_during_execution"] = preferred_during_scheduling_ignored_during_execution
        if required_during_scheduling_ignored_during_execution is not None:
            self._values["required_during_scheduling_ignored_during_execution"] = required_during_scheduling_ignored_during_execution

    @builtins.property
    def preferred_during_scheduling_ignored_during_execution(
        self,
    ) -> typing.Optional[typing.List["ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecution"]]:
        '''The scheduler will prefer to schedule pods to nodes that satisfy the affinity expressions specified by this field, but it may choose a node that violates one or more of the expressions.

        The node that is
        most preferred is the one with the greatest sum of weights, i.e.
        for each node that meets all of the scheduling requirements (resource
        request, requiredDuringScheduling affinity expressions, etc.),
        compute a sum by iterating through the elements of this field and adding
        "weight" to the sum if the node has pods which matches the corresponding podAffinityTerm; the
        node(s) with the highest sum are the most preferred.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAffinity#preferredDuringSchedulingIgnoredDuringExecution
        '''
        result = self._values.get("preferred_during_scheduling_ignored_during_execution")
        return typing.cast(typing.Optional[typing.List["ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecution"]], result)

    @builtins.property
    def required_during_scheduling_ignored_during_execution(
        self,
    ) -> typing.Optional[typing.List["ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAffinityRequiredDuringSchedulingIgnoredDuringExecution"]]:
        '''If the affinity requirements specified by this field are not met at scheduling time, the pod will not be scheduled onto the node.

        If the affinity requirements specified by this field cease to be met
        at some point during pod execution (e.g. due to a pod label update), the
        system may or may not try to eventually evict the pod from its node.
        When there are multiple elements, the lists of nodes corresponding to each
        podAffinityTerm are intersected, i.e. all terms must be satisfied.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAffinity#requiredDuringSchedulingIgnoredDuringExecution
        '''
        result = self._values.get("required_during_scheduling_ignored_during_execution")
        return typing.cast(typing.Optional[typing.List["ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAffinityRequiredDuringSchedulingIgnoredDuringExecution"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAffinity(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iocert-manageracme.ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecution",
    jsii_struct_bases=[],
    name_mapping={"pod_affinity_term": "podAffinityTerm", "weight": "weight"},
)
class ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecution:
    def __init__(
        self,
        *,
        pod_affinity_term: typing.Union["ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTerm", typing.Dict[builtins.str, typing.Any]],
        weight: jsii.Number,
    ) -> None:
        '''The weights of all of the matched WeightedPodAffinityTerm fields are added per-node to find the most preferred node(s).

        :param pod_affinity_term: Required. A pod affinity term, associated with the corresponding weight.
        :param weight: weight associated with matching the corresponding podAffinityTerm, in the range 1-100.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecution
        '''
        if isinstance(pod_affinity_term, dict):
            pod_affinity_term = ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTerm(**pod_affinity_term)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__67f53537ce0524556f6febea3e39abcc9998a8a6cd9a5b23be72153f201e06fe)
            check_type(argname="argument pod_affinity_term", value=pod_affinity_term, expected_type=type_hints["pod_affinity_term"])
            check_type(argname="argument weight", value=weight, expected_type=type_hints["weight"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "pod_affinity_term": pod_affinity_term,
            "weight": weight,
        }

    @builtins.property
    def pod_affinity_term(
        self,
    ) -> "ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTerm":
        '''Required.

        A pod affinity term, associated with the corresponding weight.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecution#podAffinityTerm
        '''
        result = self._values.get("pod_affinity_term")
        assert result is not None, "Required property 'pod_affinity_term' is missing"
        return typing.cast("ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTerm", result)

    @builtins.property
    def weight(self) -> jsii.Number:
        '''weight associated with matching the corresponding podAffinityTerm, in the range 1-100.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecution#weight
        '''
        result = self._values.get("weight")
        assert result is not None, "Required property 'weight' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecution(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iocert-manageracme.ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTerm",
    jsii_struct_bases=[],
    name_mapping={
        "topology_key": "topologyKey",
        "label_selector": "labelSelector",
        "match_label_keys": "matchLabelKeys",
        "mismatch_label_keys": "mismatchLabelKeys",
        "namespaces": "namespaces",
        "namespace_selector": "namespaceSelector",
    },
)
class ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTerm:
    def __init__(
        self,
        *,
        topology_key: builtins.str,
        label_selector: typing.Optional[typing.Union["ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermLabelSelector", typing.Dict[builtins.str, typing.Any]]] = None,
        match_label_keys: typing.Optional[typing.Sequence[builtins.str]] = None,
        mismatch_label_keys: typing.Optional[typing.Sequence[builtins.str]] = None,
        namespaces: typing.Optional[typing.Sequence[builtins.str]] = None,
        namespace_selector: typing.Optional[typing.Union["ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermNamespaceSelector", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''Required.

        A pod affinity term, associated with the corresponding weight.

        :param topology_key: This pod should be co-located (affinity) or not co-located (anti-affinity) with the pods matching the labelSelector in the specified namespaces, where co-located is defined as running on a node whose value of the label with key topologyKey matches that of any node on which any of the selected pods is running. Empty topologyKey is not allowed.
        :param label_selector: A label query over a set of resources, in this case pods. If it's null, this PodAffinityTerm matches with no Pods.
        :param match_label_keys: MatchLabelKeys is a set of pod label keys to select which pods will be taken into consideration. The keys are used to lookup values from the incoming pod labels, those key-value labels are merged with ``labelSelector`` as ``key in (value)`` to select the group of existing pods which pods will be taken into consideration for the incoming pod's pod (anti) affinity. Keys that don't exist in the incoming pod labels will be ignored. The default value is empty. The same key is forbidden to exist in both matchLabelKeys and labelSelector. Also, matchLabelKeys cannot be set when labelSelector isn't set. This is a beta field and requires enabling MatchLabelKeysInPodAffinity feature gate (enabled by default).
        :param mismatch_label_keys: MismatchLabelKeys is a set of pod label keys to select which pods will be taken into consideration. The keys are used to lookup values from the incoming pod labels, those key-value labels are merged with ``labelSelector`` as ``key notin (value)`` to select the group of existing pods which pods will be taken into consideration for the incoming pod's pod (anti) affinity. Keys that don't exist in the incoming pod labels will be ignored. The default value is empty. The same key is forbidden to exist in both mismatchLabelKeys and labelSelector. Also, mismatchLabelKeys cannot be set when labelSelector isn't set. This is a beta field and requires enabling MatchLabelKeysInPodAffinity feature gate (enabled by default).
        :param namespaces: namespaces specifies a static list of namespace names that the term applies to. The term is applied to the union of the namespaces listed in this field and the ones selected by namespaceSelector. null or empty namespaces list and null namespaceSelector means "this pod's namespace".
        :param namespace_selector: A label query over the set of namespaces that the term applies to. The term is applied to the union of the namespaces selected by this field and the ones listed in the namespaces field. null selector and null or empty namespaces list means "this pod's namespace". An empty selector ({}) matches all namespaces.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTerm
        '''
        if isinstance(label_selector, dict):
            label_selector = ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermLabelSelector(**label_selector)
        if isinstance(namespace_selector, dict):
            namespace_selector = ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermNamespaceSelector(**namespace_selector)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__59bac6e6f124245bf9dc813ceb6d089aa3f3574cb85ad97edc5edc4c48b00453)
            check_type(argname="argument topology_key", value=topology_key, expected_type=type_hints["topology_key"])
            check_type(argname="argument label_selector", value=label_selector, expected_type=type_hints["label_selector"])
            check_type(argname="argument match_label_keys", value=match_label_keys, expected_type=type_hints["match_label_keys"])
            check_type(argname="argument mismatch_label_keys", value=mismatch_label_keys, expected_type=type_hints["mismatch_label_keys"])
            check_type(argname="argument namespaces", value=namespaces, expected_type=type_hints["namespaces"])
            check_type(argname="argument namespace_selector", value=namespace_selector, expected_type=type_hints["namespace_selector"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "topology_key": topology_key,
        }
        if label_selector is not None:
            self._values["label_selector"] = label_selector
        if match_label_keys is not None:
            self._values["match_label_keys"] = match_label_keys
        if mismatch_label_keys is not None:
            self._values["mismatch_label_keys"] = mismatch_label_keys
        if namespaces is not None:
            self._values["namespaces"] = namespaces
        if namespace_selector is not None:
            self._values["namespace_selector"] = namespace_selector

    @builtins.property
    def topology_key(self) -> builtins.str:
        '''This pod should be co-located (affinity) or not co-located (anti-affinity) with the pods matching the labelSelector in the specified namespaces, where co-located is defined as running on a node whose value of the label with key topologyKey matches that of any node on which any of the selected pods is running.

        Empty topologyKey is not allowed.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTerm#topologyKey
        '''
        result = self._values.get("topology_key")
        assert result is not None, "Required property 'topology_key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def label_selector(
        self,
    ) -> typing.Optional["ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermLabelSelector"]:
        '''A label query over a set of resources, in this case pods.

        If it's null, this PodAffinityTerm matches with no Pods.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTerm#labelSelector
        '''
        result = self._values.get("label_selector")
        return typing.cast(typing.Optional["ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermLabelSelector"], result)

    @builtins.property
    def match_label_keys(self) -> typing.Optional[typing.List[builtins.str]]:
        '''MatchLabelKeys is a set of pod label keys to select which pods will be taken into consideration.

        The keys are used to lookup values from the
        incoming pod labels, those key-value labels are merged with ``labelSelector`` as ``key in (value)``
        to select the group of existing pods which pods will be taken into consideration
        for the incoming pod's pod (anti) affinity. Keys that don't exist in the incoming
        pod labels will be ignored. The default value is empty.
        The same key is forbidden to exist in both matchLabelKeys and labelSelector.
        Also, matchLabelKeys cannot be set when labelSelector isn't set.
        This is a beta field and requires enabling MatchLabelKeysInPodAffinity feature gate (enabled by default).

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTerm#matchLabelKeys
        '''
        result = self._values.get("match_label_keys")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def mismatch_label_keys(self) -> typing.Optional[typing.List[builtins.str]]:
        '''MismatchLabelKeys is a set of pod label keys to select which pods will be taken into consideration.

        The keys are used to lookup values from the
        incoming pod labels, those key-value labels are merged with ``labelSelector`` as ``key notin (value)``
        to select the group of existing pods which pods will be taken into consideration
        for the incoming pod's pod (anti) affinity. Keys that don't exist in the incoming
        pod labels will be ignored. The default value is empty.
        The same key is forbidden to exist in both mismatchLabelKeys and labelSelector.
        Also, mismatchLabelKeys cannot be set when labelSelector isn't set.
        This is a beta field and requires enabling MatchLabelKeysInPodAffinity feature gate (enabled by default).

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTerm#mismatchLabelKeys
        '''
        result = self._values.get("mismatch_label_keys")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def namespaces(self) -> typing.Optional[typing.List[builtins.str]]:
        '''namespaces specifies a static list of namespace names that the term applies to.

        The term is applied to the union of the namespaces listed in this field
        and the ones selected by namespaceSelector.
        null or empty namespaces list and null namespaceSelector means "this pod's namespace".

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTerm#namespaces
        '''
        result = self._values.get("namespaces")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def namespace_selector(
        self,
    ) -> typing.Optional["ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermNamespaceSelector"]:
        '''A label query over the set of namespaces that the term applies to.

        The term is applied to the union of the namespaces selected by this field
        and the ones listed in the namespaces field.
        null selector and null or empty namespaces list means "this pod's namespace".
        An empty selector ({}) matches all namespaces.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTerm#namespaceSelector
        '''
        result = self._values.get("namespace_selector")
        return typing.cast(typing.Optional["ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermNamespaceSelector"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTerm(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iocert-manageracme.ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermLabelSelector",
    jsii_struct_bases=[],
    name_mapping={
        "match_expressions": "matchExpressions",
        "match_labels": "matchLabels",
    },
)
class ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermLabelSelector:
    def __init__(
        self,
        *,
        match_expressions: typing.Optional[typing.Sequence[typing.Union["ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermLabelSelectorMatchExpressions", typing.Dict[builtins.str, typing.Any]]]] = None,
        match_labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''A label query over a set of resources, in this case pods.

        If it's null, this PodAffinityTerm matches with no Pods.

        :param match_expressions: matchExpressions is a list of label selector requirements. The requirements are ANDed.
        :param match_labels: matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermLabelSelector
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b4c32c657c3245e1f11a50ee06ae58c382b71871f98c5a99c5a96ae82f4c6225)
            check_type(argname="argument match_expressions", value=match_expressions, expected_type=type_hints["match_expressions"])
            check_type(argname="argument match_labels", value=match_labels, expected_type=type_hints["match_labels"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if match_expressions is not None:
            self._values["match_expressions"] = match_expressions
        if match_labels is not None:
            self._values["match_labels"] = match_labels

    @builtins.property
    def match_expressions(
        self,
    ) -> typing.Optional[typing.List["ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermLabelSelectorMatchExpressions"]]:
        '''matchExpressions is a list of label selector requirements.

        The requirements are ANDed.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermLabelSelector#matchExpressions
        '''
        result = self._values.get("match_expressions")
        return typing.cast(typing.Optional[typing.List["ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermLabelSelectorMatchExpressions"]], result)

    @builtins.property
    def match_labels(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''matchLabels is a map of {key,value} pairs.

        A single {key,value} in the matchLabels
        map is equivalent to an element of matchExpressions, whose key field is "key", the
        operator is "In", and the values array contains only "value". The requirements are ANDed.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermLabelSelector#matchLabels
        '''
        result = self._values.get("match_labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermLabelSelector(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iocert-manageracme.ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermLabelSelectorMatchExpressions",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "operator": "operator", "values": "values"},
)
class ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermLabelSelectorMatchExpressions:
    def __init__(
        self,
        *,
        key: builtins.str,
        operator: builtins.str,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''A label selector requirement is a selector that contains values, a key, and an operator that relates the key and values.

        :param key: key is the label key that the selector applies to.
        :param operator: operator represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist.
        :param values: values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermLabelSelectorMatchExpressions
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__de0c97d9dff0c2c2d2c2587a6a7b2f3fa7794d4e9379ca59079608c798168500)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "key": key,
            "operator": operator,
        }
        if values is not None:
            self._values["values"] = values

    @builtins.property
    def key(self) -> builtins.str:
        '''key is the label key that the selector applies to.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermLabelSelectorMatchExpressions#key
        '''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def operator(self) -> builtins.str:
        '''operator represents a key's relationship to a set of values.

        Valid operators are In, NotIn, Exists and DoesNotExist.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermLabelSelectorMatchExpressions#operator
        '''
        result = self._values.get("operator")
        assert result is not None, "Required property 'operator' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''values is an array of string values.

        If the operator is In or NotIn,
        the values array must be non-empty. If the operator is Exists or DoesNotExist,
        the values array must be empty. This array is replaced during a strategic
        merge patch.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermLabelSelectorMatchExpressions#values
        '''
        result = self._values.get("values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermLabelSelectorMatchExpressions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iocert-manageracme.ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermNamespaceSelector",
    jsii_struct_bases=[],
    name_mapping={
        "match_expressions": "matchExpressions",
        "match_labels": "matchLabels",
    },
)
class ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermNamespaceSelector:
    def __init__(
        self,
        *,
        match_expressions: typing.Optional[typing.Sequence[typing.Union["ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermNamespaceSelectorMatchExpressions", typing.Dict[builtins.str, typing.Any]]]] = None,
        match_labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''A label query over the set of namespaces that the term applies to.

        The term is applied to the union of the namespaces selected by this field
        and the ones listed in the namespaces field.
        null selector and null or empty namespaces list means "this pod's namespace".
        An empty selector ({}) matches all namespaces.

        :param match_expressions: matchExpressions is a list of label selector requirements. The requirements are ANDed.
        :param match_labels: matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermNamespaceSelector
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b678c9f015deab9cd50fcc1b91511f7ba8d45ef2355b983fe50c590136fb9a82)
            check_type(argname="argument match_expressions", value=match_expressions, expected_type=type_hints["match_expressions"])
            check_type(argname="argument match_labels", value=match_labels, expected_type=type_hints["match_labels"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if match_expressions is not None:
            self._values["match_expressions"] = match_expressions
        if match_labels is not None:
            self._values["match_labels"] = match_labels

    @builtins.property
    def match_expressions(
        self,
    ) -> typing.Optional[typing.List["ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermNamespaceSelectorMatchExpressions"]]:
        '''matchExpressions is a list of label selector requirements.

        The requirements are ANDed.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermNamespaceSelector#matchExpressions
        '''
        result = self._values.get("match_expressions")
        return typing.cast(typing.Optional[typing.List["ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermNamespaceSelectorMatchExpressions"]], result)

    @builtins.property
    def match_labels(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''matchLabels is a map of {key,value} pairs.

        A single {key,value} in the matchLabels
        map is equivalent to an element of matchExpressions, whose key field is "key", the
        operator is "In", and the values array contains only "value". The requirements are ANDed.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermNamespaceSelector#matchLabels
        '''
        result = self._values.get("match_labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermNamespaceSelector(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iocert-manageracme.ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermNamespaceSelectorMatchExpressions",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "operator": "operator", "values": "values"},
)
class ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermNamespaceSelectorMatchExpressions:
    def __init__(
        self,
        *,
        key: builtins.str,
        operator: builtins.str,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''A label selector requirement is a selector that contains values, a key, and an operator that relates the key and values.

        :param key: key is the label key that the selector applies to.
        :param operator: operator represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist.
        :param values: values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermNamespaceSelectorMatchExpressions
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8ae3833d224068fda7617d873ea8b79f95b81bced9f6999ef1ece4589a886e22)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "key": key,
            "operator": operator,
        }
        if values is not None:
            self._values["values"] = values

    @builtins.property
    def key(self) -> builtins.str:
        '''key is the label key that the selector applies to.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermNamespaceSelectorMatchExpressions#key
        '''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def operator(self) -> builtins.str:
        '''operator represents a key's relationship to a set of values.

        Valid operators are In, NotIn, Exists and DoesNotExist.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermNamespaceSelectorMatchExpressions#operator
        '''
        result = self._values.get("operator")
        assert result is not None, "Required property 'operator' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''values is an array of string values.

        If the operator is In or NotIn,
        the values array must be non-empty. If the operator is Exists or DoesNotExist,
        the values array must be empty. This array is replaced during a strategic
        merge patch.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermNamespaceSelectorMatchExpressions#values
        '''
        result = self._values.get("values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermNamespaceSelectorMatchExpressions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iocert-manageracme.ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAffinityRequiredDuringSchedulingIgnoredDuringExecution",
    jsii_struct_bases=[],
    name_mapping={
        "topology_key": "topologyKey",
        "label_selector": "labelSelector",
        "match_label_keys": "matchLabelKeys",
        "mismatch_label_keys": "mismatchLabelKeys",
        "namespaces": "namespaces",
        "namespace_selector": "namespaceSelector",
    },
)
class ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAffinityRequiredDuringSchedulingIgnoredDuringExecution:
    def __init__(
        self,
        *,
        topology_key: builtins.str,
        label_selector: typing.Optional[typing.Union["ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAffinityRequiredDuringSchedulingIgnoredDuringExecutionLabelSelector", typing.Dict[builtins.str, typing.Any]]] = None,
        match_label_keys: typing.Optional[typing.Sequence[builtins.str]] = None,
        mismatch_label_keys: typing.Optional[typing.Sequence[builtins.str]] = None,
        namespaces: typing.Optional[typing.Sequence[builtins.str]] = None,
        namespace_selector: typing.Optional[typing.Union["ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAffinityRequiredDuringSchedulingIgnoredDuringExecutionNamespaceSelector", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''Defines a set of pods (namely those matching the labelSelector relative to the given namespace(s)) that this pod should be co-located (affinity) or not co-located (anti-affinity) with, where co-located is defined as running on a node whose value of the label with key  matches that of any node on which a pod of the set of pods is running.

        :param topology_key: This pod should be co-located (affinity) or not co-located (anti-affinity) with the pods matching the labelSelector in the specified namespaces, where co-located is defined as running on a node whose value of the label with key topologyKey matches that of any node on which any of the selected pods is running. Empty topologyKey is not allowed.
        :param label_selector: A label query over a set of resources, in this case pods. If it's null, this PodAffinityTerm matches with no Pods.
        :param match_label_keys: MatchLabelKeys is a set of pod label keys to select which pods will be taken into consideration. The keys are used to lookup values from the incoming pod labels, those key-value labels are merged with ``labelSelector`` as ``key in (value)`` to select the group of existing pods which pods will be taken into consideration for the incoming pod's pod (anti) affinity. Keys that don't exist in the incoming pod labels will be ignored. The default value is empty. The same key is forbidden to exist in both matchLabelKeys and labelSelector. Also, matchLabelKeys cannot be set when labelSelector isn't set. This is a beta field and requires enabling MatchLabelKeysInPodAffinity feature gate (enabled by default).
        :param mismatch_label_keys: MismatchLabelKeys is a set of pod label keys to select which pods will be taken into consideration. The keys are used to lookup values from the incoming pod labels, those key-value labels are merged with ``labelSelector`` as ``key notin (value)`` to select the group of existing pods which pods will be taken into consideration for the incoming pod's pod (anti) affinity. Keys that don't exist in the incoming pod labels will be ignored. The default value is empty. The same key is forbidden to exist in both mismatchLabelKeys and labelSelector. Also, mismatchLabelKeys cannot be set when labelSelector isn't set. This is a beta field and requires enabling MatchLabelKeysInPodAffinity feature gate (enabled by default).
        :param namespaces: namespaces specifies a static list of namespace names that the term applies to. The term is applied to the union of the namespaces listed in this field and the ones selected by namespaceSelector. null or empty namespaces list and null namespaceSelector means "this pod's namespace".
        :param namespace_selector: A label query over the set of namespaces that the term applies to. The term is applied to the union of the namespaces selected by this field and the ones listed in the namespaces field. null selector and null or empty namespaces list means "this pod's namespace". An empty selector ({}) matches all namespaces.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAffinityRequiredDuringSchedulingIgnoredDuringExecution
        '''
        if isinstance(label_selector, dict):
            label_selector = ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAffinityRequiredDuringSchedulingIgnoredDuringExecutionLabelSelector(**label_selector)
        if isinstance(namespace_selector, dict):
            namespace_selector = ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAffinityRequiredDuringSchedulingIgnoredDuringExecutionNamespaceSelector(**namespace_selector)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3ce9f181986eb8f42bfa4cbdbe2f2a431316064988311bdca7206ee529efdf50)
            check_type(argname="argument topology_key", value=topology_key, expected_type=type_hints["topology_key"])
            check_type(argname="argument label_selector", value=label_selector, expected_type=type_hints["label_selector"])
            check_type(argname="argument match_label_keys", value=match_label_keys, expected_type=type_hints["match_label_keys"])
            check_type(argname="argument mismatch_label_keys", value=mismatch_label_keys, expected_type=type_hints["mismatch_label_keys"])
            check_type(argname="argument namespaces", value=namespaces, expected_type=type_hints["namespaces"])
            check_type(argname="argument namespace_selector", value=namespace_selector, expected_type=type_hints["namespace_selector"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "topology_key": topology_key,
        }
        if label_selector is not None:
            self._values["label_selector"] = label_selector
        if match_label_keys is not None:
            self._values["match_label_keys"] = match_label_keys
        if mismatch_label_keys is not None:
            self._values["mismatch_label_keys"] = mismatch_label_keys
        if namespaces is not None:
            self._values["namespaces"] = namespaces
        if namespace_selector is not None:
            self._values["namespace_selector"] = namespace_selector

    @builtins.property
    def topology_key(self) -> builtins.str:
        '''This pod should be co-located (affinity) or not co-located (anti-affinity) with the pods matching the labelSelector in the specified namespaces, where co-located is defined as running on a node whose value of the label with key topologyKey matches that of any node on which any of the selected pods is running.

        Empty topologyKey is not allowed.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAffinityRequiredDuringSchedulingIgnoredDuringExecution#topologyKey
        '''
        result = self._values.get("topology_key")
        assert result is not None, "Required property 'topology_key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def label_selector(
        self,
    ) -> typing.Optional["ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAffinityRequiredDuringSchedulingIgnoredDuringExecutionLabelSelector"]:
        '''A label query over a set of resources, in this case pods.

        If it's null, this PodAffinityTerm matches with no Pods.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAffinityRequiredDuringSchedulingIgnoredDuringExecution#labelSelector
        '''
        result = self._values.get("label_selector")
        return typing.cast(typing.Optional["ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAffinityRequiredDuringSchedulingIgnoredDuringExecutionLabelSelector"], result)

    @builtins.property
    def match_label_keys(self) -> typing.Optional[typing.List[builtins.str]]:
        '''MatchLabelKeys is a set of pod label keys to select which pods will be taken into consideration.

        The keys are used to lookup values from the
        incoming pod labels, those key-value labels are merged with ``labelSelector`` as ``key in (value)``
        to select the group of existing pods which pods will be taken into consideration
        for the incoming pod's pod (anti) affinity. Keys that don't exist in the incoming
        pod labels will be ignored. The default value is empty.
        The same key is forbidden to exist in both matchLabelKeys and labelSelector.
        Also, matchLabelKeys cannot be set when labelSelector isn't set.
        This is a beta field and requires enabling MatchLabelKeysInPodAffinity feature gate (enabled by default).

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAffinityRequiredDuringSchedulingIgnoredDuringExecution#matchLabelKeys
        '''
        result = self._values.get("match_label_keys")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def mismatch_label_keys(self) -> typing.Optional[typing.List[builtins.str]]:
        '''MismatchLabelKeys is a set of pod label keys to select which pods will be taken into consideration.

        The keys are used to lookup values from the
        incoming pod labels, those key-value labels are merged with ``labelSelector`` as ``key notin (value)``
        to select the group of existing pods which pods will be taken into consideration
        for the incoming pod's pod (anti) affinity. Keys that don't exist in the incoming
        pod labels will be ignored. The default value is empty.
        The same key is forbidden to exist in both mismatchLabelKeys and labelSelector.
        Also, mismatchLabelKeys cannot be set when labelSelector isn't set.
        This is a beta field and requires enabling MatchLabelKeysInPodAffinity feature gate (enabled by default).

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAffinityRequiredDuringSchedulingIgnoredDuringExecution#mismatchLabelKeys
        '''
        result = self._values.get("mismatch_label_keys")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def namespaces(self) -> typing.Optional[typing.List[builtins.str]]:
        '''namespaces specifies a static list of namespace names that the term applies to.

        The term is applied to the union of the namespaces listed in this field
        and the ones selected by namespaceSelector.
        null or empty namespaces list and null namespaceSelector means "this pod's namespace".

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAffinityRequiredDuringSchedulingIgnoredDuringExecution#namespaces
        '''
        result = self._values.get("namespaces")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def namespace_selector(
        self,
    ) -> typing.Optional["ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAffinityRequiredDuringSchedulingIgnoredDuringExecutionNamespaceSelector"]:
        '''A label query over the set of namespaces that the term applies to.

        The term is applied to the union of the namespaces selected by this field
        and the ones listed in the namespaces field.
        null selector and null or empty namespaces list means "this pod's namespace".
        An empty selector ({}) matches all namespaces.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAffinityRequiredDuringSchedulingIgnoredDuringExecution#namespaceSelector
        '''
        result = self._values.get("namespace_selector")
        return typing.cast(typing.Optional["ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAffinityRequiredDuringSchedulingIgnoredDuringExecutionNamespaceSelector"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAffinityRequiredDuringSchedulingIgnoredDuringExecution(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iocert-manageracme.ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAffinityRequiredDuringSchedulingIgnoredDuringExecutionLabelSelector",
    jsii_struct_bases=[],
    name_mapping={
        "match_expressions": "matchExpressions",
        "match_labels": "matchLabels",
    },
)
class ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAffinityRequiredDuringSchedulingIgnoredDuringExecutionLabelSelector:
    def __init__(
        self,
        *,
        match_expressions: typing.Optional[typing.Sequence[typing.Union["ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAffinityRequiredDuringSchedulingIgnoredDuringExecutionLabelSelectorMatchExpressions", typing.Dict[builtins.str, typing.Any]]]] = None,
        match_labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''A label query over a set of resources, in this case pods.

        If it's null, this PodAffinityTerm matches with no Pods.

        :param match_expressions: matchExpressions is a list of label selector requirements. The requirements are ANDed.
        :param match_labels: matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAffinityRequiredDuringSchedulingIgnoredDuringExecutionLabelSelector
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1cde2a7027ae8f0384b9d9f345ed8dc62c025be1fac7357251307c84f1c367db)
            check_type(argname="argument match_expressions", value=match_expressions, expected_type=type_hints["match_expressions"])
            check_type(argname="argument match_labels", value=match_labels, expected_type=type_hints["match_labels"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if match_expressions is not None:
            self._values["match_expressions"] = match_expressions
        if match_labels is not None:
            self._values["match_labels"] = match_labels

    @builtins.property
    def match_expressions(
        self,
    ) -> typing.Optional[typing.List["ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAffinityRequiredDuringSchedulingIgnoredDuringExecutionLabelSelectorMatchExpressions"]]:
        '''matchExpressions is a list of label selector requirements.

        The requirements are ANDed.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAffinityRequiredDuringSchedulingIgnoredDuringExecutionLabelSelector#matchExpressions
        '''
        result = self._values.get("match_expressions")
        return typing.cast(typing.Optional[typing.List["ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAffinityRequiredDuringSchedulingIgnoredDuringExecutionLabelSelectorMatchExpressions"]], result)

    @builtins.property
    def match_labels(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''matchLabels is a map of {key,value} pairs.

        A single {key,value} in the matchLabels
        map is equivalent to an element of matchExpressions, whose key field is "key", the
        operator is "In", and the values array contains only "value". The requirements are ANDed.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAffinityRequiredDuringSchedulingIgnoredDuringExecutionLabelSelector#matchLabels
        '''
        result = self._values.get("match_labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAffinityRequiredDuringSchedulingIgnoredDuringExecutionLabelSelector(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iocert-manageracme.ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAffinityRequiredDuringSchedulingIgnoredDuringExecutionLabelSelectorMatchExpressions",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "operator": "operator", "values": "values"},
)
class ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAffinityRequiredDuringSchedulingIgnoredDuringExecutionLabelSelectorMatchExpressions:
    def __init__(
        self,
        *,
        key: builtins.str,
        operator: builtins.str,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''A label selector requirement is a selector that contains values, a key, and an operator that relates the key and values.

        :param key: key is the label key that the selector applies to.
        :param operator: operator represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist.
        :param values: values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAffinityRequiredDuringSchedulingIgnoredDuringExecutionLabelSelectorMatchExpressions
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6f7a74a2a9316f44df5b278fd9cc43d7538a613f15acd3c0c2baa46dfcbcfe4f)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "key": key,
            "operator": operator,
        }
        if values is not None:
            self._values["values"] = values

    @builtins.property
    def key(self) -> builtins.str:
        '''key is the label key that the selector applies to.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAffinityRequiredDuringSchedulingIgnoredDuringExecutionLabelSelectorMatchExpressions#key
        '''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def operator(self) -> builtins.str:
        '''operator represents a key's relationship to a set of values.

        Valid operators are In, NotIn, Exists and DoesNotExist.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAffinityRequiredDuringSchedulingIgnoredDuringExecutionLabelSelectorMatchExpressions#operator
        '''
        result = self._values.get("operator")
        assert result is not None, "Required property 'operator' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''values is an array of string values.

        If the operator is In or NotIn,
        the values array must be non-empty. If the operator is Exists or DoesNotExist,
        the values array must be empty. This array is replaced during a strategic
        merge patch.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAffinityRequiredDuringSchedulingIgnoredDuringExecutionLabelSelectorMatchExpressions#values
        '''
        result = self._values.get("values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAffinityRequiredDuringSchedulingIgnoredDuringExecutionLabelSelectorMatchExpressions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iocert-manageracme.ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAffinityRequiredDuringSchedulingIgnoredDuringExecutionNamespaceSelector",
    jsii_struct_bases=[],
    name_mapping={
        "match_expressions": "matchExpressions",
        "match_labels": "matchLabels",
    },
)
class ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAffinityRequiredDuringSchedulingIgnoredDuringExecutionNamespaceSelector:
    def __init__(
        self,
        *,
        match_expressions: typing.Optional[typing.Sequence[typing.Union["ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAffinityRequiredDuringSchedulingIgnoredDuringExecutionNamespaceSelectorMatchExpressions", typing.Dict[builtins.str, typing.Any]]]] = None,
        match_labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''A label query over the set of namespaces that the term applies to.

        The term is applied to the union of the namespaces selected by this field
        and the ones listed in the namespaces field.
        null selector and null or empty namespaces list means "this pod's namespace".
        An empty selector ({}) matches all namespaces.

        :param match_expressions: matchExpressions is a list of label selector requirements. The requirements are ANDed.
        :param match_labels: matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAffinityRequiredDuringSchedulingIgnoredDuringExecutionNamespaceSelector
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d008cfffcc49a81208480db0ac6b715f38dd6090afbf1fc5e313de9c16a5be6f)
            check_type(argname="argument match_expressions", value=match_expressions, expected_type=type_hints["match_expressions"])
            check_type(argname="argument match_labels", value=match_labels, expected_type=type_hints["match_labels"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if match_expressions is not None:
            self._values["match_expressions"] = match_expressions
        if match_labels is not None:
            self._values["match_labels"] = match_labels

    @builtins.property
    def match_expressions(
        self,
    ) -> typing.Optional[typing.List["ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAffinityRequiredDuringSchedulingIgnoredDuringExecutionNamespaceSelectorMatchExpressions"]]:
        '''matchExpressions is a list of label selector requirements.

        The requirements are ANDed.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAffinityRequiredDuringSchedulingIgnoredDuringExecutionNamespaceSelector#matchExpressions
        '''
        result = self._values.get("match_expressions")
        return typing.cast(typing.Optional[typing.List["ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAffinityRequiredDuringSchedulingIgnoredDuringExecutionNamespaceSelectorMatchExpressions"]], result)

    @builtins.property
    def match_labels(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''matchLabels is a map of {key,value} pairs.

        A single {key,value} in the matchLabels
        map is equivalent to an element of matchExpressions, whose key field is "key", the
        operator is "In", and the values array contains only "value". The requirements are ANDed.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAffinityRequiredDuringSchedulingIgnoredDuringExecutionNamespaceSelector#matchLabels
        '''
        result = self._values.get("match_labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAffinityRequiredDuringSchedulingIgnoredDuringExecutionNamespaceSelector(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iocert-manageracme.ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAffinityRequiredDuringSchedulingIgnoredDuringExecutionNamespaceSelectorMatchExpressions",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "operator": "operator", "values": "values"},
)
class ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAffinityRequiredDuringSchedulingIgnoredDuringExecutionNamespaceSelectorMatchExpressions:
    def __init__(
        self,
        *,
        key: builtins.str,
        operator: builtins.str,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''A label selector requirement is a selector that contains values, a key, and an operator that relates the key and values.

        :param key: key is the label key that the selector applies to.
        :param operator: operator represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist.
        :param values: values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAffinityRequiredDuringSchedulingIgnoredDuringExecutionNamespaceSelectorMatchExpressions
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fddaf38947b6fd41b382e5a972df5b2a31da5d5fb6acc791cc01a38d0ba79909)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "key": key,
            "operator": operator,
        }
        if values is not None:
            self._values["values"] = values

    @builtins.property
    def key(self) -> builtins.str:
        '''key is the label key that the selector applies to.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAffinityRequiredDuringSchedulingIgnoredDuringExecutionNamespaceSelectorMatchExpressions#key
        '''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def operator(self) -> builtins.str:
        '''operator represents a key's relationship to a set of values.

        Valid operators are In, NotIn, Exists and DoesNotExist.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAffinityRequiredDuringSchedulingIgnoredDuringExecutionNamespaceSelectorMatchExpressions#operator
        '''
        result = self._values.get("operator")
        assert result is not None, "Required property 'operator' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''values is an array of string values.

        If the operator is In or NotIn,
        the values array must be non-empty. If the operator is Exists or DoesNotExist,
        the values array must be empty. This array is replaced during a strategic
        merge patch.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAffinityRequiredDuringSchedulingIgnoredDuringExecutionNamespaceSelectorMatchExpressions#values
        '''
        result = self._values.get("values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAffinityRequiredDuringSchedulingIgnoredDuringExecutionNamespaceSelectorMatchExpressions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iocert-manageracme.ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAntiAffinity",
    jsii_struct_bases=[],
    name_mapping={
        "preferred_during_scheduling_ignored_during_execution": "preferredDuringSchedulingIgnoredDuringExecution",
        "required_during_scheduling_ignored_during_execution": "requiredDuringSchedulingIgnoredDuringExecution",
    },
)
class ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAntiAffinity:
    def __init__(
        self,
        *,
        preferred_during_scheduling_ignored_during_execution: typing.Optional[typing.Sequence[typing.Union["ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecution", typing.Dict[builtins.str, typing.Any]]]] = None,
        required_during_scheduling_ignored_during_execution: typing.Optional[typing.Sequence[typing.Union["ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAntiAffinityRequiredDuringSchedulingIgnoredDuringExecution", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Describes pod anti-affinity scheduling rules (e.g. avoid putting this pod in the same node, zone, etc. as some other pod(s)).

        :param preferred_during_scheduling_ignored_during_execution: The scheduler will prefer to schedule pods to nodes that satisfy the anti-affinity expressions specified by this field, but it may choose a node that violates one or more of the expressions. The node that is most preferred is the one with the greatest sum of weights, i.e. for each node that meets all of the scheduling requirements (resource request, requiredDuringScheduling anti-affinity expressions, etc.), compute a sum by iterating through the elements of this field and adding "weight" to the sum if the node has pods which matches the corresponding podAffinityTerm; the node(s) with the highest sum are the most preferred.
        :param required_during_scheduling_ignored_during_execution: If the anti-affinity requirements specified by this field are not met at scheduling time, the pod will not be scheduled onto the node. If the anti-affinity requirements specified by this field cease to be met at some point during pod execution (e.g. due to a pod label update), the system may or may not try to eventually evict the pod from its node. When there are multiple elements, the lists of nodes corresponding to each podAffinityTerm are intersected, i.e. all terms must be satisfied.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAntiAffinity
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ab821dd2a088e090fd858a740965c376402052b2c8587ac3dfb937cf89c3eefc)
            check_type(argname="argument preferred_during_scheduling_ignored_during_execution", value=preferred_during_scheduling_ignored_during_execution, expected_type=type_hints["preferred_during_scheduling_ignored_during_execution"])
            check_type(argname="argument required_during_scheduling_ignored_during_execution", value=required_during_scheduling_ignored_during_execution, expected_type=type_hints["required_during_scheduling_ignored_during_execution"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if preferred_during_scheduling_ignored_during_execution is not None:
            self._values["preferred_during_scheduling_ignored_during_execution"] = preferred_during_scheduling_ignored_during_execution
        if required_during_scheduling_ignored_during_execution is not None:
            self._values["required_during_scheduling_ignored_during_execution"] = required_during_scheduling_ignored_during_execution

    @builtins.property
    def preferred_during_scheduling_ignored_during_execution(
        self,
    ) -> typing.Optional[typing.List["ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecution"]]:
        '''The scheduler will prefer to schedule pods to nodes that satisfy the anti-affinity expressions specified by this field, but it may choose a node that violates one or more of the expressions.

        The node that is
        most preferred is the one with the greatest sum of weights, i.e.
        for each node that meets all of the scheduling requirements (resource
        request, requiredDuringScheduling anti-affinity expressions, etc.),
        compute a sum by iterating through the elements of this field and adding
        "weight" to the sum if the node has pods which matches the corresponding podAffinityTerm; the
        node(s) with the highest sum are the most preferred.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAntiAffinity#preferredDuringSchedulingIgnoredDuringExecution
        '''
        result = self._values.get("preferred_during_scheduling_ignored_during_execution")
        return typing.cast(typing.Optional[typing.List["ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecution"]], result)

    @builtins.property
    def required_during_scheduling_ignored_during_execution(
        self,
    ) -> typing.Optional[typing.List["ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAntiAffinityRequiredDuringSchedulingIgnoredDuringExecution"]]:
        '''If the anti-affinity requirements specified by this field are not met at scheduling time, the pod will not be scheduled onto the node.

        If the anti-affinity requirements specified by this field cease to be met
        at some point during pod execution (e.g. due to a pod label update), the
        system may or may not try to eventually evict the pod from its node.
        When there are multiple elements, the lists of nodes corresponding to each
        podAffinityTerm are intersected, i.e. all terms must be satisfied.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAntiAffinity#requiredDuringSchedulingIgnoredDuringExecution
        '''
        result = self._values.get("required_during_scheduling_ignored_during_execution")
        return typing.cast(typing.Optional[typing.List["ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAntiAffinityRequiredDuringSchedulingIgnoredDuringExecution"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAntiAffinity(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iocert-manageracme.ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecution",
    jsii_struct_bases=[],
    name_mapping={"pod_affinity_term": "podAffinityTerm", "weight": "weight"},
)
class ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecution:
    def __init__(
        self,
        *,
        pod_affinity_term: typing.Union["ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTerm", typing.Dict[builtins.str, typing.Any]],
        weight: jsii.Number,
    ) -> None:
        '''The weights of all of the matched WeightedPodAffinityTerm fields are added per-node to find the most preferred node(s).

        :param pod_affinity_term: Required. A pod affinity term, associated with the corresponding weight.
        :param weight: weight associated with matching the corresponding podAffinityTerm, in the range 1-100.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecution
        '''
        if isinstance(pod_affinity_term, dict):
            pod_affinity_term = ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTerm(**pod_affinity_term)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__caf64271ddf4c65ce163505f701aae487abf905c8be5402aa19837ef861506e3)
            check_type(argname="argument pod_affinity_term", value=pod_affinity_term, expected_type=type_hints["pod_affinity_term"])
            check_type(argname="argument weight", value=weight, expected_type=type_hints["weight"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "pod_affinity_term": pod_affinity_term,
            "weight": weight,
        }

    @builtins.property
    def pod_affinity_term(
        self,
    ) -> "ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTerm":
        '''Required.

        A pod affinity term, associated with the corresponding weight.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecution#podAffinityTerm
        '''
        result = self._values.get("pod_affinity_term")
        assert result is not None, "Required property 'pod_affinity_term' is missing"
        return typing.cast("ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTerm", result)

    @builtins.property
    def weight(self) -> jsii.Number:
        '''weight associated with matching the corresponding podAffinityTerm, in the range 1-100.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecution#weight
        '''
        result = self._values.get("weight")
        assert result is not None, "Required property 'weight' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecution(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iocert-manageracme.ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTerm",
    jsii_struct_bases=[],
    name_mapping={
        "topology_key": "topologyKey",
        "label_selector": "labelSelector",
        "match_label_keys": "matchLabelKeys",
        "mismatch_label_keys": "mismatchLabelKeys",
        "namespaces": "namespaces",
        "namespace_selector": "namespaceSelector",
    },
)
class ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTerm:
    def __init__(
        self,
        *,
        topology_key: builtins.str,
        label_selector: typing.Optional[typing.Union["ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermLabelSelector", typing.Dict[builtins.str, typing.Any]]] = None,
        match_label_keys: typing.Optional[typing.Sequence[builtins.str]] = None,
        mismatch_label_keys: typing.Optional[typing.Sequence[builtins.str]] = None,
        namespaces: typing.Optional[typing.Sequence[builtins.str]] = None,
        namespace_selector: typing.Optional[typing.Union["ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermNamespaceSelector", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''Required.

        A pod affinity term, associated with the corresponding weight.

        :param topology_key: This pod should be co-located (affinity) or not co-located (anti-affinity) with the pods matching the labelSelector in the specified namespaces, where co-located is defined as running on a node whose value of the label with key topologyKey matches that of any node on which any of the selected pods is running. Empty topologyKey is not allowed.
        :param label_selector: A label query over a set of resources, in this case pods. If it's null, this PodAffinityTerm matches with no Pods.
        :param match_label_keys: MatchLabelKeys is a set of pod label keys to select which pods will be taken into consideration. The keys are used to lookup values from the incoming pod labels, those key-value labels are merged with ``labelSelector`` as ``key in (value)`` to select the group of existing pods which pods will be taken into consideration for the incoming pod's pod (anti) affinity. Keys that don't exist in the incoming pod labels will be ignored. The default value is empty. The same key is forbidden to exist in both matchLabelKeys and labelSelector. Also, matchLabelKeys cannot be set when labelSelector isn't set. This is a beta field and requires enabling MatchLabelKeysInPodAffinity feature gate (enabled by default).
        :param mismatch_label_keys: MismatchLabelKeys is a set of pod label keys to select which pods will be taken into consideration. The keys are used to lookup values from the incoming pod labels, those key-value labels are merged with ``labelSelector`` as ``key notin (value)`` to select the group of existing pods which pods will be taken into consideration for the incoming pod's pod (anti) affinity. Keys that don't exist in the incoming pod labels will be ignored. The default value is empty. The same key is forbidden to exist in both mismatchLabelKeys and labelSelector. Also, mismatchLabelKeys cannot be set when labelSelector isn't set. This is a beta field and requires enabling MatchLabelKeysInPodAffinity feature gate (enabled by default).
        :param namespaces: namespaces specifies a static list of namespace names that the term applies to. The term is applied to the union of the namespaces listed in this field and the ones selected by namespaceSelector. null or empty namespaces list and null namespaceSelector means "this pod's namespace".
        :param namespace_selector: A label query over the set of namespaces that the term applies to. The term is applied to the union of the namespaces selected by this field and the ones listed in the namespaces field. null selector and null or empty namespaces list means "this pod's namespace". An empty selector ({}) matches all namespaces.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTerm
        '''
        if isinstance(label_selector, dict):
            label_selector = ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermLabelSelector(**label_selector)
        if isinstance(namespace_selector, dict):
            namespace_selector = ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermNamespaceSelector(**namespace_selector)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__efea315c17146562a7f2d978d5b23be4a6f09632f6586a75fade75848fe13e76)
            check_type(argname="argument topology_key", value=topology_key, expected_type=type_hints["topology_key"])
            check_type(argname="argument label_selector", value=label_selector, expected_type=type_hints["label_selector"])
            check_type(argname="argument match_label_keys", value=match_label_keys, expected_type=type_hints["match_label_keys"])
            check_type(argname="argument mismatch_label_keys", value=mismatch_label_keys, expected_type=type_hints["mismatch_label_keys"])
            check_type(argname="argument namespaces", value=namespaces, expected_type=type_hints["namespaces"])
            check_type(argname="argument namespace_selector", value=namespace_selector, expected_type=type_hints["namespace_selector"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "topology_key": topology_key,
        }
        if label_selector is not None:
            self._values["label_selector"] = label_selector
        if match_label_keys is not None:
            self._values["match_label_keys"] = match_label_keys
        if mismatch_label_keys is not None:
            self._values["mismatch_label_keys"] = mismatch_label_keys
        if namespaces is not None:
            self._values["namespaces"] = namespaces
        if namespace_selector is not None:
            self._values["namespace_selector"] = namespace_selector

    @builtins.property
    def topology_key(self) -> builtins.str:
        '''This pod should be co-located (affinity) or not co-located (anti-affinity) with the pods matching the labelSelector in the specified namespaces, where co-located is defined as running on a node whose value of the label with key topologyKey matches that of any node on which any of the selected pods is running.

        Empty topologyKey is not allowed.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTerm#topologyKey
        '''
        result = self._values.get("topology_key")
        assert result is not None, "Required property 'topology_key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def label_selector(
        self,
    ) -> typing.Optional["ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermLabelSelector"]:
        '''A label query over a set of resources, in this case pods.

        If it's null, this PodAffinityTerm matches with no Pods.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTerm#labelSelector
        '''
        result = self._values.get("label_selector")
        return typing.cast(typing.Optional["ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermLabelSelector"], result)

    @builtins.property
    def match_label_keys(self) -> typing.Optional[typing.List[builtins.str]]:
        '''MatchLabelKeys is a set of pod label keys to select which pods will be taken into consideration.

        The keys are used to lookup values from the
        incoming pod labels, those key-value labels are merged with ``labelSelector`` as ``key in (value)``
        to select the group of existing pods which pods will be taken into consideration
        for the incoming pod's pod (anti) affinity. Keys that don't exist in the incoming
        pod labels will be ignored. The default value is empty.
        The same key is forbidden to exist in both matchLabelKeys and labelSelector.
        Also, matchLabelKeys cannot be set when labelSelector isn't set.
        This is a beta field and requires enabling MatchLabelKeysInPodAffinity feature gate (enabled by default).

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTerm#matchLabelKeys
        '''
        result = self._values.get("match_label_keys")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def mismatch_label_keys(self) -> typing.Optional[typing.List[builtins.str]]:
        '''MismatchLabelKeys is a set of pod label keys to select which pods will be taken into consideration.

        The keys are used to lookup values from the
        incoming pod labels, those key-value labels are merged with ``labelSelector`` as ``key notin (value)``
        to select the group of existing pods which pods will be taken into consideration
        for the incoming pod's pod (anti) affinity. Keys that don't exist in the incoming
        pod labels will be ignored. The default value is empty.
        The same key is forbidden to exist in both mismatchLabelKeys and labelSelector.
        Also, mismatchLabelKeys cannot be set when labelSelector isn't set.
        This is a beta field and requires enabling MatchLabelKeysInPodAffinity feature gate (enabled by default).

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTerm#mismatchLabelKeys
        '''
        result = self._values.get("mismatch_label_keys")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def namespaces(self) -> typing.Optional[typing.List[builtins.str]]:
        '''namespaces specifies a static list of namespace names that the term applies to.

        The term is applied to the union of the namespaces listed in this field
        and the ones selected by namespaceSelector.
        null or empty namespaces list and null namespaceSelector means "this pod's namespace".

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTerm#namespaces
        '''
        result = self._values.get("namespaces")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def namespace_selector(
        self,
    ) -> typing.Optional["ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermNamespaceSelector"]:
        '''A label query over the set of namespaces that the term applies to.

        The term is applied to the union of the namespaces selected by this field
        and the ones listed in the namespaces field.
        null selector and null or empty namespaces list means "this pod's namespace".
        An empty selector ({}) matches all namespaces.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTerm#namespaceSelector
        '''
        result = self._values.get("namespace_selector")
        return typing.cast(typing.Optional["ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermNamespaceSelector"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTerm(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iocert-manageracme.ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermLabelSelector",
    jsii_struct_bases=[],
    name_mapping={
        "match_expressions": "matchExpressions",
        "match_labels": "matchLabels",
    },
)
class ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermLabelSelector:
    def __init__(
        self,
        *,
        match_expressions: typing.Optional[typing.Sequence[typing.Union["ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermLabelSelectorMatchExpressions", typing.Dict[builtins.str, typing.Any]]]] = None,
        match_labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''A label query over a set of resources, in this case pods.

        If it's null, this PodAffinityTerm matches with no Pods.

        :param match_expressions: matchExpressions is a list of label selector requirements. The requirements are ANDed.
        :param match_labels: matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermLabelSelector
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a3258a46b4863c0aae4b2e584094c63f36c1155c4e7b7177eaeb2e0037f27d64)
            check_type(argname="argument match_expressions", value=match_expressions, expected_type=type_hints["match_expressions"])
            check_type(argname="argument match_labels", value=match_labels, expected_type=type_hints["match_labels"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if match_expressions is not None:
            self._values["match_expressions"] = match_expressions
        if match_labels is not None:
            self._values["match_labels"] = match_labels

    @builtins.property
    def match_expressions(
        self,
    ) -> typing.Optional[typing.List["ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermLabelSelectorMatchExpressions"]]:
        '''matchExpressions is a list of label selector requirements.

        The requirements are ANDed.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermLabelSelector#matchExpressions
        '''
        result = self._values.get("match_expressions")
        return typing.cast(typing.Optional[typing.List["ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermLabelSelectorMatchExpressions"]], result)

    @builtins.property
    def match_labels(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''matchLabels is a map of {key,value} pairs.

        A single {key,value} in the matchLabels
        map is equivalent to an element of matchExpressions, whose key field is "key", the
        operator is "In", and the values array contains only "value". The requirements are ANDed.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermLabelSelector#matchLabels
        '''
        result = self._values.get("match_labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermLabelSelector(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iocert-manageracme.ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermLabelSelectorMatchExpressions",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "operator": "operator", "values": "values"},
)
class ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermLabelSelectorMatchExpressions:
    def __init__(
        self,
        *,
        key: builtins.str,
        operator: builtins.str,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''A label selector requirement is a selector that contains values, a key, and an operator that relates the key and values.

        :param key: key is the label key that the selector applies to.
        :param operator: operator represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist.
        :param values: values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermLabelSelectorMatchExpressions
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__da3c5c9e940a92a70700ce6652dfc1df28b6234bc6bd9c87468832e1c6cf7fc2)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "key": key,
            "operator": operator,
        }
        if values is not None:
            self._values["values"] = values

    @builtins.property
    def key(self) -> builtins.str:
        '''key is the label key that the selector applies to.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermLabelSelectorMatchExpressions#key
        '''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def operator(self) -> builtins.str:
        '''operator represents a key's relationship to a set of values.

        Valid operators are In, NotIn, Exists and DoesNotExist.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermLabelSelectorMatchExpressions#operator
        '''
        result = self._values.get("operator")
        assert result is not None, "Required property 'operator' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''values is an array of string values.

        If the operator is In or NotIn,
        the values array must be non-empty. If the operator is Exists or DoesNotExist,
        the values array must be empty. This array is replaced during a strategic
        merge patch.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermLabelSelectorMatchExpressions#values
        '''
        result = self._values.get("values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermLabelSelectorMatchExpressions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iocert-manageracme.ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermNamespaceSelector",
    jsii_struct_bases=[],
    name_mapping={
        "match_expressions": "matchExpressions",
        "match_labels": "matchLabels",
    },
)
class ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermNamespaceSelector:
    def __init__(
        self,
        *,
        match_expressions: typing.Optional[typing.Sequence[typing.Union["ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermNamespaceSelectorMatchExpressions", typing.Dict[builtins.str, typing.Any]]]] = None,
        match_labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''A label query over the set of namespaces that the term applies to.

        The term is applied to the union of the namespaces selected by this field
        and the ones listed in the namespaces field.
        null selector and null or empty namespaces list means "this pod's namespace".
        An empty selector ({}) matches all namespaces.

        :param match_expressions: matchExpressions is a list of label selector requirements. The requirements are ANDed.
        :param match_labels: matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermNamespaceSelector
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1dafa47e3ae28aa2e49438db504569e19ff0353bf20b48d9b358f76152ede14e)
            check_type(argname="argument match_expressions", value=match_expressions, expected_type=type_hints["match_expressions"])
            check_type(argname="argument match_labels", value=match_labels, expected_type=type_hints["match_labels"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if match_expressions is not None:
            self._values["match_expressions"] = match_expressions
        if match_labels is not None:
            self._values["match_labels"] = match_labels

    @builtins.property
    def match_expressions(
        self,
    ) -> typing.Optional[typing.List["ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermNamespaceSelectorMatchExpressions"]]:
        '''matchExpressions is a list of label selector requirements.

        The requirements are ANDed.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermNamespaceSelector#matchExpressions
        '''
        result = self._values.get("match_expressions")
        return typing.cast(typing.Optional[typing.List["ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermNamespaceSelectorMatchExpressions"]], result)

    @builtins.property
    def match_labels(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''matchLabels is a map of {key,value} pairs.

        A single {key,value} in the matchLabels
        map is equivalent to an element of matchExpressions, whose key field is "key", the
        operator is "In", and the values array contains only "value". The requirements are ANDed.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermNamespaceSelector#matchLabels
        '''
        result = self._values.get("match_labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermNamespaceSelector(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iocert-manageracme.ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermNamespaceSelectorMatchExpressions",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "operator": "operator", "values": "values"},
)
class ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermNamespaceSelectorMatchExpressions:
    def __init__(
        self,
        *,
        key: builtins.str,
        operator: builtins.str,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''A label selector requirement is a selector that contains values, a key, and an operator that relates the key and values.

        :param key: key is the label key that the selector applies to.
        :param operator: operator represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist.
        :param values: values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermNamespaceSelectorMatchExpressions
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__22676c608c81dfc67ddc1ba10dfef17466834dc5487cd8ee9552020a48000a8b)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "key": key,
            "operator": operator,
        }
        if values is not None:
            self._values["values"] = values

    @builtins.property
    def key(self) -> builtins.str:
        '''key is the label key that the selector applies to.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermNamespaceSelectorMatchExpressions#key
        '''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def operator(self) -> builtins.str:
        '''operator represents a key's relationship to a set of values.

        Valid operators are In, NotIn, Exists and DoesNotExist.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermNamespaceSelectorMatchExpressions#operator
        '''
        result = self._values.get("operator")
        assert result is not None, "Required property 'operator' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''values is an array of string values.

        If the operator is In or NotIn,
        the values array must be non-empty. If the operator is Exists or DoesNotExist,
        the values array must be empty. This array is replaced during a strategic
        merge patch.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermNamespaceSelectorMatchExpressions#values
        '''
        result = self._values.get("values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermNamespaceSelectorMatchExpressions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iocert-manageracme.ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAntiAffinityRequiredDuringSchedulingIgnoredDuringExecution",
    jsii_struct_bases=[],
    name_mapping={
        "topology_key": "topologyKey",
        "label_selector": "labelSelector",
        "match_label_keys": "matchLabelKeys",
        "mismatch_label_keys": "mismatchLabelKeys",
        "namespaces": "namespaces",
        "namespace_selector": "namespaceSelector",
    },
)
class ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAntiAffinityRequiredDuringSchedulingIgnoredDuringExecution:
    def __init__(
        self,
        *,
        topology_key: builtins.str,
        label_selector: typing.Optional[typing.Union["ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAntiAffinityRequiredDuringSchedulingIgnoredDuringExecutionLabelSelector", typing.Dict[builtins.str, typing.Any]]] = None,
        match_label_keys: typing.Optional[typing.Sequence[builtins.str]] = None,
        mismatch_label_keys: typing.Optional[typing.Sequence[builtins.str]] = None,
        namespaces: typing.Optional[typing.Sequence[builtins.str]] = None,
        namespace_selector: typing.Optional[typing.Union["ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAntiAffinityRequiredDuringSchedulingIgnoredDuringExecutionNamespaceSelector", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''Defines a set of pods (namely those matching the labelSelector relative to the given namespace(s)) that this pod should be co-located (affinity) or not co-located (anti-affinity) with, where co-located is defined as running on a node whose value of the label with key  matches that of any node on which a pod of the set of pods is running.

        :param topology_key: This pod should be co-located (affinity) or not co-located (anti-affinity) with the pods matching the labelSelector in the specified namespaces, where co-located is defined as running on a node whose value of the label with key topologyKey matches that of any node on which any of the selected pods is running. Empty topologyKey is not allowed.
        :param label_selector: A label query over a set of resources, in this case pods. If it's null, this PodAffinityTerm matches with no Pods.
        :param match_label_keys: MatchLabelKeys is a set of pod label keys to select which pods will be taken into consideration. The keys are used to lookup values from the incoming pod labels, those key-value labels are merged with ``labelSelector`` as ``key in (value)`` to select the group of existing pods which pods will be taken into consideration for the incoming pod's pod (anti) affinity. Keys that don't exist in the incoming pod labels will be ignored. The default value is empty. The same key is forbidden to exist in both matchLabelKeys and labelSelector. Also, matchLabelKeys cannot be set when labelSelector isn't set. This is a beta field and requires enabling MatchLabelKeysInPodAffinity feature gate (enabled by default).
        :param mismatch_label_keys: MismatchLabelKeys is a set of pod label keys to select which pods will be taken into consideration. The keys are used to lookup values from the incoming pod labels, those key-value labels are merged with ``labelSelector`` as ``key notin (value)`` to select the group of existing pods which pods will be taken into consideration for the incoming pod's pod (anti) affinity. Keys that don't exist in the incoming pod labels will be ignored. The default value is empty. The same key is forbidden to exist in both mismatchLabelKeys and labelSelector. Also, mismatchLabelKeys cannot be set when labelSelector isn't set. This is a beta field and requires enabling MatchLabelKeysInPodAffinity feature gate (enabled by default).
        :param namespaces: namespaces specifies a static list of namespace names that the term applies to. The term is applied to the union of the namespaces listed in this field and the ones selected by namespaceSelector. null or empty namespaces list and null namespaceSelector means "this pod's namespace".
        :param namespace_selector: A label query over the set of namespaces that the term applies to. The term is applied to the union of the namespaces selected by this field and the ones listed in the namespaces field. null selector and null or empty namespaces list means "this pod's namespace". An empty selector ({}) matches all namespaces.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAntiAffinityRequiredDuringSchedulingIgnoredDuringExecution
        '''
        if isinstance(label_selector, dict):
            label_selector = ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAntiAffinityRequiredDuringSchedulingIgnoredDuringExecutionLabelSelector(**label_selector)
        if isinstance(namespace_selector, dict):
            namespace_selector = ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAntiAffinityRequiredDuringSchedulingIgnoredDuringExecutionNamespaceSelector(**namespace_selector)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d64c6177fb32631798d50ded8740d04b67729a8cefeac433bdaec79ab1704df8)
            check_type(argname="argument topology_key", value=topology_key, expected_type=type_hints["topology_key"])
            check_type(argname="argument label_selector", value=label_selector, expected_type=type_hints["label_selector"])
            check_type(argname="argument match_label_keys", value=match_label_keys, expected_type=type_hints["match_label_keys"])
            check_type(argname="argument mismatch_label_keys", value=mismatch_label_keys, expected_type=type_hints["mismatch_label_keys"])
            check_type(argname="argument namespaces", value=namespaces, expected_type=type_hints["namespaces"])
            check_type(argname="argument namespace_selector", value=namespace_selector, expected_type=type_hints["namespace_selector"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "topology_key": topology_key,
        }
        if label_selector is not None:
            self._values["label_selector"] = label_selector
        if match_label_keys is not None:
            self._values["match_label_keys"] = match_label_keys
        if mismatch_label_keys is not None:
            self._values["mismatch_label_keys"] = mismatch_label_keys
        if namespaces is not None:
            self._values["namespaces"] = namespaces
        if namespace_selector is not None:
            self._values["namespace_selector"] = namespace_selector

    @builtins.property
    def topology_key(self) -> builtins.str:
        '''This pod should be co-located (affinity) or not co-located (anti-affinity) with the pods matching the labelSelector in the specified namespaces, where co-located is defined as running on a node whose value of the label with key topologyKey matches that of any node on which any of the selected pods is running.

        Empty topologyKey is not allowed.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAntiAffinityRequiredDuringSchedulingIgnoredDuringExecution#topologyKey
        '''
        result = self._values.get("topology_key")
        assert result is not None, "Required property 'topology_key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def label_selector(
        self,
    ) -> typing.Optional["ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAntiAffinityRequiredDuringSchedulingIgnoredDuringExecutionLabelSelector"]:
        '''A label query over a set of resources, in this case pods.

        If it's null, this PodAffinityTerm matches with no Pods.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAntiAffinityRequiredDuringSchedulingIgnoredDuringExecution#labelSelector
        '''
        result = self._values.get("label_selector")
        return typing.cast(typing.Optional["ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAntiAffinityRequiredDuringSchedulingIgnoredDuringExecutionLabelSelector"], result)

    @builtins.property
    def match_label_keys(self) -> typing.Optional[typing.List[builtins.str]]:
        '''MatchLabelKeys is a set of pod label keys to select which pods will be taken into consideration.

        The keys are used to lookup values from the
        incoming pod labels, those key-value labels are merged with ``labelSelector`` as ``key in (value)``
        to select the group of existing pods which pods will be taken into consideration
        for the incoming pod's pod (anti) affinity. Keys that don't exist in the incoming
        pod labels will be ignored. The default value is empty.
        The same key is forbidden to exist in both matchLabelKeys and labelSelector.
        Also, matchLabelKeys cannot be set when labelSelector isn't set.
        This is a beta field and requires enabling MatchLabelKeysInPodAffinity feature gate (enabled by default).

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAntiAffinityRequiredDuringSchedulingIgnoredDuringExecution#matchLabelKeys
        '''
        result = self._values.get("match_label_keys")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def mismatch_label_keys(self) -> typing.Optional[typing.List[builtins.str]]:
        '''MismatchLabelKeys is a set of pod label keys to select which pods will be taken into consideration.

        The keys are used to lookup values from the
        incoming pod labels, those key-value labels are merged with ``labelSelector`` as ``key notin (value)``
        to select the group of existing pods which pods will be taken into consideration
        for the incoming pod's pod (anti) affinity. Keys that don't exist in the incoming
        pod labels will be ignored. The default value is empty.
        The same key is forbidden to exist in both mismatchLabelKeys and labelSelector.
        Also, mismatchLabelKeys cannot be set when labelSelector isn't set.
        This is a beta field and requires enabling MatchLabelKeysInPodAffinity feature gate (enabled by default).

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAntiAffinityRequiredDuringSchedulingIgnoredDuringExecution#mismatchLabelKeys
        '''
        result = self._values.get("mismatch_label_keys")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def namespaces(self) -> typing.Optional[typing.List[builtins.str]]:
        '''namespaces specifies a static list of namespace names that the term applies to.

        The term is applied to the union of the namespaces listed in this field
        and the ones selected by namespaceSelector.
        null or empty namespaces list and null namespaceSelector means "this pod's namespace".

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAntiAffinityRequiredDuringSchedulingIgnoredDuringExecution#namespaces
        '''
        result = self._values.get("namespaces")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def namespace_selector(
        self,
    ) -> typing.Optional["ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAntiAffinityRequiredDuringSchedulingIgnoredDuringExecutionNamespaceSelector"]:
        '''A label query over the set of namespaces that the term applies to.

        The term is applied to the union of the namespaces selected by this field
        and the ones listed in the namespaces field.
        null selector and null or empty namespaces list means "this pod's namespace".
        An empty selector ({}) matches all namespaces.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAntiAffinityRequiredDuringSchedulingIgnoredDuringExecution#namespaceSelector
        '''
        result = self._values.get("namespace_selector")
        return typing.cast(typing.Optional["ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAntiAffinityRequiredDuringSchedulingIgnoredDuringExecutionNamespaceSelector"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAntiAffinityRequiredDuringSchedulingIgnoredDuringExecution(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iocert-manageracme.ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAntiAffinityRequiredDuringSchedulingIgnoredDuringExecutionLabelSelector",
    jsii_struct_bases=[],
    name_mapping={
        "match_expressions": "matchExpressions",
        "match_labels": "matchLabels",
    },
)
class ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAntiAffinityRequiredDuringSchedulingIgnoredDuringExecutionLabelSelector:
    def __init__(
        self,
        *,
        match_expressions: typing.Optional[typing.Sequence[typing.Union["ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAntiAffinityRequiredDuringSchedulingIgnoredDuringExecutionLabelSelectorMatchExpressions", typing.Dict[builtins.str, typing.Any]]]] = None,
        match_labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''A label query over a set of resources, in this case pods.

        If it's null, this PodAffinityTerm matches with no Pods.

        :param match_expressions: matchExpressions is a list of label selector requirements. The requirements are ANDed.
        :param match_labels: matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAntiAffinityRequiredDuringSchedulingIgnoredDuringExecutionLabelSelector
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5c0d04ab4767ae5d7bc00b0f6356530fff84c0c6b1cc2e8a7f27dafefa5f30cf)
            check_type(argname="argument match_expressions", value=match_expressions, expected_type=type_hints["match_expressions"])
            check_type(argname="argument match_labels", value=match_labels, expected_type=type_hints["match_labels"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if match_expressions is not None:
            self._values["match_expressions"] = match_expressions
        if match_labels is not None:
            self._values["match_labels"] = match_labels

    @builtins.property
    def match_expressions(
        self,
    ) -> typing.Optional[typing.List["ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAntiAffinityRequiredDuringSchedulingIgnoredDuringExecutionLabelSelectorMatchExpressions"]]:
        '''matchExpressions is a list of label selector requirements.

        The requirements are ANDed.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAntiAffinityRequiredDuringSchedulingIgnoredDuringExecutionLabelSelector#matchExpressions
        '''
        result = self._values.get("match_expressions")
        return typing.cast(typing.Optional[typing.List["ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAntiAffinityRequiredDuringSchedulingIgnoredDuringExecutionLabelSelectorMatchExpressions"]], result)

    @builtins.property
    def match_labels(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''matchLabels is a map of {key,value} pairs.

        A single {key,value} in the matchLabels
        map is equivalent to an element of matchExpressions, whose key field is "key", the
        operator is "In", and the values array contains only "value". The requirements are ANDed.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAntiAffinityRequiredDuringSchedulingIgnoredDuringExecutionLabelSelector#matchLabels
        '''
        result = self._values.get("match_labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAntiAffinityRequiredDuringSchedulingIgnoredDuringExecutionLabelSelector(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iocert-manageracme.ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAntiAffinityRequiredDuringSchedulingIgnoredDuringExecutionLabelSelectorMatchExpressions",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "operator": "operator", "values": "values"},
)
class ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAntiAffinityRequiredDuringSchedulingIgnoredDuringExecutionLabelSelectorMatchExpressions:
    def __init__(
        self,
        *,
        key: builtins.str,
        operator: builtins.str,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''A label selector requirement is a selector that contains values, a key, and an operator that relates the key and values.

        :param key: key is the label key that the selector applies to.
        :param operator: operator represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist.
        :param values: values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAntiAffinityRequiredDuringSchedulingIgnoredDuringExecutionLabelSelectorMatchExpressions
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__605f7a2e21f1815bdadc0b035cc430154ac81373f1b08a942aa87c8f9982b068)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "key": key,
            "operator": operator,
        }
        if values is not None:
            self._values["values"] = values

    @builtins.property
    def key(self) -> builtins.str:
        '''key is the label key that the selector applies to.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAntiAffinityRequiredDuringSchedulingIgnoredDuringExecutionLabelSelectorMatchExpressions#key
        '''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def operator(self) -> builtins.str:
        '''operator represents a key's relationship to a set of values.

        Valid operators are In, NotIn, Exists and DoesNotExist.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAntiAffinityRequiredDuringSchedulingIgnoredDuringExecutionLabelSelectorMatchExpressions#operator
        '''
        result = self._values.get("operator")
        assert result is not None, "Required property 'operator' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''values is an array of string values.

        If the operator is In or NotIn,
        the values array must be non-empty. If the operator is Exists or DoesNotExist,
        the values array must be empty. This array is replaced during a strategic
        merge patch.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAntiAffinityRequiredDuringSchedulingIgnoredDuringExecutionLabelSelectorMatchExpressions#values
        '''
        result = self._values.get("values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAntiAffinityRequiredDuringSchedulingIgnoredDuringExecutionLabelSelectorMatchExpressions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iocert-manageracme.ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAntiAffinityRequiredDuringSchedulingIgnoredDuringExecutionNamespaceSelector",
    jsii_struct_bases=[],
    name_mapping={
        "match_expressions": "matchExpressions",
        "match_labels": "matchLabels",
    },
)
class ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAntiAffinityRequiredDuringSchedulingIgnoredDuringExecutionNamespaceSelector:
    def __init__(
        self,
        *,
        match_expressions: typing.Optional[typing.Sequence[typing.Union["ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAntiAffinityRequiredDuringSchedulingIgnoredDuringExecutionNamespaceSelectorMatchExpressions", typing.Dict[builtins.str, typing.Any]]]] = None,
        match_labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''A label query over the set of namespaces that the term applies to.

        The term is applied to the union of the namespaces selected by this field
        and the ones listed in the namespaces field.
        null selector and null or empty namespaces list means "this pod's namespace".
        An empty selector ({}) matches all namespaces.

        :param match_expressions: matchExpressions is a list of label selector requirements. The requirements are ANDed.
        :param match_labels: matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAntiAffinityRequiredDuringSchedulingIgnoredDuringExecutionNamespaceSelector
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4d615d9445aa34aff5d26ef06f5f0ddcd4fda89fab861a2738a18e7b6e261731)
            check_type(argname="argument match_expressions", value=match_expressions, expected_type=type_hints["match_expressions"])
            check_type(argname="argument match_labels", value=match_labels, expected_type=type_hints["match_labels"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if match_expressions is not None:
            self._values["match_expressions"] = match_expressions
        if match_labels is not None:
            self._values["match_labels"] = match_labels

    @builtins.property
    def match_expressions(
        self,
    ) -> typing.Optional[typing.List["ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAntiAffinityRequiredDuringSchedulingIgnoredDuringExecutionNamespaceSelectorMatchExpressions"]]:
        '''matchExpressions is a list of label selector requirements.

        The requirements are ANDed.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAntiAffinityRequiredDuringSchedulingIgnoredDuringExecutionNamespaceSelector#matchExpressions
        '''
        result = self._values.get("match_expressions")
        return typing.cast(typing.Optional[typing.List["ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAntiAffinityRequiredDuringSchedulingIgnoredDuringExecutionNamespaceSelectorMatchExpressions"]], result)

    @builtins.property
    def match_labels(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''matchLabels is a map of {key,value} pairs.

        A single {key,value} in the matchLabels
        map is equivalent to an element of matchExpressions, whose key field is "key", the
        operator is "In", and the values array contains only "value". The requirements are ANDed.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAntiAffinityRequiredDuringSchedulingIgnoredDuringExecutionNamespaceSelector#matchLabels
        '''
        result = self._values.get("match_labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAntiAffinityRequiredDuringSchedulingIgnoredDuringExecutionNamespaceSelector(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iocert-manageracme.ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAntiAffinityRequiredDuringSchedulingIgnoredDuringExecutionNamespaceSelectorMatchExpressions",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "operator": "operator", "values": "values"},
)
class ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAntiAffinityRequiredDuringSchedulingIgnoredDuringExecutionNamespaceSelectorMatchExpressions:
    def __init__(
        self,
        *,
        key: builtins.str,
        operator: builtins.str,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''A label selector requirement is a selector that contains values, a key, and an operator that relates the key and values.

        :param key: key is the label key that the selector applies to.
        :param operator: operator represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist.
        :param values: values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAntiAffinityRequiredDuringSchedulingIgnoredDuringExecutionNamespaceSelectorMatchExpressions
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eaec30274d71aff89fdefaa7c67360fc2bc6c75c119a89fbaec725f5b42833d0)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "key": key,
            "operator": operator,
        }
        if values is not None:
            self._values["values"] = values

    @builtins.property
    def key(self) -> builtins.str:
        '''key is the label key that the selector applies to.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAntiAffinityRequiredDuringSchedulingIgnoredDuringExecutionNamespaceSelectorMatchExpressions#key
        '''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def operator(self) -> builtins.str:
        '''operator represents a key's relationship to a set of values.

        Valid operators are In, NotIn, Exists and DoesNotExist.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAntiAffinityRequiredDuringSchedulingIgnoredDuringExecutionNamespaceSelectorMatchExpressions#operator
        '''
        result = self._values.get("operator")
        assert result is not None, "Required property 'operator' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''values is an array of string values.

        If the operator is In or NotIn,
        the values array must be non-empty. If the operator is Exists or DoesNotExist,
        the values array must be empty. This array is replaced during a strategic
        merge patch.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAntiAffinityRequiredDuringSchedulingIgnoredDuringExecutionNamespaceSelectorMatchExpressions#values
        '''
        result = self._values.get("values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAntiAffinityRequiredDuringSchedulingIgnoredDuringExecutionNamespaceSelectorMatchExpressions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iocert-manageracme.ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecImagePullSecrets",
    jsii_struct_bases=[],
    name_mapping={"name": "name"},
)
class ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecImagePullSecrets:
    def __init__(self, *, name: typing.Optional[builtins.str] = None) -> None:
        '''LocalObjectReference contains enough information to let you locate the referenced object inside the same namespace.

        :param name: Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecImagePullSecrets
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9859fd882b5ec21ed3095e5a77d3d6269e1d3ee77a6a9dd962a9ab622821dd27)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name of the referent.

        This field is effectively required, but due to backwards compatibility is
        allowed to be empty. Instances of this type with an empty value here are
        almost certainly wrong.
        More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecImagePullSecrets#name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecImagePullSecrets(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iocert-manageracme.ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecSecurityContext",
    jsii_struct_bases=[],
    name_mapping={
        "fs_group": "fsGroup",
        "fs_group_change_policy": "fsGroupChangePolicy",
        "run_as_group": "runAsGroup",
        "run_as_non_root": "runAsNonRoot",
        "run_as_user": "runAsUser",
        "seccomp_profile": "seccompProfile",
        "se_linux_options": "seLinuxOptions",
        "supplemental_groups": "supplementalGroups",
        "sysctls": "sysctls",
    },
)
class ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecSecurityContext:
    def __init__(
        self,
        *,
        fs_group: typing.Optional[jsii.Number] = None,
        fs_group_change_policy: typing.Optional[builtins.str] = None,
        run_as_group: typing.Optional[jsii.Number] = None,
        run_as_non_root: typing.Optional[builtins.bool] = None,
        run_as_user: typing.Optional[jsii.Number] = None,
        seccomp_profile: typing.Optional[typing.Union["ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecSecurityContextSeccompProfile", typing.Dict[builtins.str, typing.Any]]] = None,
        se_linux_options: typing.Optional[typing.Union["ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecSecurityContextSeLinuxOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        supplemental_groups: typing.Optional[typing.Sequence[jsii.Number]] = None,
        sysctls: typing.Optional[typing.Sequence[typing.Union["ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecSecurityContextSysctls", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''If specified, the pod's security context.

        :param fs_group: A special supplemental group that applies to all containers in a pod. Some volume types allow the Kubelet to change the ownership of that volume to be owned by the pod: 1. The owning GID will be the FSGroup 2. The setgid bit is set (new files created in the volume will be owned by FSGroup) 3. The permission bits are OR'd with rw-rw---- If unset, the Kubelet will not modify the ownership and permissions of any volume. Note that this field cannot be set when spec.os.name is windows.
        :param fs_group_change_policy: fsGroupChangePolicy defines behavior of changing ownership and permission of the volume before being exposed inside Pod. This field will only apply to volume types which support fsGroup based ownership(and permissions). It will have no effect on ephemeral volume types such as: secret, configmaps and emptydir. Valid values are "OnRootMismatch" and "Always". If not specified, "Always" is used. Note that this field cannot be set when spec.os.name is windows.
        :param run_as_group: The GID to run the entrypoint of the container process. Uses runtime default if unset. May also be set in SecurityContext. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence for that container. Note that this field cannot be set when spec.os.name is windows.
        :param run_as_non_root: Indicates that the container must run as a non-root user. If true, the Kubelet will validate the image at runtime to ensure that it does not run as UID 0 (root) and fail to start the container if it does. If unset or false, no such validation will be performed. May also be set in SecurityContext. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.
        :param run_as_user: The UID to run the entrypoint of the container process. Defaults to user specified in image metadata if unspecified. May also be set in SecurityContext. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence for that container. Note that this field cannot be set when spec.os.name is windows. Default: user specified in image metadata if unspecified.
        :param seccomp_profile: The seccomp options to use by the containers in this pod. Note that this field cannot be set when spec.os.name is windows.
        :param se_linux_options: The SELinux context to be applied to all containers. If unspecified, the container runtime will allocate a random SELinux context for each container. May also be set in SecurityContext. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence for that container. Note that this field cannot be set when spec.os.name is windows.
        :param supplemental_groups: A list of groups applied to the first process run in each container, in addition to the container's primary GID, the fsGroup (if specified), and group memberships defined in the container image for the uid of the container process. If unspecified, no additional groups are added to any container. Note that group memberships defined in the container image for the uid of the container process are still effective, even if they are not included in this list. Note that this field cannot be set when spec.os.name is windows.
        :param sysctls: Sysctls hold a list of namespaced sysctls used for the pod. Pods with unsupported sysctls (by the container runtime) might fail to launch. Note that this field cannot be set when spec.os.name is windows.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecSecurityContext
        '''
        if isinstance(seccomp_profile, dict):
            seccomp_profile = ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecSecurityContextSeccompProfile(**seccomp_profile)
        if isinstance(se_linux_options, dict):
            se_linux_options = ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecSecurityContextSeLinuxOptions(**se_linux_options)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3382d5a17213e2c85657b289a3d23b9fe837b85499a1b07653bcf473e3edd021)
            check_type(argname="argument fs_group", value=fs_group, expected_type=type_hints["fs_group"])
            check_type(argname="argument fs_group_change_policy", value=fs_group_change_policy, expected_type=type_hints["fs_group_change_policy"])
            check_type(argname="argument run_as_group", value=run_as_group, expected_type=type_hints["run_as_group"])
            check_type(argname="argument run_as_non_root", value=run_as_non_root, expected_type=type_hints["run_as_non_root"])
            check_type(argname="argument run_as_user", value=run_as_user, expected_type=type_hints["run_as_user"])
            check_type(argname="argument seccomp_profile", value=seccomp_profile, expected_type=type_hints["seccomp_profile"])
            check_type(argname="argument se_linux_options", value=se_linux_options, expected_type=type_hints["se_linux_options"])
            check_type(argname="argument supplemental_groups", value=supplemental_groups, expected_type=type_hints["supplemental_groups"])
            check_type(argname="argument sysctls", value=sysctls, expected_type=type_hints["sysctls"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if fs_group is not None:
            self._values["fs_group"] = fs_group
        if fs_group_change_policy is not None:
            self._values["fs_group_change_policy"] = fs_group_change_policy
        if run_as_group is not None:
            self._values["run_as_group"] = run_as_group
        if run_as_non_root is not None:
            self._values["run_as_non_root"] = run_as_non_root
        if run_as_user is not None:
            self._values["run_as_user"] = run_as_user
        if seccomp_profile is not None:
            self._values["seccomp_profile"] = seccomp_profile
        if se_linux_options is not None:
            self._values["se_linux_options"] = se_linux_options
        if supplemental_groups is not None:
            self._values["supplemental_groups"] = supplemental_groups
        if sysctls is not None:
            self._values["sysctls"] = sysctls

    @builtins.property
    def fs_group(self) -> typing.Optional[jsii.Number]:
        '''A special supplemental group that applies to all containers in a pod.

        Some volume types allow the Kubelet to change the ownership of that volume
        to be owned by the pod:

        1. The owning GID will be the FSGroup
        2. The setgid bit is set (new files created in the volume will be owned by FSGroup)
        3. The permission bits are OR'd with rw-rw----

        If unset, the Kubelet will not modify the ownership and permissions of any volume.
        Note that this field cannot be set when spec.os.name is windows.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecSecurityContext#fsGroup
        '''
        result = self._values.get("fs_group")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def fs_group_change_policy(self) -> typing.Optional[builtins.str]:
        '''fsGroupChangePolicy defines behavior of changing ownership and permission of the volume before being exposed inside Pod.

        This field will only apply to
        volume types which support fsGroup based ownership(and permissions).
        It will have no effect on ephemeral volume types such as: secret, configmaps
        and emptydir.
        Valid values are "OnRootMismatch" and "Always". If not specified, "Always" is used.
        Note that this field cannot be set when spec.os.name is windows.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecSecurityContext#fsGroupChangePolicy
        '''
        result = self._values.get("fs_group_change_policy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def run_as_group(self) -> typing.Optional[jsii.Number]:
        '''The GID to run the entrypoint of the container process.

        Uses runtime default if unset.
        May also be set in SecurityContext.  If set in both SecurityContext and
        PodSecurityContext, the value specified in SecurityContext takes precedence
        for that container.
        Note that this field cannot be set when spec.os.name is windows.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecSecurityContext#runAsGroup
        '''
        result = self._values.get("run_as_group")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def run_as_non_root(self) -> typing.Optional[builtins.bool]:
        '''Indicates that the container must run as a non-root user.

        If true, the Kubelet will validate the image at runtime to ensure that it
        does not run as UID 0 (root) and fail to start the container if it does.
        If unset or false, no such validation will be performed.
        May also be set in SecurityContext.  If set in both SecurityContext and
        PodSecurityContext, the value specified in SecurityContext takes precedence.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecSecurityContext#runAsNonRoot
        '''
        result = self._values.get("run_as_non_root")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def run_as_user(self) -> typing.Optional[jsii.Number]:
        '''The UID to run the entrypoint of the container process.

        Defaults to user specified in image metadata if unspecified.
        May also be set in SecurityContext.  If set in both SecurityContext and
        PodSecurityContext, the value specified in SecurityContext takes precedence
        for that container.
        Note that this field cannot be set when spec.os.name is windows.

        :default: user specified in image metadata if unspecified.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecSecurityContext#runAsUser
        '''
        result = self._values.get("run_as_user")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def seccomp_profile(
        self,
    ) -> typing.Optional["ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecSecurityContextSeccompProfile"]:
        '''The seccomp options to use by the containers in this pod.

        Note that this field cannot be set when spec.os.name is windows.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecSecurityContext#seccompProfile
        '''
        result = self._values.get("seccomp_profile")
        return typing.cast(typing.Optional["ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecSecurityContextSeccompProfile"], result)

    @builtins.property
    def se_linux_options(
        self,
    ) -> typing.Optional["ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecSecurityContextSeLinuxOptions"]:
        '''The SELinux context to be applied to all containers.

        If unspecified, the container runtime will allocate a random SELinux context for each
        container.  May also be set in SecurityContext.  If set in
        both SecurityContext and PodSecurityContext, the value specified in SecurityContext
        takes precedence for that container.
        Note that this field cannot be set when spec.os.name is windows.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecSecurityContext#seLinuxOptions
        '''
        result = self._values.get("se_linux_options")
        return typing.cast(typing.Optional["ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecSecurityContextSeLinuxOptions"], result)

    @builtins.property
    def supplemental_groups(self) -> typing.Optional[typing.List[jsii.Number]]:
        '''A list of groups applied to the first process run in each container, in addition to the container's primary GID, the fsGroup (if specified), and group memberships defined in the container image for the uid of the container process.

        If unspecified,
        no additional groups are added to any container. Note that group memberships
        defined in the container image for the uid of the container process are still effective,
        even if they are not included in this list.
        Note that this field cannot be set when spec.os.name is windows.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecSecurityContext#supplementalGroups
        '''
        result = self._values.get("supplemental_groups")
        return typing.cast(typing.Optional[typing.List[jsii.Number]], result)

    @builtins.property
    def sysctls(
        self,
    ) -> typing.Optional[typing.List["ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecSecurityContextSysctls"]]:
        '''Sysctls hold a list of namespaced sysctls used for the pod.

        Pods with unsupported
        sysctls (by the container runtime) might fail to launch.
        Note that this field cannot be set when spec.os.name is windows.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecSecurityContext#sysctls
        '''
        result = self._values.get("sysctls")
        return typing.cast(typing.Optional[typing.List["ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecSecurityContextSysctls"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecSecurityContext(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iocert-manageracme.ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecSecurityContextSeLinuxOptions",
    jsii_struct_bases=[],
    name_mapping={"level": "level", "role": "role", "type": "type", "user": "user"},
)
class ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecSecurityContextSeLinuxOptions:
    def __init__(
        self,
        *,
        level: typing.Optional[builtins.str] = None,
        role: typing.Optional[builtins.str] = None,
        type: typing.Optional[builtins.str] = None,
        user: typing.Optional[builtins.str] = None,
    ) -> None:
        '''The SELinux context to be applied to all containers.

        If unspecified, the container runtime will allocate a random SELinux context for each
        container.  May also be set in SecurityContext.  If set in
        both SecurityContext and PodSecurityContext, the value specified in SecurityContext
        takes precedence for that container.
        Note that this field cannot be set when spec.os.name is windows.

        :param level: Level is SELinux level label that applies to the container.
        :param role: Role is a SELinux role label that applies to the container.
        :param type: Type is a SELinux type label that applies to the container.
        :param user: User is a SELinux user label that applies to the container.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecSecurityContextSeLinuxOptions
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ad6a87b1e8b45aa3e93ec6c6f6663bae7834255f279f1e579f41c481583ea512)
            check_type(argname="argument level", value=level, expected_type=type_hints["level"])
            check_type(argname="argument role", value=role, expected_type=type_hints["role"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument user", value=user, expected_type=type_hints["user"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if level is not None:
            self._values["level"] = level
        if role is not None:
            self._values["role"] = role
        if type is not None:
            self._values["type"] = type
        if user is not None:
            self._values["user"] = user

    @builtins.property
    def level(self) -> typing.Optional[builtins.str]:
        '''Level is SELinux level label that applies to the container.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecSecurityContextSeLinuxOptions#level
        '''
        result = self._values.get("level")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def role(self) -> typing.Optional[builtins.str]:
        '''Role is a SELinux role label that applies to the container.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecSecurityContextSeLinuxOptions#role
        '''
        result = self._values.get("role")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''Type is a SELinux type label that applies to the container.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecSecurityContextSeLinuxOptions#type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def user(self) -> typing.Optional[builtins.str]:
        '''User is a SELinux user label that applies to the container.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecSecurityContextSeLinuxOptions#user
        '''
        result = self._values.get("user")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecSecurityContextSeLinuxOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iocert-manageracme.ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecSecurityContextSeccompProfile",
    jsii_struct_bases=[],
    name_mapping={"type": "type", "localhost_profile": "localhostProfile"},
)
class ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecSecurityContextSeccompProfile:
    def __init__(
        self,
        *,
        type: builtins.str,
        localhost_profile: typing.Optional[builtins.str] = None,
    ) -> None:
        '''The seccomp options to use by the containers in this pod.

        Note that this field cannot be set when spec.os.name is windows.

        :param type: type indicates which kind of seccomp profile will be applied. Valid options are:. Localhost - a profile defined in a file on the node should be used. RuntimeDefault - the container runtime default profile should be used. Unconfined - no profile should be applied.
        :param localhost_profile: localhostProfile indicates a profile defined in a file on the node should be used. The profile must be preconfigured on the node to work. Must be a descending path, relative to the kubelet's configured seccomp profile location. Must be set if type is "Localhost". Must NOT be set for any other type.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecSecurityContextSeccompProfile
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__250f1451ce2065546eec63696a776116347bad21687392234bb8c9f701600e43)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument localhost_profile", value=localhost_profile, expected_type=type_hints["localhost_profile"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "type": type,
        }
        if localhost_profile is not None:
            self._values["localhost_profile"] = localhost_profile

    @builtins.property
    def type(self) -> builtins.str:
        '''type indicates which kind of seccomp profile will be applied. Valid options are:.

        Localhost - a profile defined in a file on the node should be used.
        RuntimeDefault - the container runtime default profile should be used.
        Unconfined - no profile should be applied.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecSecurityContextSeccompProfile#type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def localhost_profile(self) -> typing.Optional[builtins.str]:
        '''localhostProfile indicates a profile defined in a file on the node should be used.

        The profile must be preconfigured on the node to work.
        Must be a descending path, relative to the kubelet's configured seccomp profile location.
        Must be set if type is "Localhost". Must NOT be set for any other type.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecSecurityContextSeccompProfile#localhostProfile
        '''
        result = self._values.get("localhost_profile")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecSecurityContextSeccompProfile(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iocert-manageracme.ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecSecurityContextSysctls",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "value": "value"},
)
class ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecSecurityContextSysctls:
    def __init__(self, *, name: builtins.str, value: builtins.str) -> None:
        '''Sysctl defines a kernel parameter to be set.

        :param name: Name of a property to set.
        :param value: Value of a property to set.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecSecurityContextSysctls
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8d1f2e562b7329e2c6ba925c5bb2f341d0ec701ee3528a722df6cab2003e646d)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "value": value,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''Name of a property to set.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecSecurityContextSysctls#name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        '''Value of a property to set.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecSecurityContextSysctls#value
        '''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecSecurityContextSysctls(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iocert-manageracme.ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecTolerations",
    jsii_struct_bases=[],
    name_mapping={
        "effect": "effect",
        "key": "key",
        "operator": "operator",
        "toleration_seconds": "tolerationSeconds",
        "value": "value",
    },
)
class ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecTolerations:
    def __init__(
        self,
        *,
        effect: typing.Optional[builtins.str] = None,
        key: typing.Optional[builtins.str] = None,
        operator: typing.Optional[builtins.str] = None,
        toleration_seconds: typing.Optional[jsii.Number] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''The pod this Toleration is attached to tolerates any taint that matches the triple <key,value,effect> using the matching operator .

        :param effect: Effect indicates the taint effect to match. Empty means match all taint effects. When specified, allowed values are NoSchedule, PreferNoSchedule and NoExecute.
        :param key: Key is the taint key that the toleration applies to. Empty means match all taint keys. If the key is empty, operator must be Exists; this combination means to match all values and all keys.
        :param operator: Operator represents a key's relationship to the value. Valid operators are Exists and Equal. Defaults to Equal. Exists is equivalent to wildcard for value, so that a pod can tolerate all taints of a particular category. Default: Equal.
        :param toleration_seconds: TolerationSeconds represents the period of time the toleration (which must be of effect NoExecute, otherwise this field is ignored) tolerates the taint. By default, it is not set, which means tolerate the taint forever (do not evict). Zero and negative values will be treated as 0 (evict immediately) by the system.
        :param value: Value is the taint value the toleration matches to. If the operator is Exists, the value should be empty, otherwise just a regular string.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecTolerations
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3b197938ebc537eff86a92974f545e4f535fbe1e79f01cdfa97fcfbe8b797657)
            check_type(argname="argument effect", value=effect, expected_type=type_hints["effect"])
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
            check_type(argname="argument toleration_seconds", value=toleration_seconds, expected_type=type_hints["toleration_seconds"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if effect is not None:
            self._values["effect"] = effect
        if key is not None:
            self._values["key"] = key
        if operator is not None:
            self._values["operator"] = operator
        if toleration_seconds is not None:
            self._values["toleration_seconds"] = toleration_seconds
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def effect(self) -> typing.Optional[builtins.str]:
        '''Effect indicates the taint effect to match.

        Empty means match all taint effects.
        When specified, allowed values are NoSchedule, PreferNoSchedule and NoExecute.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecTolerations#effect
        '''
        result = self._values.get("effect")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''Key is the taint key that the toleration applies to.

        Empty means match all taint keys.
        If the key is empty, operator must be Exists; this combination means to match all values and all keys.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecTolerations#key
        '''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def operator(self) -> typing.Optional[builtins.str]:
        '''Operator represents a key's relationship to the value.

        Valid operators are Exists and Equal. Defaults to Equal.
        Exists is equivalent to wildcard for value, so that a pod can
        tolerate all taints of a particular category.

        :default: Equal.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecTolerations#operator
        '''
        result = self._values.get("operator")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def toleration_seconds(self) -> typing.Optional[jsii.Number]:
        '''TolerationSeconds represents the period of time the toleration (which must be of effect NoExecute, otherwise this field is ignored) tolerates the taint.

        By default,
        it is not set, which means tolerate the taint forever (do not evict). Zero and
        negative values will be treated as 0 (evict immediately) by the system.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecTolerations#tolerationSeconds
        '''
        result = self._values.get("toleration_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''Value is the taint value the toleration matches to.

        If the operator is Exists, the value should be empty, otherwise just a regular string.

        :schema: ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecTolerations#value
        '''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecTolerations(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iocert-manageracme.ChallengeSpecSolverHttp01Ingress",
    jsii_struct_bases=[],
    name_mapping={
        "class_": "class",
        "ingress_class_name": "ingressClassName",
        "ingress_template": "ingressTemplate",
        "name": "name",
        "pod_template": "podTemplate",
        "service_type": "serviceType",
    },
)
class ChallengeSpecSolverHttp01Ingress:
    def __init__(
        self,
        *,
        class_: typing.Optional[builtins.str] = None,
        ingress_class_name: typing.Optional[builtins.str] = None,
        ingress_template: typing.Optional[typing.Union["ChallengeSpecSolverHttp01IngressIngressTemplate", typing.Dict[builtins.str, typing.Any]]] = None,
        name: typing.Optional[builtins.str] = None,
        pod_template: typing.Optional[typing.Union["ChallengeSpecSolverHttp01IngressPodTemplate", typing.Dict[builtins.str, typing.Any]]] = None,
        service_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''The ingress based HTTP01 challenge solver will solve challenges by creating or modifying Ingress resources in order to route requests for '/.well-known/acme-challenge/XYZ' to 'challenge solver' pods that are provisioned by cert-manager for each Challenge to be completed.

        :param class_: This field configures the annotation ``kubernetes.io/ingress.class`` when creating Ingress resources to solve ACME challenges that use this challenge solver. Only one of ``class``, ``name`` or ``ingressClassName`` may be specified.
        :param ingress_class_name: This field configures the field ``ingressClassName`` on the created Ingress resources used to solve ACME challenges that use this challenge solver. This is the recommended way of configuring the ingress class. Only one of ``class``, ``name`` or ``ingressClassName`` may be specified.
        :param ingress_template: Optional ingress template used to configure the ACME challenge solver ingress used for HTTP01 challenges.
        :param name: The name of the ingress resource that should have ACME challenge solving routes inserted into it in order to solve HTTP01 challenges. This is typically used in conjunction with ingress controllers like ingress-gce, which maintains a 1:1 mapping between external IPs and ingress resources. Only one of ``class``, ``name`` or ``ingressClassName`` may be specified.
        :param pod_template: Optional pod template used to configure the ACME challenge solver pods used for HTTP01 challenges.
        :param service_type: Optional service type for Kubernetes solver service. Supported values are NodePort or ClusterIP. If unset, defaults to NodePort.

        :schema: ChallengeSpecSolverHttp01Ingress
        '''
        if isinstance(ingress_template, dict):
            ingress_template = ChallengeSpecSolverHttp01IngressIngressTemplate(**ingress_template)
        if isinstance(pod_template, dict):
            pod_template = ChallengeSpecSolverHttp01IngressPodTemplate(**pod_template)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__408732626e682c629a101bb800fe202e2f00a46a57820a3b4a379d59f996eb25)
            check_type(argname="argument class_", value=class_, expected_type=type_hints["class_"])
            check_type(argname="argument ingress_class_name", value=ingress_class_name, expected_type=type_hints["ingress_class_name"])
            check_type(argname="argument ingress_template", value=ingress_template, expected_type=type_hints["ingress_template"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument pod_template", value=pod_template, expected_type=type_hints["pod_template"])
            check_type(argname="argument service_type", value=service_type, expected_type=type_hints["service_type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if class_ is not None:
            self._values["class_"] = class_
        if ingress_class_name is not None:
            self._values["ingress_class_name"] = ingress_class_name
        if ingress_template is not None:
            self._values["ingress_template"] = ingress_template
        if name is not None:
            self._values["name"] = name
        if pod_template is not None:
            self._values["pod_template"] = pod_template
        if service_type is not None:
            self._values["service_type"] = service_type

    @builtins.property
    def class_(self) -> typing.Optional[builtins.str]:
        '''This field configures the annotation ``kubernetes.io/ingress.class`` when creating Ingress resources to solve ACME challenges that use this challenge solver. Only one of ``class``, ``name`` or ``ingressClassName`` may be specified.

        :schema: ChallengeSpecSolverHttp01Ingress#class
        '''
        result = self._values.get("class_")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ingress_class_name(self) -> typing.Optional[builtins.str]:
        '''This field configures the field ``ingressClassName`` on the created Ingress resources used to solve ACME challenges that use this challenge solver.

        This is the recommended way of configuring the ingress class. Only one of
        ``class``, ``name`` or ``ingressClassName`` may be specified.

        :schema: ChallengeSpecSolverHttp01Ingress#ingressClassName
        '''
        result = self._values.get("ingress_class_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ingress_template(
        self,
    ) -> typing.Optional["ChallengeSpecSolverHttp01IngressIngressTemplate"]:
        '''Optional ingress template used to configure the ACME challenge solver ingress used for HTTP01 challenges.

        :schema: ChallengeSpecSolverHttp01Ingress#ingressTemplate
        '''
        result = self._values.get("ingress_template")
        return typing.cast(typing.Optional["ChallengeSpecSolverHttp01IngressIngressTemplate"], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the ingress resource that should have ACME challenge solving routes inserted into it in order to solve HTTP01 challenges.

        This is typically used in conjunction with ingress controllers like
        ingress-gce, which maintains a 1:1 mapping between external IPs and
        ingress resources. Only one of ``class``, ``name`` or ``ingressClassName`` may
        be specified.

        :schema: ChallengeSpecSolverHttp01Ingress#name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def pod_template(
        self,
    ) -> typing.Optional["ChallengeSpecSolverHttp01IngressPodTemplate"]:
        '''Optional pod template used to configure the ACME challenge solver pods used for HTTP01 challenges.

        :schema: ChallengeSpecSolverHttp01Ingress#podTemplate
        '''
        result = self._values.get("pod_template")
        return typing.cast(typing.Optional["ChallengeSpecSolverHttp01IngressPodTemplate"], result)

    @builtins.property
    def service_type(self) -> typing.Optional[builtins.str]:
        '''Optional service type for Kubernetes solver service.

        Supported values
        are NodePort or ClusterIP. If unset, defaults to NodePort.

        :schema: ChallengeSpecSolverHttp01Ingress#serviceType
        '''
        result = self._values.get("service_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ChallengeSpecSolverHttp01Ingress(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iocert-manageracme.ChallengeSpecSolverHttp01IngressIngressTemplate",
    jsii_struct_bases=[],
    name_mapping={"metadata": "metadata"},
)
class ChallengeSpecSolverHttp01IngressIngressTemplate:
    def __init__(
        self,
        *,
        metadata: typing.Optional[typing.Union["ChallengeSpecSolverHttp01IngressIngressTemplateMetadata", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''Optional ingress template used to configure the ACME challenge solver ingress used for HTTP01 challenges.

        :param metadata: ObjectMeta overrides for the ingress used to solve HTTP01 challenges. Only the 'labels' and 'annotations' fields may be set. If labels or annotations overlap with in-built values, the values here will override the in-built values.

        :schema: ChallengeSpecSolverHttp01IngressIngressTemplate
        '''
        if isinstance(metadata, dict):
            metadata = ChallengeSpecSolverHttp01IngressIngressTemplateMetadata(**metadata)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e3e7fc9ed653a05e7787d3a770b22522625722d61652450d252dcd22dcc878db)
            check_type(argname="argument metadata", value=metadata, expected_type=type_hints["metadata"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if metadata is not None:
            self._values["metadata"] = metadata

    @builtins.property
    def metadata(
        self,
    ) -> typing.Optional["ChallengeSpecSolverHttp01IngressIngressTemplateMetadata"]:
        '''ObjectMeta overrides for the ingress used to solve HTTP01 challenges.

        Only the 'labels' and 'annotations' fields may be set.
        If labels or annotations overlap with in-built values, the values here
        will override the in-built values.

        :schema: ChallengeSpecSolverHttp01IngressIngressTemplate#metadata
        '''
        result = self._values.get("metadata")
        return typing.cast(typing.Optional["ChallengeSpecSolverHttp01IngressIngressTemplateMetadata"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ChallengeSpecSolverHttp01IngressIngressTemplate(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iocert-manageracme.ChallengeSpecSolverHttp01IngressIngressTemplateMetadata",
    jsii_struct_bases=[],
    name_mapping={"annotations": "annotations", "labels": "labels"},
)
class ChallengeSpecSolverHttp01IngressIngressTemplateMetadata:
    def __init__(
        self,
        *,
        annotations: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''ObjectMeta overrides for the ingress used to solve HTTP01 challenges.

        Only the 'labels' and 'annotations' fields may be set.
        If labels or annotations overlap with in-built values, the values here
        will override the in-built values.

        :param annotations: Annotations that should be added to the created ACME HTTP01 solver ingress.
        :param labels: Labels that should be added to the created ACME HTTP01 solver ingress.

        :schema: ChallengeSpecSolverHttp01IngressIngressTemplateMetadata
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0e064f5873f9bd1176ec8fe22b1734b5db2747a93d1f4354ff953eb33f40f701)
            check_type(argname="argument annotations", value=annotations, expected_type=type_hints["annotations"])
            check_type(argname="argument labels", value=labels, expected_type=type_hints["labels"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if annotations is not None:
            self._values["annotations"] = annotations
        if labels is not None:
            self._values["labels"] = labels

    @builtins.property
    def annotations(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Annotations that should be added to the created ACME HTTP01 solver ingress.

        :schema: ChallengeSpecSolverHttp01IngressIngressTemplateMetadata#annotations
        '''
        result = self._values.get("annotations")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def labels(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Labels that should be added to the created ACME HTTP01 solver ingress.

        :schema: ChallengeSpecSolverHttp01IngressIngressTemplateMetadata#labels
        '''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ChallengeSpecSolverHttp01IngressIngressTemplateMetadata(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iocert-manageracme.ChallengeSpecSolverHttp01IngressPodTemplate",
    jsii_struct_bases=[],
    name_mapping={"metadata": "metadata", "spec": "spec"},
)
class ChallengeSpecSolverHttp01IngressPodTemplate:
    def __init__(
        self,
        *,
        metadata: typing.Optional[typing.Union["ChallengeSpecSolverHttp01IngressPodTemplateMetadata", typing.Dict[builtins.str, typing.Any]]] = None,
        spec: typing.Optional[typing.Union["ChallengeSpecSolverHttp01IngressPodTemplateSpec", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''Optional pod template used to configure the ACME challenge solver pods used for HTTP01 challenges.

        :param metadata: ObjectMeta overrides for the pod used to solve HTTP01 challenges. Only the 'labels' and 'annotations' fields may be set. If labels or annotations overlap with in-built values, the values here will override the in-built values.
        :param spec: PodSpec defines overrides for the HTTP01 challenge solver pod. Check ACMEChallengeSolverHTTP01IngressPodSpec to find out currently supported fields. All other fields will be ignored.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplate
        '''
        if isinstance(metadata, dict):
            metadata = ChallengeSpecSolverHttp01IngressPodTemplateMetadata(**metadata)
        if isinstance(spec, dict):
            spec = ChallengeSpecSolverHttp01IngressPodTemplateSpec(**spec)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6d69d3251d18e75d85c237247ddf685a9af0fa179ff6e1cad64c1fa285f48355)
            check_type(argname="argument metadata", value=metadata, expected_type=type_hints["metadata"])
            check_type(argname="argument spec", value=spec, expected_type=type_hints["spec"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if metadata is not None:
            self._values["metadata"] = metadata
        if spec is not None:
            self._values["spec"] = spec

    @builtins.property
    def metadata(
        self,
    ) -> typing.Optional["ChallengeSpecSolverHttp01IngressPodTemplateMetadata"]:
        '''ObjectMeta overrides for the pod used to solve HTTP01 challenges.

        Only the 'labels' and 'annotations' fields may be set.
        If labels or annotations overlap with in-built values, the values here
        will override the in-built values.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplate#metadata
        '''
        result = self._values.get("metadata")
        return typing.cast(typing.Optional["ChallengeSpecSolverHttp01IngressPodTemplateMetadata"], result)

    @builtins.property
    def spec(
        self,
    ) -> typing.Optional["ChallengeSpecSolverHttp01IngressPodTemplateSpec"]:
        '''PodSpec defines overrides for the HTTP01 challenge solver pod.

        Check ACMEChallengeSolverHTTP01IngressPodSpec to find out currently supported fields.
        All other fields will be ignored.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplate#spec
        '''
        result = self._values.get("spec")
        return typing.cast(typing.Optional["ChallengeSpecSolverHttp01IngressPodTemplateSpec"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ChallengeSpecSolverHttp01IngressPodTemplate(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iocert-manageracme.ChallengeSpecSolverHttp01IngressPodTemplateMetadata",
    jsii_struct_bases=[],
    name_mapping={"annotations": "annotations", "labels": "labels"},
)
class ChallengeSpecSolverHttp01IngressPodTemplateMetadata:
    def __init__(
        self,
        *,
        annotations: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''ObjectMeta overrides for the pod used to solve HTTP01 challenges.

        Only the 'labels' and 'annotations' fields may be set.
        If labels or annotations overlap with in-built values, the values here
        will override the in-built values.

        :param annotations: Annotations that should be added to the created ACME HTTP01 solver pods.
        :param labels: Labels that should be added to the created ACME HTTP01 solver pods.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateMetadata
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b09908dbff5bd2f918117323927331cb51af2e6a0076610db1b1dce8b9157684)
            check_type(argname="argument annotations", value=annotations, expected_type=type_hints["annotations"])
            check_type(argname="argument labels", value=labels, expected_type=type_hints["labels"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if annotations is not None:
            self._values["annotations"] = annotations
        if labels is not None:
            self._values["labels"] = labels

    @builtins.property
    def annotations(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Annotations that should be added to the created ACME HTTP01 solver pods.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateMetadata#annotations
        '''
        result = self._values.get("annotations")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def labels(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Labels that should be added to the created ACME HTTP01 solver pods.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateMetadata#labels
        '''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ChallengeSpecSolverHttp01IngressPodTemplateMetadata(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iocert-manageracme.ChallengeSpecSolverHttp01IngressPodTemplateSpec",
    jsii_struct_bases=[],
    name_mapping={
        "affinity": "affinity",
        "image_pull_secrets": "imagePullSecrets",
        "node_selector": "nodeSelector",
        "priority_class_name": "priorityClassName",
        "security_context": "securityContext",
        "service_account_name": "serviceAccountName",
        "tolerations": "tolerations",
    },
)
class ChallengeSpecSolverHttp01IngressPodTemplateSpec:
    def __init__(
        self,
        *,
        affinity: typing.Optional[typing.Union["ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinity", typing.Dict[builtins.str, typing.Any]]] = None,
        image_pull_secrets: typing.Optional[typing.Sequence[typing.Union["ChallengeSpecSolverHttp01IngressPodTemplateSpecImagePullSecrets", typing.Dict[builtins.str, typing.Any]]]] = None,
        node_selector: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        priority_class_name: typing.Optional[builtins.str] = None,
        security_context: typing.Optional[typing.Union["ChallengeSpecSolverHttp01IngressPodTemplateSpecSecurityContext", typing.Dict[builtins.str, typing.Any]]] = None,
        service_account_name: typing.Optional[builtins.str] = None,
        tolerations: typing.Optional[typing.Sequence[typing.Union["ChallengeSpecSolverHttp01IngressPodTemplateSpecTolerations", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''PodSpec defines overrides for the HTTP01 challenge solver pod.

        Check ACMEChallengeSolverHTTP01IngressPodSpec to find out currently supported fields.
        All other fields will be ignored.

        :param affinity: If specified, the pod's scheduling constraints.
        :param image_pull_secrets: If specified, the pod's imagePullSecrets.
        :param node_selector: NodeSelector is a selector which must be true for the pod to fit on a node. Selector which must match a node's labels for the pod to be scheduled on that node. More info: https://kubernetes.io/docs/concepts/configuration/assign-pod-node/
        :param priority_class_name: If specified, the pod's priorityClassName.
        :param security_context: If specified, the pod's security context.
        :param service_account_name: If specified, the pod's service account.
        :param tolerations: If specified, the pod's tolerations.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpec
        '''
        if isinstance(affinity, dict):
            affinity = ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinity(**affinity)
        if isinstance(security_context, dict):
            security_context = ChallengeSpecSolverHttp01IngressPodTemplateSpecSecurityContext(**security_context)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c55b1852a0ce8beedd77943df68f0f11832ef840acf01cb6da63966fae9cfcf4)
            check_type(argname="argument affinity", value=affinity, expected_type=type_hints["affinity"])
            check_type(argname="argument image_pull_secrets", value=image_pull_secrets, expected_type=type_hints["image_pull_secrets"])
            check_type(argname="argument node_selector", value=node_selector, expected_type=type_hints["node_selector"])
            check_type(argname="argument priority_class_name", value=priority_class_name, expected_type=type_hints["priority_class_name"])
            check_type(argname="argument security_context", value=security_context, expected_type=type_hints["security_context"])
            check_type(argname="argument service_account_name", value=service_account_name, expected_type=type_hints["service_account_name"])
            check_type(argname="argument tolerations", value=tolerations, expected_type=type_hints["tolerations"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if affinity is not None:
            self._values["affinity"] = affinity
        if image_pull_secrets is not None:
            self._values["image_pull_secrets"] = image_pull_secrets
        if node_selector is not None:
            self._values["node_selector"] = node_selector
        if priority_class_name is not None:
            self._values["priority_class_name"] = priority_class_name
        if security_context is not None:
            self._values["security_context"] = security_context
        if service_account_name is not None:
            self._values["service_account_name"] = service_account_name
        if tolerations is not None:
            self._values["tolerations"] = tolerations

    @builtins.property
    def affinity(
        self,
    ) -> typing.Optional["ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinity"]:
        '''If specified, the pod's scheduling constraints.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpec#affinity
        '''
        result = self._values.get("affinity")
        return typing.cast(typing.Optional["ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinity"], result)

    @builtins.property
    def image_pull_secrets(
        self,
    ) -> typing.Optional[typing.List["ChallengeSpecSolverHttp01IngressPodTemplateSpecImagePullSecrets"]]:
        '''If specified, the pod's imagePullSecrets.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpec#imagePullSecrets
        '''
        result = self._values.get("image_pull_secrets")
        return typing.cast(typing.Optional[typing.List["ChallengeSpecSolverHttp01IngressPodTemplateSpecImagePullSecrets"]], result)

    @builtins.property
    def node_selector(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''NodeSelector is a selector which must be true for the pod to fit on a node.

        Selector which must match a node's labels for the pod to be scheduled on that node.
        More info: https://kubernetes.io/docs/concepts/configuration/assign-pod-node/

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpec#nodeSelector
        '''
        result = self._values.get("node_selector")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def priority_class_name(self) -> typing.Optional[builtins.str]:
        '''If specified, the pod's priorityClassName.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpec#priorityClassName
        '''
        result = self._values.get("priority_class_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def security_context(
        self,
    ) -> typing.Optional["ChallengeSpecSolverHttp01IngressPodTemplateSpecSecurityContext"]:
        '''If specified, the pod's security context.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpec#securityContext
        '''
        result = self._values.get("security_context")
        return typing.cast(typing.Optional["ChallengeSpecSolverHttp01IngressPodTemplateSpecSecurityContext"], result)

    @builtins.property
    def service_account_name(self) -> typing.Optional[builtins.str]:
        '''If specified, the pod's service account.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpec#serviceAccountName
        '''
        result = self._values.get("service_account_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tolerations(
        self,
    ) -> typing.Optional[typing.List["ChallengeSpecSolverHttp01IngressPodTemplateSpecTolerations"]]:
        '''If specified, the pod's tolerations.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpec#tolerations
        '''
        result = self._values.get("tolerations")
        return typing.cast(typing.Optional[typing.List["ChallengeSpecSolverHttp01IngressPodTemplateSpecTolerations"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ChallengeSpecSolverHttp01IngressPodTemplateSpec(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iocert-manageracme.ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinity",
    jsii_struct_bases=[],
    name_mapping={
        "node_affinity": "nodeAffinity",
        "pod_affinity": "podAffinity",
        "pod_anti_affinity": "podAntiAffinity",
    },
)
class ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinity:
    def __init__(
        self,
        *,
        node_affinity: typing.Optional[typing.Union["ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinity", typing.Dict[builtins.str, typing.Any]]] = None,
        pod_affinity: typing.Optional[typing.Union["ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinity", typing.Dict[builtins.str, typing.Any]]] = None,
        pod_anti_affinity: typing.Optional[typing.Union["ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinity", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''If specified, the pod's scheduling constraints.

        :param node_affinity: Describes node affinity scheduling rules for the pod.
        :param pod_affinity: Describes pod affinity scheduling rules (e.g. co-locate this pod in the same node, zone, etc. as some other pod(s)).
        :param pod_anti_affinity: Describes pod anti-affinity scheduling rules (e.g. avoid putting this pod in the same node, zone, etc. as some other pod(s)).

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinity
        '''
        if isinstance(node_affinity, dict):
            node_affinity = ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinity(**node_affinity)
        if isinstance(pod_affinity, dict):
            pod_affinity = ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinity(**pod_affinity)
        if isinstance(pod_anti_affinity, dict):
            pod_anti_affinity = ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinity(**pod_anti_affinity)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e4725fc235dbf7a8a04ea9bc8552fbda04f11532609b62223dc12b3ce1cfc890)
            check_type(argname="argument node_affinity", value=node_affinity, expected_type=type_hints["node_affinity"])
            check_type(argname="argument pod_affinity", value=pod_affinity, expected_type=type_hints["pod_affinity"])
            check_type(argname="argument pod_anti_affinity", value=pod_anti_affinity, expected_type=type_hints["pod_anti_affinity"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if node_affinity is not None:
            self._values["node_affinity"] = node_affinity
        if pod_affinity is not None:
            self._values["pod_affinity"] = pod_affinity
        if pod_anti_affinity is not None:
            self._values["pod_anti_affinity"] = pod_anti_affinity

    @builtins.property
    def node_affinity(
        self,
    ) -> typing.Optional["ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinity"]:
        '''Describes node affinity scheduling rules for the pod.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinity#nodeAffinity
        '''
        result = self._values.get("node_affinity")
        return typing.cast(typing.Optional["ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinity"], result)

    @builtins.property
    def pod_affinity(
        self,
    ) -> typing.Optional["ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinity"]:
        '''Describes pod affinity scheduling rules (e.g. co-locate this pod in the same node, zone, etc. as some other pod(s)).

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinity#podAffinity
        '''
        result = self._values.get("pod_affinity")
        return typing.cast(typing.Optional["ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinity"], result)

    @builtins.property
    def pod_anti_affinity(
        self,
    ) -> typing.Optional["ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinity"]:
        '''Describes pod anti-affinity scheduling rules (e.g. avoid putting this pod in the same node, zone, etc. as some other pod(s)).

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinity#podAntiAffinity
        '''
        result = self._values.get("pod_anti_affinity")
        return typing.cast(typing.Optional["ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinity"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinity(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iocert-manageracme.ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinity",
    jsii_struct_bases=[],
    name_mapping={
        "preferred_during_scheduling_ignored_during_execution": "preferredDuringSchedulingIgnoredDuringExecution",
        "required_during_scheduling_ignored_during_execution": "requiredDuringSchedulingIgnoredDuringExecution",
    },
)
class ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinity:
    def __init__(
        self,
        *,
        preferred_during_scheduling_ignored_during_execution: typing.Optional[typing.Sequence[typing.Union["ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecution", typing.Dict[builtins.str, typing.Any]]]] = None,
        required_during_scheduling_ignored_during_execution: typing.Optional[typing.Union["ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecution", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''Describes node affinity scheduling rules for the pod.

        :param preferred_during_scheduling_ignored_during_execution: The scheduler will prefer to schedule pods to nodes that satisfy the affinity expressions specified by this field, but it may choose a node that violates one or more of the expressions. The node that is most preferred is the one with the greatest sum of weights, i.e. for each node that meets all of the scheduling requirements (resource request, requiredDuringScheduling affinity expressions, etc.), compute a sum by iterating through the elements of this field and adding "weight" to the sum if the node matches the corresponding matchExpressions; the node(s) with the highest sum are the most preferred.
        :param required_during_scheduling_ignored_during_execution: If the affinity requirements specified by this field are not met at scheduling time, the pod will not be scheduled onto the node. If the affinity requirements specified by this field cease to be met at some point during pod execution (e.g. due to an update), the system may or may not try to eventually evict the pod from its node.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinity
        '''
        if isinstance(required_during_scheduling_ignored_during_execution, dict):
            required_during_scheduling_ignored_during_execution = ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecution(**required_during_scheduling_ignored_during_execution)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1f5b9eddd3e77b4926a363d5fff196640cebb824cccaa09e005aded4073b508c)
            check_type(argname="argument preferred_during_scheduling_ignored_during_execution", value=preferred_during_scheduling_ignored_during_execution, expected_type=type_hints["preferred_during_scheduling_ignored_during_execution"])
            check_type(argname="argument required_during_scheduling_ignored_during_execution", value=required_during_scheduling_ignored_during_execution, expected_type=type_hints["required_during_scheduling_ignored_during_execution"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if preferred_during_scheduling_ignored_during_execution is not None:
            self._values["preferred_during_scheduling_ignored_during_execution"] = preferred_during_scheduling_ignored_during_execution
        if required_during_scheduling_ignored_during_execution is not None:
            self._values["required_during_scheduling_ignored_during_execution"] = required_during_scheduling_ignored_during_execution

    @builtins.property
    def preferred_during_scheduling_ignored_during_execution(
        self,
    ) -> typing.Optional[typing.List["ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecution"]]:
        '''The scheduler will prefer to schedule pods to nodes that satisfy the affinity expressions specified by this field, but it may choose a node that violates one or more of the expressions.

        The node that is
        most preferred is the one with the greatest sum of weights, i.e.
        for each node that meets all of the scheduling requirements (resource
        request, requiredDuringScheduling affinity expressions, etc.),
        compute a sum by iterating through the elements of this field and adding
        "weight" to the sum if the node matches the corresponding matchExpressions; the
        node(s) with the highest sum are the most preferred.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinity#preferredDuringSchedulingIgnoredDuringExecution
        '''
        result = self._values.get("preferred_during_scheduling_ignored_during_execution")
        return typing.cast(typing.Optional[typing.List["ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecution"]], result)

    @builtins.property
    def required_during_scheduling_ignored_during_execution(
        self,
    ) -> typing.Optional["ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecution"]:
        '''If the affinity requirements specified by this field are not met at scheduling time, the pod will not be scheduled onto the node.

        If the affinity requirements specified by this field cease to be met
        at some point during pod execution (e.g. due to an update), the system
        may or may not try to eventually evict the pod from its node.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinity#requiredDuringSchedulingIgnoredDuringExecution
        '''
        result = self._values.get("required_during_scheduling_ignored_during_execution")
        return typing.cast(typing.Optional["ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecution"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinity(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iocert-manageracme.ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecution",
    jsii_struct_bases=[],
    name_mapping={"preference": "preference", "weight": "weight"},
)
class ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecution:
    def __init__(
        self,
        *,
        preference: typing.Union["ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecutionPreference", typing.Dict[builtins.str, typing.Any]],
        weight: jsii.Number,
    ) -> None:
        '''An empty preferred scheduling term matches all objects with implicit weight 0 (i.e. it's a no-op). A null preferred scheduling term matches no objects (i.e. is also a no-op).

        :param preference: A node selector term, associated with the corresponding weight.
        :param weight: Weight associated with matching the corresponding nodeSelectorTerm, in the range 1-100.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecution
        '''
        if isinstance(preference, dict):
            preference = ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecutionPreference(**preference)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__46f7952cde067868c2b74413c601e3a91c0574bb4fcd5db8a424d552d033a047)
            check_type(argname="argument preference", value=preference, expected_type=type_hints["preference"])
            check_type(argname="argument weight", value=weight, expected_type=type_hints["weight"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "preference": preference,
            "weight": weight,
        }

    @builtins.property
    def preference(
        self,
    ) -> "ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecutionPreference":
        '''A node selector term, associated with the corresponding weight.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecution#preference
        '''
        result = self._values.get("preference")
        assert result is not None, "Required property 'preference' is missing"
        return typing.cast("ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecutionPreference", result)

    @builtins.property
    def weight(self) -> jsii.Number:
        '''Weight associated with matching the corresponding nodeSelectorTerm, in the range 1-100.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecution#weight
        '''
        result = self._values.get("weight")
        assert result is not None, "Required property 'weight' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecution(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iocert-manageracme.ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecutionPreference",
    jsii_struct_bases=[],
    name_mapping={
        "match_expressions": "matchExpressions",
        "match_fields": "matchFields",
    },
)
class ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecutionPreference:
    def __init__(
        self,
        *,
        match_expressions: typing.Optional[typing.Sequence[typing.Union["ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecutionPreferenceMatchExpressions", typing.Dict[builtins.str, typing.Any]]]] = None,
        match_fields: typing.Optional[typing.Sequence[typing.Union["ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecutionPreferenceMatchFields", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''A node selector term, associated with the corresponding weight.

        :param match_expressions: A list of node selector requirements by node's labels.
        :param match_fields: A list of node selector requirements by node's fields.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecutionPreference
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fd8289b175672663b8617afe183d823b765fdbc317bd817d4dddefef7714236c)
            check_type(argname="argument match_expressions", value=match_expressions, expected_type=type_hints["match_expressions"])
            check_type(argname="argument match_fields", value=match_fields, expected_type=type_hints["match_fields"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if match_expressions is not None:
            self._values["match_expressions"] = match_expressions
        if match_fields is not None:
            self._values["match_fields"] = match_fields

    @builtins.property
    def match_expressions(
        self,
    ) -> typing.Optional[typing.List["ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecutionPreferenceMatchExpressions"]]:
        '''A list of node selector requirements by node's labels.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecutionPreference#matchExpressions
        '''
        result = self._values.get("match_expressions")
        return typing.cast(typing.Optional[typing.List["ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecutionPreferenceMatchExpressions"]], result)

    @builtins.property
    def match_fields(
        self,
    ) -> typing.Optional[typing.List["ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecutionPreferenceMatchFields"]]:
        '''A list of node selector requirements by node's fields.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecutionPreference#matchFields
        '''
        result = self._values.get("match_fields")
        return typing.cast(typing.Optional[typing.List["ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecutionPreferenceMatchFields"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecutionPreference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iocert-manageracme.ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecutionPreferenceMatchExpressions",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "operator": "operator", "values": "values"},
)
class ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecutionPreferenceMatchExpressions:
    def __init__(
        self,
        *,
        key: builtins.str,
        operator: builtins.str,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''A node selector requirement is a selector that contains values, a key, and an operator that relates the key and values.

        :param key: The label key that the selector applies to.
        :param operator: Represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists, DoesNotExist. Gt, and Lt.
        :param values: An array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. If the operator is Gt or Lt, the values array must have a single element, which will be interpreted as an integer. This array is replaced during a strategic merge patch.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecutionPreferenceMatchExpressions
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3db3beed886a79a61590ea1dc6f3ba8a17ae215c05e802628e2d0bc5dab95c11)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "key": key,
            "operator": operator,
        }
        if values is not None:
            self._values["values"] = values

    @builtins.property
    def key(self) -> builtins.str:
        '''The label key that the selector applies to.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecutionPreferenceMatchExpressions#key
        '''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def operator(self) -> builtins.str:
        '''Represents a key's relationship to a set of values.

        Valid operators are In, NotIn, Exists, DoesNotExist. Gt, and Lt.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecutionPreferenceMatchExpressions#operator
        '''
        result = self._values.get("operator")
        assert result is not None, "Required property 'operator' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''An array of string values.

        If the operator is In or NotIn,
        the values array must be non-empty. If the operator is Exists or DoesNotExist,
        the values array must be empty. If the operator is Gt or Lt, the values
        array must have a single element, which will be interpreted as an integer.
        This array is replaced during a strategic merge patch.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecutionPreferenceMatchExpressions#values
        '''
        result = self._values.get("values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecutionPreferenceMatchExpressions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iocert-manageracme.ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecutionPreferenceMatchFields",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "operator": "operator", "values": "values"},
)
class ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecutionPreferenceMatchFields:
    def __init__(
        self,
        *,
        key: builtins.str,
        operator: builtins.str,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''A node selector requirement is a selector that contains values, a key, and an operator that relates the key and values.

        :param key: The label key that the selector applies to.
        :param operator: Represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists, DoesNotExist. Gt, and Lt.
        :param values: An array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. If the operator is Gt or Lt, the values array must have a single element, which will be interpreted as an integer. This array is replaced during a strategic merge patch.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecutionPreferenceMatchFields
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__795b6506b645f122ce26f5df4f33c5305a512cc4287b2e88611b07a3fe81d766)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "key": key,
            "operator": operator,
        }
        if values is not None:
            self._values["values"] = values

    @builtins.property
    def key(self) -> builtins.str:
        '''The label key that the selector applies to.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecutionPreferenceMatchFields#key
        '''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def operator(self) -> builtins.str:
        '''Represents a key's relationship to a set of values.

        Valid operators are In, NotIn, Exists, DoesNotExist. Gt, and Lt.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecutionPreferenceMatchFields#operator
        '''
        result = self._values.get("operator")
        assert result is not None, "Required property 'operator' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''An array of string values.

        If the operator is In or NotIn,
        the values array must be non-empty. If the operator is Exists or DoesNotExist,
        the values array must be empty. If the operator is Gt or Lt, the values
        array must have a single element, which will be interpreted as an integer.
        This array is replaced during a strategic merge patch.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecutionPreferenceMatchFields#values
        '''
        result = self._values.get("values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecutionPreferenceMatchFields(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iocert-manageracme.ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecution",
    jsii_struct_bases=[],
    name_mapping={"node_selector_terms": "nodeSelectorTerms"},
)
class ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecution:
    def __init__(
        self,
        *,
        node_selector_terms: typing.Sequence[typing.Union["ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionNodeSelectorTerms", typing.Dict[builtins.str, typing.Any]]],
    ) -> None:
        '''If the affinity requirements specified by this field are not met at scheduling time, the pod will not be scheduled onto the node.

        If the affinity requirements specified by this field cease to be met
        at some point during pod execution (e.g. due to an update), the system
        may or may not try to eventually evict the pod from its node.

        :param node_selector_terms: Required. A list of node selector terms. The terms are ORed.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecution
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__161051c4f4dd22a6804aaa5a717f810d1bc6a9623f9b80215cd98626da6170bf)
            check_type(argname="argument node_selector_terms", value=node_selector_terms, expected_type=type_hints["node_selector_terms"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "node_selector_terms": node_selector_terms,
        }

    @builtins.property
    def node_selector_terms(
        self,
    ) -> typing.List["ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionNodeSelectorTerms"]:
        '''Required.

        A list of node selector terms. The terms are ORed.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecution#nodeSelectorTerms
        '''
        result = self._values.get("node_selector_terms")
        assert result is not None, "Required property 'node_selector_terms' is missing"
        return typing.cast(typing.List["ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionNodeSelectorTerms"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecution(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iocert-manageracme.ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionNodeSelectorTerms",
    jsii_struct_bases=[],
    name_mapping={
        "match_expressions": "matchExpressions",
        "match_fields": "matchFields",
    },
)
class ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionNodeSelectorTerms:
    def __init__(
        self,
        *,
        match_expressions: typing.Optional[typing.Sequence[typing.Union["ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionNodeSelectorTermsMatchExpressions", typing.Dict[builtins.str, typing.Any]]]] = None,
        match_fields: typing.Optional[typing.Sequence[typing.Union["ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionNodeSelectorTermsMatchFields", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''A null or empty node selector term matches no objects.

        The requirements of
        them are ANDed.
        The TopologySelectorTerm type implements a subset of the NodeSelectorTerm.

        :param match_expressions: A list of node selector requirements by node's labels.
        :param match_fields: A list of node selector requirements by node's fields.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionNodeSelectorTerms
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b744f19a967cad64d04088cea822de7b5236126d5b57c0961e26cb1d21bcdce7)
            check_type(argname="argument match_expressions", value=match_expressions, expected_type=type_hints["match_expressions"])
            check_type(argname="argument match_fields", value=match_fields, expected_type=type_hints["match_fields"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if match_expressions is not None:
            self._values["match_expressions"] = match_expressions
        if match_fields is not None:
            self._values["match_fields"] = match_fields

    @builtins.property
    def match_expressions(
        self,
    ) -> typing.Optional[typing.List["ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionNodeSelectorTermsMatchExpressions"]]:
        '''A list of node selector requirements by node's labels.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionNodeSelectorTerms#matchExpressions
        '''
        result = self._values.get("match_expressions")
        return typing.cast(typing.Optional[typing.List["ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionNodeSelectorTermsMatchExpressions"]], result)

    @builtins.property
    def match_fields(
        self,
    ) -> typing.Optional[typing.List["ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionNodeSelectorTermsMatchFields"]]:
        '''A list of node selector requirements by node's fields.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionNodeSelectorTerms#matchFields
        '''
        result = self._values.get("match_fields")
        return typing.cast(typing.Optional[typing.List["ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionNodeSelectorTermsMatchFields"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionNodeSelectorTerms(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iocert-manageracme.ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionNodeSelectorTermsMatchExpressions",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "operator": "operator", "values": "values"},
)
class ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionNodeSelectorTermsMatchExpressions:
    def __init__(
        self,
        *,
        key: builtins.str,
        operator: builtins.str,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''A node selector requirement is a selector that contains values, a key, and an operator that relates the key and values.

        :param key: The label key that the selector applies to.
        :param operator: Represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists, DoesNotExist. Gt, and Lt.
        :param values: An array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. If the operator is Gt or Lt, the values array must have a single element, which will be interpreted as an integer. This array is replaced during a strategic merge patch.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionNodeSelectorTermsMatchExpressions
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6983dcff128ed3db81d6133320b7ab2bce7a7d2d9b0eca6033a4c057659d2eec)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "key": key,
            "operator": operator,
        }
        if values is not None:
            self._values["values"] = values

    @builtins.property
    def key(self) -> builtins.str:
        '''The label key that the selector applies to.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionNodeSelectorTermsMatchExpressions#key
        '''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def operator(self) -> builtins.str:
        '''Represents a key's relationship to a set of values.

        Valid operators are In, NotIn, Exists, DoesNotExist. Gt, and Lt.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionNodeSelectorTermsMatchExpressions#operator
        '''
        result = self._values.get("operator")
        assert result is not None, "Required property 'operator' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''An array of string values.

        If the operator is In or NotIn,
        the values array must be non-empty. If the operator is Exists or DoesNotExist,
        the values array must be empty. If the operator is Gt or Lt, the values
        array must have a single element, which will be interpreted as an integer.
        This array is replaced during a strategic merge patch.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionNodeSelectorTermsMatchExpressions#values
        '''
        result = self._values.get("values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionNodeSelectorTermsMatchExpressions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iocert-manageracme.ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionNodeSelectorTermsMatchFields",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "operator": "operator", "values": "values"},
)
class ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionNodeSelectorTermsMatchFields:
    def __init__(
        self,
        *,
        key: builtins.str,
        operator: builtins.str,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''A node selector requirement is a selector that contains values, a key, and an operator that relates the key and values.

        :param key: The label key that the selector applies to.
        :param operator: Represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists, DoesNotExist. Gt, and Lt.
        :param values: An array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. If the operator is Gt or Lt, the values array must have a single element, which will be interpreted as an integer. This array is replaced during a strategic merge patch.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionNodeSelectorTermsMatchFields
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ec159c62ca76f76cd8fee949b1ba7bc2f20c4ffa2206f2385331a25e79aa8c6a)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "key": key,
            "operator": operator,
        }
        if values is not None:
            self._values["values"] = values

    @builtins.property
    def key(self) -> builtins.str:
        '''The label key that the selector applies to.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionNodeSelectorTermsMatchFields#key
        '''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def operator(self) -> builtins.str:
        '''Represents a key's relationship to a set of values.

        Valid operators are In, NotIn, Exists, DoesNotExist. Gt, and Lt.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionNodeSelectorTermsMatchFields#operator
        '''
        result = self._values.get("operator")
        assert result is not None, "Required property 'operator' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''An array of string values.

        If the operator is In or NotIn,
        the values array must be non-empty. If the operator is Exists or DoesNotExist,
        the values array must be empty. If the operator is Gt or Lt, the values
        array must have a single element, which will be interpreted as an integer.
        This array is replaced during a strategic merge patch.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionNodeSelectorTermsMatchFields#values
        '''
        result = self._values.get("values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionNodeSelectorTermsMatchFields(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iocert-manageracme.ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinity",
    jsii_struct_bases=[],
    name_mapping={
        "preferred_during_scheduling_ignored_during_execution": "preferredDuringSchedulingIgnoredDuringExecution",
        "required_during_scheduling_ignored_during_execution": "requiredDuringSchedulingIgnoredDuringExecution",
    },
)
class ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinity:
    def __init__(
        self,
        *,
        preferred_during_scheduling_ignored_during_execution: typing.Optional[typing.Sequence[typing.Union["ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecution", typing.Dict[builtins.str, typing.Any]]]] = None,
        required_during_scheduling_ignored_during_execution: typing.Optional[typing.Sequence[typing.Union["ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityRequiredDuringSchedulingIgnoredDuringExecution", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Describes pod affinity scheduling rules (e.g. co-locate this pod in the same node, zone, etc. as some other pod(s)).

        :param preferred_during_scheduling_ignored_during_execution: The scheduler will prefer to schedule pods to nodes that satisfy the affinity expressions specified by this field, but it may choose a node that violates one or more of the expressions. The node that is most preferred is the one with the greatest sum of weights, i.e. for each node that meets all of the scheduling requirements (resource request, requiredDuringScheduling affinity expressions, etc.), compute a sum by iterating through the elements of this field and adding "weight" to the sum if the node has pods which matches the corresponding podAffinityTerm; the node(s) with the highest sum are the most preferred.
        :param required_during_scheduling_ignored_during_execution: If the affinity requirements specified by this field are not met at scheduling time, the pod will not be scheduled onto the node. If the affinity requirements specified by this field cease to be met at some point during pod execution (e.g. due to a pod label update), the system may or may not try to eventually evict the pod from its node. When there are multiple elements, the lists of nodes corresponding to each podAffinityTerm are intersected, i.e. all terms must be satisfied.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinity
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eb2c0c7fa056016c7433535606c9091ee315abf2497dcd74dcd1cd9e1db0353a)
            check_type(argname="argument preferred_during_scheduling_ignored_during_execution", value=preferred_during_scheduling_ignored_during_execution, expected_type=type_hints["preferred_during_scheduling_ignored_during_execution"])
            check_type(argname="argument required_during_scheduling_ignored_during_execution", value=required_during_scheduling_ignored_during_execution, expected_type=type_hints["required_during_scheduling_ignored_during_execution"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if preferred_during_scheduling_ignored_during_execution is not None:
            self._values["preferred_during_scheduling_ignored_during_execution"] = preferred_during_scheduling_ignored_during_execution
        if required_during_scheduling_ignored_during_execution is not None:
            self._values["required_during_scheduling_ignored_during_execution"] = required_during_scheduling_ignored_during_execution

    @builtins.property
    def preferred_during_scheduling_ignored_during_execution(
        self,
    ) -> typing.Optional[typing.List["ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecution"]]:
        '''The scheduler will prefer to schedule pods to nodes that satisfy the affinity expressions specified by this field, but it may choose a node that violates one or more of the expressions.

        The node that is
        most preferred is the one with the greatest sum of weights, i.e.
        for each node that meets all of the scheduling requirements (resource
        request, requiredDuringScheduling affinity expressions, etc.),
        compute a sum by iterating through the elements of this field and adding
        "weight" to the sum if the node has pods which matches the corresponding podAffinityTerm; the
        node(s) with the highest sum are the most preferred.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinity#preferredDuringSchedulingIgnoredDuringExecution
        '''
        result = self._values.get("preferred_during_scheduling_ignored_during_execution")
        return typing.cast(typing.Optional[typing.List["ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecution"]], result)

    @builtins.property
    def required_during_scheduling_ignored_during_execution(
        self,
    ) -> typing.Optional[typing.List["ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityRequiredDuringSchedulingIgnoredDuringExecution"]]:
        '''If the affinity requirements specified by this field are not met at scheduling time, the pod will not be scheduled onto the node.

        If the affinity requirements specified by this field cease to be met
        at some point during pod execution (e.g. due to a pod label update), the
        system may or may not try to eventually evict the pod from its node.
        When there are multiple elements, the lists of nodes corresponding to each
        podAffinityTerm are intersected, i.e. all terms must be satisfied.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinity#requiredDuringSchedulingIgnoredDuringExecution
        '''
        result = self._values.get("required_during_scheduling_ignored_during_execution")
        return typing.cast(typing.Optional[typing.List["ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityRequiredDuringSchedulingIgnoredDuringExecution"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinity(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iocert-manageracme.ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecution",
    jsii_struct_bases=[],
    name_mapping={"pod_affinity_term": "podAffinityTerm", "weight": "weight"},
)
class ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecution:
    def __init__(
        self,
        *,
        pod_affinity_term: typing.Union["ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTerm", typing.Dict[builtins.str, typing.Any]],
        weight: jsii.Number,
    ) -> None:
        '''The weights of all of the matched WeightedPodAffinityTerm fields are added per-node to find the most preferred node(s).

        :param pod_affinity_term: Required. A pod affinity term, associated with the corresponding weight.
        :param weight: weight associated with matching the corresponding podAffinityTerm, in the range 1-100.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecution
        '''
        if isinstance(pod_affinity_term, dict):
            pod_affinity_term = ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTerm(**pod_affinity_term)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__02b63a56c28d75f58aaa104f0e3f3907fd21e796c71bbba401591c1d5c53b4a8)
            check_type(argname="argument pod_affinity_term", value=pod_affinity_term, expected_type=type_hints["pod_affinity_term"])
            check_type(argname="argument weight", value=weight, expected_type=type_hints["weight"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "pod_affinity_term": pod_affinity_term,
            "weight": weight,
        }

    @builtins.property
    def pod_affinity_term(
        self,
    ) -> "ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTerm":
        '''Required.

        A pod affinity term, associated with the corresponding weight.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecution#podAffinityTerm
        '''
        result = self._values.get("pod_affinity_term")
        assert result is not None, "Required property 'pod_affinity_term' is missing"
        return typing.cast("ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTerm", result)

    @builtins.property
    def weight(self) -> jsii.Number:
        '''weight associated with matching the corresponding podAffinityTerm, in the range 1-100.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecution#weight
        '''
        result = self._values.get("weight")
        assert result is not None, "Required property 'weight' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecution(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iocert-manageracme.ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTerm",
    jsii_struct_bases=[],
    name_mapping={
        "topology_key": "topologyKey",
        "label_selector": "labelSelector",
        "match_label_keys": "matchLabelKeys",
        "mismatch_label_keys": "mismatchLabelKeys",
        "namespaces": "namespaces",
        "namespace_selector": "namespaceSelector",
    },
)
class ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTerm:
    def __init__(
        self,
        *,
        topology_key: builtins.str,
        label_selector: typing.Optional[typing.Union["ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermLabelSelector", typing.Dict[builtins.str, typing.Any]]] = None,
        match_label_keys: typing.Optional[typing.Sequence[builtins.str]] = None,
        mismatch_label_keys: typing.Optional[typing.Sequence[builtins.str]] = None,
        namespaces: typing.Optional[typing.Sequence[builtins.str]] = None,
        namespace_selector: typing.Optional[typing.Union["ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermNamespaceSelector", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''Required.

        A pod affinity term, associated with the corresponding weight.

        :param topology_key: This pod should be co-located (affinity) or not co-located (anti-affinity) with the pods matching the labelSelector in the specified namespaces, where co-located is defined as running on a node whose value of the label with key topologyKey matches that of any node on which any of the selected pods is running. Empty topologyKey is not allowed.
        :param label_selector: A label query over a set of resources, in this case pods. If it's null, this PodAffinityTerm matches with no Pods.
        :param match_label_keys: MatchLabelKeys is a set of pod label keys to select which pods will be taken into consideration. The keys are used to lookup values from the incoming pod labels, those key-value labels are merged with ``labelSelector`` as ``key in (value)`` to select the group of existing pods which pods will be taken into consideration for the incoming pod's pod (anti) affinity. Keys that don't exist in the incoming pod labels will be ignored. The default value is empty. The same key is forbidden to exist in both matchLabelKeys and labelSelector. Also, matchLabelKeys cannot be set when labelSelector isn't set. This is a beta field and requires enabling MatchLabelKeysInPodAffinity feature gate (enabled by default).
        :param mismatch_label_keys: MismatchLabelKeys is a set of pod label keys to select which pods will be taken into consideration. The keys are used to lookup values from the incoming pod labels, those key-value labels are merged with ``labelSelector`` as ``key notin (value)`` to select the group of existing pods which pods will be taken into consideration for the incoming pod's pod (anti) affinity. Keys that don't exist in the incoming pod labels will be ignored. The default value is empty. The same key is forbidden to exist in both mismatchLabelKeys and labelSelector. Also, mismatchLabelKeys cannot be set when labelSelector isn't set. This is a beta field and requires enabling MatchLabelKeysInPodAffinity feature gate (enabled by default).
        :param namespaces: namespaces specifies a static list of namespace names that the term applies to. The term is applied to the union of the namespaces listed in this field and the ones selected by namespaceSelector. null or empty namespaces list and null namespaceSelector means "this pod's namespace".
        :param namespace_selector: A label query over the set of namespaces that the term applies to. The term is applied to the union of the namespaces selected by this field and the ones listed in the namespaces field. null selector and null or empty namespaces list means "this pod's namespace". An empty selector ({}) matches all namespaces.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTerm
        '''
        if isinstance(label_selector, dict):
            label_selector = ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermLabelSelector(**label_selector)
        if isinstance(namespace_selector, dict):
            namespace_selector = ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermNamespaceSelector(**namespace_selector)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__14510f593855c5c591882bd8aa55dcc3d74603e3aee3f5eb618c657e5137d3cf)
            check_type(argname="argument topology_key", value=topology_key, expected_type=type_hints["topology_key"])
            check_type(argname="argument label_selector", value=label_selector, expected_type=type_hints["label_selector"])
            check_type(argname="argument match_label_keys", value=match_label_keys, expected_type=type_hints["match_label_keys"])
            check_type(argname="argument mismatch_label_keys", value=mismatch_label_keys, expected_type=type_hints["mismatch_label_keys"])
            check_type(argname="argument namespaces", value=namespaces, expected_type=type_hints["namespaces"])
            check_type(argname="argument namespace_selector", value=namespace_selector, expected_type=type_hints["namespace_selector"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "topology_key": topology_key,
        }
        if label_selector is not None:
            self._values["label_selector"] = label_selector
        if match_label_keys is not None:
            self._values["match_label_keys"] = match_label_keys
        if mismatch_label_keys is not None:
            self._values["mismatch_label_keys"] = mismatch_label_keys
        if namespaces is not None:
            self._values["namespaces"] = namespaces
        if namespace_selector is not None:
            self._values["namespace_selector"] = namespace_selector

    @builtins.property
    def topology_key(self) -> builtins.str:
        '''This pod should be co-located (affinity) or not co-located (anti-affinity) with the pods matching the labelSelector in the specified namespaces, where co-located is defined as running on a node whose value of the label with key topologyKey matches that of any node on which any of the selected pods is running.

        Empty topologyKey is not allowed.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTerm#topologyKey
        '''
        result = self._values.get("topology_key")
        assert result is not None, "Required property 'topology_key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def label_selector(
        self,
    ) -> typing.Optional["ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermLabelSelector"]:
        '''A label query over a set of resources, in this case pods.

        If it's null, this PodAffinityTerm matches with no Pods.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTerm#labelSelector
        '''
        result = self._values.get("label_selector")
        return typing.cast(typing.Optional["ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermLabelSelector"], result)

    @builtins.property
    def match_label_keys(self) -> typing.Optional[typing.List[builtins.str]]:
        '''MatchLabelKeys is a set of pod label keys to select which pods will be taken into consideration.

        The keys are used to lookup values from the
        incoming pod labels, those key-value labels are merged with ``labelSelector`` as ``key in (value)``
        to select the group of existing pods which pods will be taken into consideration
        for the incoming pod's pod (anti) affinity. Keys that don't exist in the incoming
        pod labels will be ignored. The default value is empty.
        The same key is forbidden to exist in both matchLabelKeys and labelSelector.
        Also, matchLabelKeys cannot be set when labelSelector isn't set.
        This is a beta field and requires enabling MatchLabelKeysInPodAffinity feature gate (enabled by default).

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTerm#matchLabelKeys
        '''
        result = self._values.get("match_label_keys")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def mismatch_label_keys(self) -> typing.Optional[typing.List[builtins.str]]:
        '''MismatchLabelKeys is a set of pod label keys to select which pods will be taken into consideration.

        The keys are used to lookup values from the
        incoming pod labels, those key-value labels are merged with ``labelSelector`` as ``key notin (value)``
        to select the group of existing pods which pods will be taken into consideration
        for the incoming pod's pod (anti) affinity. Keys that don't exist in the incoming
        pod labels will be ignored. The default value is empty.
        The same key is forbidden to exist in both mismatchLabelKeys and labelSelector.
        Also, mismatchLabelKeys cannot be set when labelSelector isn't set.
        This is a beta field and requires enabling MatchLabelKeysInPodAffinity feature gate (enabled by default).

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTerm#mismatchLabelKeys
        '''
        result = self._values.get("mismatch_label_keys")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def namespaces(self) -> typing.Optional[typing.List[builtins.str]]:
        '''namespaces specifies a static list of namespace names that the term applies to.

        The term is applied to the union of the namespaces listed in this field
        and the ones selected by namespaceSelector.
        null or empty namespaces list and null namespaceSelector means "this pod's namespace".

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTerm#namespaces
        '''
        result = self._values.get("namespaces")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def namespace_selector(
        self,
    ) -> typing.Optional["ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermNamespaceSelector"]:
        '''A label query over the set of namespaces that the term applies to.

        The term is applied to the union of the namespaces selected by this field
        and the ones listed in the namespaces field.
        null selector and null or empty namespaces list means "this pod's namespace".
        An empty selector ({}) matches all namespaces.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTerm#namespaceSelector
        '''
        result = self._values.get("namespace_selector")
        return typing.cast(typing.Optional["ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermNamespaceSelector"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTerm(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iocert-manageracme.ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermLabelSelector",
    jsii_struct_bases=[],
    name_mapping={
        "match_expressions": "matchExpressions",
        "match_labels": "matchLabels",
    },
)
class ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermLabelSelector:
    def __init__(
        self,
        *,
        match_expressions: typing.Optional[typing.Sequence[typing.Union["ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermLabelSelectorMatchExpressions", typing.Dict[builtins.str, typing.Any]]]] = None,
        match_labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''A label query over a set of resources, in this case pods.

        If it's null, this PodAffinityTerm matches with no Pods.

        :param match_expressions: matchExpressions is a list of label selector requirements. The requirements are ANDed.
        :param match_labels: matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermLabelSelector
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bab4a4fb78540135a5cb25eed199cb74e21a4985c3806c1519aeda545c5344d3)
            check_type(argname="argument match_expressions", value=match_expressions, expected_type=type_hints["match_expressions"])
            check_type(argname="argument match_labels", value=match_labels, expected_type=type_hints["match_labels"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if match_expressions is not None:
            self._values["match_expressions"] = match_expressions
        if match_labels is not None:
            self._values["match_labels"] = match_labels

    @builtins.property
    def match_expressions(
        self,
    ) -> typing.Optional[typing.List["ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermLabelSelectorMatchExpressions"]]:
        '''matchExpressions is a list of label selector requirements.

        The requirements are ANDed.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermLabelSelector#matchExpressions
        '''
        result = self._values.get("match_expressions")
        return typing.cast(typing.Optional[typing.List["ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermLabelSelectorMatchExpressions"]], result)

    @builtins.property
    def match_labels(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''matchLabels is a map of {key,value} pairs.

        A single {key,value} in the matchLabels
        map is equivalent to an element of matchExpressions, whose key field is "key", the
        operator is "In", and the values array contains only "value". The requirements are ANDed.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermLabelSelector#matchLabels
        '''
        result = self._values.get("match_labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermLabelSelector(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iocert-manageracme.ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermLabelSelectorMatchExpressions",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "operator": "operator", "values": "values"},
)
class ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermLabelSelectorMatchExpressions:
    def __init__(
        self,
        *,
        key: builtins.str,
        operator: builtins.str,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''A label selector requirement is a selector that contains values, a key, and an operator that relates the key and values.

        :param key: key is the label key that the selector applies to.
        :param operator: operator represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist.
        :param values: values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermLabelSelectorMatchExpressions
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__860f489daa83128689d6f48e3dc5ff1ff727b5c14e3648855eb6dd6c7738d97b)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "key": key,
            "operator": operator,
        }
        if values is not None:
            self._values["values"] = values

    @builtins.property
    def key(self) -> builtins.str:
        '''key is the label key that the selector applies to.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermLabelSelectorMatchExpressions#key
        '''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def operator(self) -> builtins.str:
        '''operator represents a key's relationship to a set of values.

        Valid operators are In, NotIn, Exists and DoesNotExist.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermLabelSelectorMatchExpressions#operator
        '''
        result = self._values.get("operator")
        assert result is not None, "Required property 'operator' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''values is an array of string values.

        If the operator is In or NotIn,
        the values array must be non-empty. If the operator is Exists or DoesNotExist,
        the values array must be empty. This array is replaced during a strategic
        merge patch.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermLabelSelectorMatchExpressions#values
        '''
        result = self._values.get("values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermLabelSelectorMatchExpressions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iocert-manageracme.ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermNamespaceSelector",
    jsii_struct_bases=[],
    name_mapping={
        "match_expressions": "matchExpressions",
        "match_labels": "matchLabels",
    },
)
class ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermNamespaceSelector:
    def __init__(
        self,
        *,
        match_expressions: typing.Optional[typing.Sequence[typing.Union["ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermNamespaceSelectorMatchExpressions", typing.Dict[builtins.str, typing.Any]]]] = None,
        match_labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''A label query over the set of namespaces that the term applies to.

        The term is applied to the union of the namespaces selected by this field
        and the ones listed in the namespaces field.
        null selector and null or empty namespaces list means "this pod's namespace".
        An empty selector ({}) matches all namespaces.

        :param match_expressions: matchExpressions is a list of label selector requirements. The requirements are ANDed.
        :param match_labels: matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermNamespaceSelector
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1e9b1c1ba3f72820af01ef8d576bcbce7940bafdab42d3dd675b6c936c1d8cfc)
            check_type(argname="argument match_expressions", value=match_expressions, expected_type=type_hints["match_expressions"])
            check_type(argname="argument match_labels", value=match_labels, expected_type=type_hints["match_labels"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if match_expressions is not None:
            self._values["match_expressions"] = match_expressions
        if match_labels is not None:
            self._values["match_labels"] = match_labels

    @builtins.property
    def match_expressions(
        self,
    ) -> typing.Optional[typing.List["ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermNamespaceSelectorMatchExpressions"]]:
        '''matchExpressions is a list of label selector requirements.

        The requirements are ANDed.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermNamespaceSelector#matchExpressions
        '''
        result = self._values.get("match_expressions")
        return typing.cast(typing.Optional[typing.List["ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermNamespaceSelectorMatchExpressions"]], result)

    @builtins.property
    def match_labels(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''matchLabels is a map of {key,value} pairs.

        A single {key,value} in the matchLabels
        map is equivalent to an element of matchExpressions, whose key field is "key", the
        operator is "In", and the values array contains only "value". The requirements are ANDed.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermNamespaceSelector#matchLabels
        '''
        result = self._values.get("match_labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermNamespaceSelector(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iocert-manageracme.ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermNamespaceSelectorMatchExpressions",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "operator": "operator", "values": "values"},
)
class ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermNamespaceSelectorMatchExpressions:
    def __init__(
        self,
        *,
        key: builtins.str,
        operator: builtins.str,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''A label selector requirement is a selector that contains values, a key, and an operator that relates the key and values.

        :param key: key is the label key that the selector applies to.
        :param operator: operator represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist.
        :param values: values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermNamespaceSelectorMatchExpressions
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__043f465ff0ebd6f84d1aa6be27ecaec09d22ae38d6e2e55ca7175e3c95e3ce08)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "key": key,
            "operator": operator,
        }
        if values is not None:
            self._values["values"] = values

    @builtins.property
    def key(self) -> builtins.str:
        '''key is the label key that the selector applies to.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermNamespaceSelectorMatchExpressions#key
        '''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def operator(self) -> builtins.str:
        '''operator represents a key's relationship to a set of values.

        Valid operators are In, NotIn, Exists and DoesNotExist.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermNamespaceSelectorMatchExpressions#operator
        '''
        result = self._values.get("operator")
        assert result is not None, "Required property 'operator' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''values is an array of string values.

        If the operator is In or NotIn,
        the values array must be non-empty. If the operator is Exists or DoesNotExist,
        the values array must be empty. This array is replaced during a strategic
        merge patch.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermNamespaceSelectorMatchExpressions#values
        '''
        result = self._values.get("values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermNamespaceSelectorMatchExpressions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iocert-manageracme.ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityRequiredDuringSchedulingIgnoredDuringExecution",
    jsii_struct_bases=[],
    name_mapping={
        "topology_key": "topologyKey",
        "label_selector": "labelSelector",
        "match_label_keys": "matchLabelKeys",
        "mismatch_label_keys": "mismatchLabelKeys",
        "namespaces": "namespaces",
        "namespace_selector": "namespaceSelector",
    },
)
class ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityRequiredDuringSchedulingIgnoredDuringExecution:
    def __init__(
        self,
        *,
        topology_key: builtins.str,
        label_selector: typing.Optional[typing.Union["ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityRequiredDuringSchedulingIgnoredDuringExecutionLabelSelector", typing.Dict[builtins.str, typing.Any]]] = None,
        match_label_keys: typing.Optional[typing.Sequence[builtins.str]] = None,
        mismatch_label_keys: typing.Optional[typing.Sequence[builtins.str]] = None,
        namespaces: typing.Optional[typing.Sequence[builtins.str]] = None,
        namespace_selector: typing.Optional[typing.Union["ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityRequiredDuringSchedulingIgnoredDuringExecutionNamespaceSelector", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''Defines a set of pods (namely those matching the labelSelector relative to the given namespace(s)) that this pod should be co-located (affinity) or not co-located (anti-affinity) with, where co-located is defined as running on a node whose value of the label with key  matches that of any node on which a pod of the set of pods is running.

        :param topology_key: This pod should be co-located (affinity) or not co-located (anti-affinity) with the pods matching the labelSelector in the specified namespaces, where co-located is defined as running on a node whose value of the label with key topologyKey matches that of any node on which any of the selected pods is running. Empty topologyKey is not allowed.
        :param label_selector: A label query over a set of resources, in this case pods. If it's null, this PodAffinityTerm matches with no Pods.
        :param match_label_keys: MatchLabelKeys is a set of pod label keys to select which pods will be taken into consideration. The keys are used to lookup values from the incoming pod labels, those key-value labels are merged with ``labelSelector`` as ``key in (value)`` to select the group of existing pods which pods will be taken into consideration for the incoming pod's pod (anti) affinity. Keys that don't exist in the incoming pod labels will be ignored. The default value is empty. The same key is forbidden to exist in both matchLabelKeys and labelSelector. Also, matchLabelKeys cannot be set when labelSelector isn't set. This is a beta field and requires enabling MatchLabelKeysInPodAffinity feature gate (enabled by default).
        :param mismatch_label_keys: MismatchLabelKeys is a set of pod label keys to select which pods will be taken into consideration. The keys are used to lookup values from the incoming pod labels, those key-value labels are merged with ``labelSelector`` as ``key notin (value)`` to select the group of existing pods which pods will be taken into consideration for the incoming pod's pod (anti) affinity. Keys that don't exist in the incoming pod labels will be ignored. The default value is empty. The same key is forbidden to exist in both mismatchLabelKeys and labelSelector. Also, mismatchLabelKeys cannot be set when labelSelector isn't set. This is a beta field and requires enabling MatchLabelKeysInPodAffinity feature gate (enabled by default).
        :param namespaces: namespaces specifies a static list of namespace names that the term applies to. The term is applied to the union of the namespaces listed in this field and the ones selected by namespaceSelector. null or empty namespaces list and null namespaceSelector means "this pod's namespace".
        :param namespace_selector: A label query over the set of namespaces that the term applies to. The term is applied to the union of the namespaces selected by this field and the ones listed in the namespaces field. null selector and null or empty namespaces list means "this pod's namespace". An empty selector ({}) matches all namespaces.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityRequiredDuringSchedulingIgnoredDuringExecution
        '''
        if isinstance(label_selector, dict):
            label_selector = ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityRequiredDuringSchedulingIgnoredDuringExecutionLabelSelector(**label_selector)
        if isinstance(namespace_selector, dict):
            namespace_selector = ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityRequiredDuringSchedulingIgnoredDuringExecutionNamespaceSelector(**namespace_selector)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__922594031745af5710f4997ce6758f019a75edb530bc7195bd558b71fc280418)
            check_type(argname="argument topology_key", value=topology_key, expected_type=type_hints["topology_key"])
            check_type(argname="argument label_selector", value=label_selector, expected_type=type_hints["label_selector"])
            check_type(argname="argument match_label_keys", value=match_label_keys, expected_type=type_hints["match_label_keys"])
            check_type(argname="argument mismatch_label_keys", value=mismatch_label_keys, expected_type=type_hints["mismatch_label_keys"])
            check_type(argname="argument namespaces", value=namespaces, expected_type=type_hints["namespaces"])
            check_type(argname="argument namespace_selector", value=namespace_selector, expected_type=type_hints["namespace_selector"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "topology_key": topology_key,
        }
        if label_selector is not None:
            self._values["label_selector"] = label_selector
        if match_label_keys is not None:
            self._values["match_label_keys"] = match_label_keys
        if mismatch_label_keys is not None:
            self._values["mismatch_label_keys"] = mismatch_label_keys
        if namespaces is not None:
            self._values["namespaces"] = namespaces
        if namespace_selector is not None:
            self._values["namespace_selector"] = namespace_selector

    @builtins.property
    def topology_key(self) -> builtins.str:
        '''This pod should be co-located (affinity) or not co-located (anti-affinity) with the pods matching the labelSelector in the specified namespaces, where co-located is defined as running on a node whose value of the label with key topologyKey matches that of any node on which any of the selected pods is running.

        Empty topologyKey is not allowed.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityRequiredDuringSchedulingIgnoredDuringExecution#topologyKey
        '''
        result = self._values.get("topology_key")
        assert result is not None, "Required property 'topology_key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def label_selector(
        self,
    ) -> typing.Optional["ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityRequiredDuringSchedulingIgnoredDuringExecutionLabelSelector"]:
        '''A label query over a set of resources, in this case pods.

        If it's null, this PodAffinityTerm matches with no Pods.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityRequiredDuringSchedulingIgnoredDuringExecution#labelSelector
        '''
        result = self._values.get("label_selector")
        return typing.cast(typing.Optional["ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityRequiredDuringSchedulingIgnoredDuringExecutionLabelSelector"], result)

    @builtins.property
    def match_label_keys(self) -> typing.Optional[typing.List[builtins.str]]:
        '''MatchLabelKeys is a set of pod label keys to select which pods will be taken into consideration.

        The keys are used to lookup values from the
        incoming pod labels, those key-value labels are merged with ``labelSelector`` as ``key in (value)``
        to select the group of existing pods which pods will be taken into consideration
        for the incoming pod's pod (anti) affinity. Keys that don't exist in the incoming
        pod labels will be ignored. The default value is empty.
        The same key is forbidden to exist in both matchLabelKeys and labelSelector.
        Also, matchLabelKeys cannot be set when labelSelector isn't set.
        This is a beta field and requires enabling MatchLabelKeysInPodAffinity feature gate (enabled by default).

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityRequiredDuringSchedulingIgnoredDuringExecution#matchLabelKeys
        '''
        result = self._values.get("match_label_keys")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def mismatch_label_keys(self) -> typing.Optional[typing.List[builtins.str]]:
        '''MismatchLabelKeys is a set of pod label keys to select which pods will be taken into consideration.

        The keys are used to lookup values from the
        incoming pod labels, those key-value labels are merged with ``labelSelector`` as ``key notin (value)``
        to select the group of existing pods which pods will be taken into consideration
        for the incoming pod's pod (anti) affinity. Keys that don't exist in the incoming
        pod labels will be ignored. The default value is empty.
        The same key is forbidden to exist in both mismatchLabelKeys and labelSelector.
        Also, mismatchLabelKeys cannot be set when labelSelector isn't set.
        This is a beta field and requires enabling MatchLabelKeysInPodAffinity feature gate (enabled by default).

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityRequiredDuringSchedulingIgnoredDuringExecution#mismatchLabelKeys
        '''
        result = self._values.get("mismatch_label_keys")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def namespaces(self) -> typing.Optional[typing.List[builtins.str]]:
        '''namespaces specifies a static list of namespace names that the term applies to.

        The term is applied to the union of the namespaces listed in this field
        and the ones selected by namespaceSelector.
        null or empty namespaces list and null namespaceSelector means "this pod's namespace".

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityRequiredDuringSchedulingIgnoredDuringExecution#namespaces
        '''
        result = self._values.get("namespaces")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def namespace_selector(
        self,
    ) -> typing.Optional["ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityRequiredDuringSchedulingIgnoredDuringExecutionNamespaceSelector"]:
        '''A label query over the set of namespaces that the term applies to.

        The term is applied to the union of the namespaces selected by this field
        and the ones listed in the namespaces field.
        null selector and null or empty namespaces list means "this pod's namespace".
        An empty selector ({}) matches all namespaces.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityRequiredDuringSchedulingIgnoredDuringExecution#namespaceSelector
        '''
        result = self._values.get("namespace_selector")
        return typing.cast(typing.Optional["ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityRequiredDuringSchedulingIgnoredDuringExecutionNamespaceSelector"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityRequiredDuringSchedulingIgnoredDuringExecution(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iocert-manageracme.ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityRequiredDuringSchedulingIgnoredDuringExecutionLabelSelector",
    jsii_struct_bases=[],
    name_mapping={
        "match_expressions": "matchExpressions",
        "match_labels": "matchLabels",
    },
)
class ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityRequiredDuringSchedulingIgnoredDuringExecutionLabelSelector:
    def __init__(
        self,
        *,
        match_expressions: typing.Optional[typing.Sequence[typing.Union["ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityRequiredDuringSchedulingIgnoredDuringExecutionLabelSelectorMatchExpressions", typing.Dict[builtins.str, typing.Any]]]] = None,
        match_labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''A label query over a set of resources, in this case pods.

        If it's null, this PodAffinityTerm matches with no Pods.

        :param match_expressions: matchExpressions is a list of label selector requirements. The requirements are ANDed.
        :param match_labels: matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityRequiredDuringSchedulingIgnoredDuringExecutionLabelSelector
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9378ba8a7b53c4f919d4882ae1278e31734324fc6e3ec7cc9b485ffe4b5f31d7)
            check_type(argname="argument match_expressions", value=match_expressions, expected_type=type_hints["match_expressions"])
            check_type(argname="argument match_labels", value=match_labels, expected_type=type_hints["match_labels"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if match_expressions is not None:
            self._values["match_expressions"] = match_expressions
        if match_labels is not None:
            self._values["match_labels"] = match_labels

    @builtins.property
    def match_expressions(
        self,
    ) -> typing.Optional[typing.List["ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityRequiredDuringSchedulingIgnoredDuringExecutionLabelSelectorMatchExpressions"]]:
        '''matchExpressions is a list of label selector requirements.

        The requirements are ANDed.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityRequiredDuringSchedulingIgnoredDuringExecutionLabelSelector#matchExpressions
        '''
        result = self._values.get("match_expressions")
        return typing.cast(typing.Optional[typing.List["ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityRequiredDuringSchedulingIgnoredDuringExecutionLabelSelectorMatchExpressions"]], result)

    @builtins.property
    def match_labels(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''matchLabels is a map of {key,value} pairs.

        A single {key,value} in the matchLabels
        map is equivalent to an element of matchExpressions, whose key field is "key", the
        operator is "In", and the values array contains only "value". The requirements are ANDed.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityRequiredDuringSchedulingIgnoredDuringExecutionLabelSelector#matchLabels
        '''
        result = self._values.get("match_labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityRequiredDuringSchedulingIgnoredDuringExecutionLabelSelector(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iocert-manageracme.ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityRequiredDuringSchedulingIgnoredDuringExecutionLabelSelectorMatchExpressions",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "operator": "operator", "values": "values"},
)
class ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityRequiredDuringSchedulingIgnoredDuringExecutionLabelSelectorMatchExpressions:
    def __init__(
        self,
        *,
        key: builtins.str,
        operator: builtins.str,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''A label selector requirement is a selector that contains values, a key, and an operator that relates the key and values.

        :param key: key is the label key that the selector applies to.
        :param operator: operator represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist.
        :param values: values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityRequiredDuringSchedulingIgnoredDuringExecutionLabelSelectorMatchExpressions
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ba23b47efb96d237c5b3540a82a4c9205457e0500ed1090e766570d8f7973b30)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "key": key,
            "operator": operator,
        }
        if values is not None:
            self._values["values"] = values

    @builtins.property
    def key(self) -> builtins.str:
        '''key is the label key that the selector applies to.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityRequiredDuringSchedulingIgnoredDuringExecutionLabelSelectorMatchExpressions#key
        '''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def operator(self) -> builtins.str:
        '''operator represents a key's relationship to a set of values.

        Valid operators are In, NotIn, Exists and DoesNotExist.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityRequiredDuringSchedulingIgnoredDuringExecutionLabelSelectorMatchExpressions#operator
        '''
        result = self._values.get("operator")
        assert result is not None, "Required property 'operator' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''values is an array of string values.

        If the operator is In or NotIn,
        the values array must be non-empty. If the operator is Exists or DoesNotExist,
        the values array must be empty. This array is replaced during a strategic
        merge patch.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityRequiredDuringSchedulingIgnoredDuringExecutionLabelSelectorMatchExpressions#values
        '''
        result = self._values.get("values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityRequiredDuringSchedulingIgnoredDuringExecutionLabelSelectorMatchExpressions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iocert-manageracme.ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityRequiredDuringSchedulingIgnoredDuringExecutionNamespaceSelector",
    jsii_struct_bases=[],
    name_mapping={
        "match_expressions": "matchExpressions",
        "match_labels": "matchLabels",
    },
)
class ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityRequiredDuringSchedulingIgnoredDuringExecutionNamespaceSelector:
    def __init__(
        self,
        *,
        match_expressions: typing.Optional[typing.Sequence[typing.Union["ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityRequiredDuringSchedulingIgnoredDuringExecutionNamespaceSelectorMatchExpressions", typing.Dict[builtins.str, typing.Any]]]] = None,
        match_labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''A label query over the set of namespaces that the term applies to.

        The term is applied to the union of the namespaces selected by this field
        and the ones listed in the namespaces field.
        null selector and null or empty namespaces list means "this pod's namespace".
        An empty selector ({}) matches all namespaces.

        :param match_expressions: matchExpressions is a list of label selector requirements. The requirements are ANDed.
        :param match_labels: matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityRequiredDuringSchedulingIgnoredDuringExecutionNamespaceSelector
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7e0de58859c9cd5be5f9fc24ca1433f8950542e5eaffc2af6582f958616c0a04)
            check_type(argname="argument match_expressions", value=match_expressions, expected_type=type_hints["match_expressions"])
            check_type(argname="argument match_labels", value=match_labels, expected_type=type_hints["match_labels"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if match_expressions is not None:
            self._values["match_expressions"] = match_expressions
        if match_labels is not None:
            self._values["match_labels"] = match_labels

    @builtins.property
    def match_expressions(
        self,
    ) -> typing.Optional[typing.List["ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityRequiredDuringSchedulingIgnoredDuringExecutionNamespaceSelectorMatchExpressions"]]:
        '''matchExpressions is a list of label selector requirements.

        The requirements are ANDed.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityRequiredDuringSchedulingIgnoredDuringExecutionNamespaceSelector#matchExpressions
        '''
        result = self._values.get("match_expressions")
        return typing.cast(typing.Optional[typing.List["ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityRequiredDuringSchedulingIgnoredDuringExecutionNamespaceSelectorMatchExpressions"]], result)

    @builtins.property
    def match_labels(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''matchLabels is a map of {key,value} pairs.

        A single {key,value} in the matchLabels
        map is equivalent to an element of matchExpressions, whose key field is "key", the
        operator is "In", and the values array contains only "value". The requirements are ANDed.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityRequiredDuringSchedulingIgnoredDuringExecutionNamespaceSelector#matchLabels
        '''
        result = self._values.get("match_labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityRequiredDuringSchedulingIgnoredDuringExecutionNamespaceSelector(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iocert-manageracme.ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityRequiredDuringSchedulingIgnoredDuringExecutionNamespaceSelectorMatchExpressions",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "operator": "operator", "values": "values"},
)
class ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityRequiredDuringSchedulingIgnoredDuringExecutionNamespaceSelectorMatchExpressions:
    def __init__(
        self,
        *,
        key: builtins.str,
        operator: builtins.str,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''A label selector requirement is a selector that contains values, a key, and an operator that relates the key and values.

        :param key: key is the label key that the selector applies to.
        :param operator: operator represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist.
        :param values: values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityRequiredDuringSchedulingIgnoredDuringExecutionNamespaceSelectorMatchExpressions
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bce77446c5edcba3f047d7e98cf05bfcdb22b07c83faa44338ef002a9848a7bd)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "key": key,
            "operator": operator,
        }
        if values is not None:
            self._values["values"] = values

    @builtins.property
    def key(self) -> builtins.str:
        '''key is the label key that the selector applies to.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityRequiredDuringSchedulingIgnoredDuringExecutionNamespaceSelectorMatchExpressions#key
        '''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def operator(self) -> builtins.str:
        '''operator represents a key's relationship to a set of values.

        Valid operators are In, NotIn, Exists and DoesNotExist.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityRequiredDuringSchedulingIgnoredDuringExecutionNamespaceSelectorMatchExpressions#operator
        '''
        result = self._values.get("operator")
        assert result is not None, "Required property 'operator' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''values is an array of string values.

        If the operator is In or NotIn,
        the values array must be non-empty. If the operator is Exists or DoesNotExist,
        the values array must be empty. This array is replaced during a strategic
        merge patch.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityRequiredDuringSchedulingIgnoredDuringExecutionNamespaceSelectorMatchExpressions#values
        '''
        result = self._values.get("values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityRequiredDuringSchedulingIgnoredDuringExecutionNamespaceSelectorMatchExpressions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iocert-manageracme.ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinity",
    jsii_struct_bases=[],
    name_mapping={
        "preferred_during_scheduling_ignored_during_execution": "preferredDuringSchedulingIgnoredDuringExecution",
        "required_during_scheduling_ignored_during_execution": "requiredDuringSchedulingIgnoredDuringExecution",
    },
)
class ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinity:
    def __init__(
        self,
        *,
        preferred_during_scheduling_ignored_during_execution: typing.Optional[typing.Sequence[typing.Union["ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecution", typing.Dict[builtins.str, typing.Any]]]] = None,
        required_during_scheduling_ignored_during_execution: typing.Optional[typing.Sequence[typing.Union["ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityRequiredDuringSchedulingIgnoredDuringExecution", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Describes pod anti-affinity scheduling rules (e.g. avoid putting this pod in the same node, zone, etc. as some other pod(s)).

        :param preferred_during_scheduling_ignored_during_execution: The scheduler will prefer to schedule pods to nodes that satisfy the anti-affinity expressions specified by this field, but it may choose a node that violates one or more of the expressions. The node that is most preferred is the one with the greatest sum of weights, i.e. for each node that meets all of the scheduling requirements (resource request, requiredDuringScheduling anti-affinity expressions, etc.), compute a sum by iterating through the elements of this field and adding "weight" to the sum if the node has pods which matches the corresponding podAffinityTerm; the node(s) with the highest sum are the most preferred.
        :param required_during_scheduling_ignored_during_execution: If the anti-affinity requirements specified by this field are not met at scheduling time, the pod will not be scheduled onto the node. If the anti-affinity requirements specified by this field cease to be met at some point during pod execution (e.g. due to a pod label update), the system may or may not try to eventually evict the pod from its node. When there are multiple elements, the lists of nodes corresponding to each podAffinityTerm are intersected, i.e. all terms must be satisfied.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinity
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2e3ef9df9d1f4bbc9dfda4479d18531323273cd91822ff6570c15b646ca5ae6e)
            check_type(argname="argument preferred_during_scheduling_ignored_during_execution", value=preferred_during_scheduling_ignored_during_execution, expected_type=type_hints["preferred_during_scheduling_ignored_during_execution"])
            check_type(argname="argument required_during_scheduling_ignored_during_execution", value=required_during_scheduling_ignored_during_execution, expected_type=type_hints["required_during_scheduling_ignored_during_execution"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if preferred_during_scheduling_ignored_during_execution is not None:
            self._values["preferred_during_scheduling_ignored_during_execution"] = preferred_during_scheduling_ignored_during_execution
        if required_during_scheduling_ignored_during_execution is not None:
            self._values["required_during_scheduling_ignored_during_execution"] = required_during_scheduling_ignored_during_execution

    @builtins.property
    def preferred_during_scheduling_ignored_during_execution(
        self,
    ) -> typing.Optional[typing.List["ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecution"]]:
        '''The scheduler will prefer to schedule pods to nodes that satisfy the anti-affinity expressions specified by this field, but it may choose a node that violates one or more of the expressions.

        The node that is
        most preferred is the one with the greatest sum of weights, i.e.
        for each node that meets all of the scheduling requirements (resource
        request, requiredDuringScheduling anti-affinity expressions, etc.),
        compute a sum by iterating through the elements of this field and adding
        "weight" to the sum if the node has pods which matches the corresponding podAffinityTerm; the
        node(s) with the highest sum are the most preferred.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinity#preferredDuringSchedulingIgnoredDuringExecution
        '''
        result = self._values.get("preferred_during_scheduling_ignored_during_execution")
        return typing.cast(typing.Optional[typing.List["ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecution"]], result)

    @builtins.property
    def required_during_scheduling_ignored_during_execution(
        self,
    ) -> typing.Optional[typing.List["ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityRequiredDuringSchedulingIgnoredDuringExecution"]]:
        '''If the anti-affinity requirements specified by this field are not met at scheduling time, the pod will not be scheduled onto the node.

        If the anti-affinity requirements specified by this field cease to be met
        at some point during pod execution (e.g. due to a pod label update), the
        system may or may not try to eventually evict the pod from its node.
        When there are multiple elements, the lists of nodes corresponding to each
        podAffinityTerm are intersected, i.e. all terms must be satisfied.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinity#requiredDuringSchedulingIgnoredDuringExecution
        '''
        result = self._values.get("required_during_scheduling_ignored_during_execution")
        return typing.cast(typing.Optional[typing.List["ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityRequiredDuringSchedulingIgnoredDuringExecution"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinity(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iocert-manageracme.ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecution",
    jsii_struct_bases=[],
    name_mapping={"pod_affinity_term": "podAffinityTerm", "weight": "weight"},
)
class ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecution:
    def __init__(
        self,
        *,
        pod_affinity_term: typing.Union["ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTerm", typing.Dict[builtins.str, typing.Any]],
        weight: jsii.Number,
    ) -> None:
        '''The weights of all of the matched WeightedPodAffinityTerm fields are added per-node to find the most preferred node(s).

        :param pod_affinity_term: Required. A pod affinity term, associated with the corresponding weight.
        :param weight: weight associated with matching the corresponding podAffinityTerm, in the range 1-100.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecution
        '''
        if isinstance(pod_affinity_term, dict):
            pod_affinity_term = ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTerm(**pod_affinity_term)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__155ee19c3e7f0489156b102f27150e749c596f8955b60a1a6d79c4569d6d8073)
            check_type(argname="argument pod_affinity_term", value=pod_affinity_term, expected_type=type_hints["pod_affinity_term"])
            check_type(argname="argument weight", value=weight, expected_type=type_hints["weight"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "pod_affinity_term": pod_affinity_term,
            "weight": weight,
        }

    @builtins.property
    def pod_affinity_term(
        self,
    ) -> "ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTerm":
        '''Required.

        A pod affinity term, associated with the corresponding weight.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecution#podAffinityTerm
        '''
        result = self._values.get("pod_affinity_term")
        assert result is not None, "Required property 'pod_affinity_term' is missing"
        return typing.cast("ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTerm", result)

    @builtins.property
    def weight(self) -> jsii.Number:
        '''weight associated with matching the corresponding podAffinityTerm, in the range 1-100.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecution#weight
        '''
        result = self._values.get("weight")
        assert result is not None, "Required property 'weight' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecution(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iocert-manageracme.ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTerm",
    jsii_struct_bases=[],
    name_mapping={
        "topology_key": "topologyKey",
        "label_selector": "labelSelector",
        "match_label_keys": "matchLabelKeys",
        "mismatch_label_keys": "mismatchLabelKeys",
        "namespaces": "namespaces",
        "namespace_selector": "namespaceSelector",
    },
)
class ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTerm:
    def __init__(
        self,
        *,
        topology_key: builtins.str,
        label_selector: typing.Optional[typing.Union["ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermLabelSelector", typing.Dict[builtins.str, typing.Any]]] = None,
        match_label_keys: typing.Optional[typing.Sequence[builtins.str]] = None,
        mismatch_label_keys: typing.Optional[typing.Sequence[builtins.str]] = None,
        namespaces: typing.Optional[typing.Sequence[builtins.str]] = None,
        namespace_selector: typing.Optional[typing.Union["ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermNamespaceSelector", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''Required.

        A pod affinity term, associated with the corresponding weight.

        :param topology_key: This pod should be co-located (affinity) or not co-located (anti-affinity) with the pods matching the labelSelector in the specified namespaces, where co-located is defined as running on a node whose value of the label with key topologyKey matches that of any node on which any of the selected pods is running. Empty topologyKey is not allowed.
        :param label_selector: A label query over a set of resources, in this case pods. If it's null, this PodAffinityTerm matches with no Pods.
        :param match_label_keys: MatchLabelKeys is a set of pod label keys to select which pods will be taken into consideration. The keys are used to lookup values from the incoming pod labels, those key-value labels are merged with ``labelSelector`` as ``key in (value)`` to select the group of existing pods which pods will be taken into consideration for the incoming pod's pod (anti) affinity. Keys that don't exist in the incoming pod labels will be ignored. The default value is empty. The same key is forbidden to exist in both matchLabelKeys and labelSelector. Also, matchLabelKeys cannot be set when labelSelector isn't set. This is a beta field and requires enabling MatchLabelKeysInPodAffinity feature gate (enabled by default).
        :param mismatch_label_keys: MismatchLabelKeys is a set of pod label keys to select which pods will be taken into consideration. The keys are used to lookup values from the incoming pod labels, those key-value labels are merged with ``labelSelector`` as ``key notin (value)`` to select the group of existing pods which pods will be taken into consideration for the incoming pod's pod (anti) affinity. Keys that don't exist in the incoming pod labels will be ignored. The default value is empty. The same key is forbidden to exist in both mismatchLabelKeys and labelSelector. Also, mismatchLabelKeys cannot be set when labelSelector isn't set. This is a beta field and requires enabling MatchLabelKeysInPodAffinity feature gate (enabled by default).
        :param namespaces: namespaces specifies a static list of namespace names that the term applies to. The term is applied to the union of the namespaces listed in this field and the ones selected by namespaceSelector. null or empty namespaces list and null namespaceSelector means "this pod's namespace".
        :param namespace_selector: A label query over the set of namespaces that the term applies to. The term is applied to the union of the namespaces selected by this field and the ones listed in the namespaces field. null selector and null or empty namespaces list means "this pod's namespace". An empty selector ({}) matches all namespaces.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTerm
        '''
        if isinstance(label_selector, dict):
            label_selector = ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermLabelSelector(**label_selector)
        if isinstance(namespace_selector, dict):
            namespace_selector = ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermNamespaceSelector(**namespace_selector)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ace66bc55b30573a6c9bcb8ead82e91f877f68addf011d52c4b4f30cffb50afe)
            check_type(argname="argument topology_key", value=topology_key, expected_type=type_hints["topology_key"])
            check_type(argname="argument label_selector", value=label_selector, expected_type=type_hints["label_selector"])
            check_type(argname="argument match_label_keys", value=match_label_keys, expected_type=type_hints["match_label_keys"])
            check_type(argname="argument mismatch_label_keys", value=mismatch_label_keys, expected_type=type_hints["mismatch_label_keys"])
            check_type(argname="argument namespaces", value=namespaces, expected_type=type_hints["namespaces"])
            check_type(argname="argument namespace_selector", value=namespace_selector, expected_type=type_hints["namespace_selector"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "topology_key": topology_key,
        }
        if label_selector is not None:
            self._values["label_selector"] = label_selector
        if match_label_keys is not None:
            self._values["match_label_keys"] = match_label_keys
        if mismatch_label_keys is not None:
            self._values["mismatch_label_keys"] = mismatch_label_keys
        if namespaces is not None:
            self._values["namespaces"] = namespaces
        if namespace_selector is not None:
            self._values["namespace_selector"] = namespace_selector

    @builtins.property
    def topology_key(self) -> builtins.str:
        '''This pod should be co-located (affinity) or not co-located (anti-affinity) with the pods matching the labelSelector in the specified namespaces, where co-located is defined as running on a node whose value of the label with key topologyKey matches that of any node on which any of the selected pods is running.

        Empty topologyKey is not allowed.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTerm#topologyKey
        '''
        result = self._values.get("topology_key")
        assert result is not None, "Required property 'topology_key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def label_selector(
        self,
    ) -> typing.Optional["ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermLabelSelector"]:
        '''A label query over a set of resources, in this case pods.

        If it's null, this PodAffinityTerm matches with no Pods.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTerm#labelSelector
        '''
        result = self._values.get("label_selector")
        return typing.cast(typing.Optional["ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermLabelSelector"], result)

    @builtins.property
    def match_label_keys(self) -> typing.Optional[typing.List[builtins.str]]:
        '''MatchLabelKeys is a set of pod label keys to select which pods will be taken into consideration.

        The keys are used to lookup values from the
        incoming pod labels, those key-value labels are merged with ``labelSelector`` as ``key in (value)``
        to select the group of existing pods which pods will be taken into consideration
        for the incoming pod's pod (anti) affinity. Keys that don't exist in the incoming
        pod labels will be ignored. The default value is empty.
        The same key is forbidden to exist in both matchLabelKeys and labelSelector.
        Also, matchLabelKeys cannot be set when labelSelector isn't set.
        This is a beta field and requires enabling MatchLabelKeysInPodAffinity feature gate (enabled by default).

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTerm#matchLabelKeys
        '''
        result = self._values.get("match_label_keys")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def mismatch_label_keys(self) -> typing.Optional[typing.List[builtins.str]]:
        '''MismatchLabelKeys is a set of pod label keys to select which pods will be taken into consideration.

        The keys are used to lookup values from the
        incoming pod labels, those key-value labels are merged with ``labelSelector`` as ``key notin (value)``
        to select the group of existing pods which pods will be taken into consideration
        for the incoming pod's pod (anti) affinity. Keys that don't exist in the incoming
        pod labels will be ignored. The default value is empty.
        The same key is forbidden to exist in both mismatchLabelKeys and labelSelector.
        Also, mismatchLabelKeys cannot be set when labelSelector isn't set.
        This is a beta field and requires enabling MatchLabelKeysInPodAffinity feature gate (enabled by default).

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTerm#mismatchLabelKeys
        '''
        result = self._values.get("mismatch_label_keys")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def namespaces(self) -> typing.Optional[typing.List[builtins.str]]:
        '''namespaces specifies a static list of namespace names that the term applies to.

        The term is applied to the union of the namespaces listed in this field
        and the ones selected by namespaceSelector.
        null or empty namespaces list and null namespaceSelector means "this pod's namespace".

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTerm#namespaces
        '''
        result = self._values.get("namespaces")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def namespace_selector(
        self,
    ) -> typing.Optional["ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermNamespaceSelector"]:
        '''A label query over the set of namespaces that the term applies to.

        The term is applied to the union of the namespaces selected by this field
        and the ones listed in the namespaces field.
        null selector and null or empty namespaces list means "this pod's namespace".
        An empty selector ({}) matches all namespaces.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTerm#namespaceSelector
        '''
        result = self._values.get("namespace_selector")
        return typing.cast(typing.Optional["ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermNamespaceSelector"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTerm(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iocert-manageracme.ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermLabelSelector",
    jsii_struct_bases=[],
    name_mapping={
        "match_expressions": "matchExpressions",
        "match_labels": "matchLabels",
    },
)
class ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermLabelSelector:
    def __init__(
        self,
        *,
        match_expressions: typing.Optional[typing.Sequence[typing.Union["ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermLabelSelectorMatchExpressions", typing.Dict[builtins.str, typing.Any]]]] = None,
        match_labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''A label query over a set of resources, in this case pods.

        If it's null, this PodAffinityTerm matches with no Pods.

        :param match_expressions: matchExpressions is a list of label selector requirements. The requirements are ANDed.
        :param match_labels: matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermLabelSelector
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__944085c3fc4b87f3f9bd37e2bb5cd2f98be5e92ba1e8d0efb81aa103f8c044d8)
            check_type(argname="argument match_expressions", value=match_expressions, expected_type=type_hints["match_expressions"])
            check_type(argname="argument match_labels", value=match_labels, expected_type=type_hints["match_labels"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if match_expressions is not None:
            self._values["match_expressions"] = match_expressions
        if match_labels is not None:
            self._values["match_labels"] = match_labels

    @builtins.property
    def match_expressions(
        self,
    ) -> typing.Optional[typing.List["ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermLabelSelectorMatchExpressions"]]:
        '''matchExpressions is a list of label selector requirements.

        The requirements are ANDed.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermLabelSelector#matchExpressions
        '''
        result = self._values.get("match_expressions")
        return typing.cast(typing.Optional[typing.List["ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermLabelSelectorMatchExpressions"]], result)

    @builtins.property
    def match_labels(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''matchLabels is a map of {key,value} pairs.

        A single {key,value} in the matchLabels
        map is equivalent to an element of matchExpressions, whose key field is "key", the
        operator is "In", and the values array contains only "value". The requirements are ANDed.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermLabelSelector#matchLabels
        '''
        result = self._values.get("match_labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermLabelSelector(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iocert-manageracme.ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermLabelSelectorMatchExpressions",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "operator": "operator", "values": "values"},
)
class ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermLabelSelectorMatchExpressions:
    def __init__(
        self,
        *,
        key: builtins.str,
        operator: builtins.str,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''A label selector requirement is a selector that contains values, a key, and an operator that relates the key and values.

        :param key: key is the label key that the selector applies to.
        :param operator: operator represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist.
        :param values: values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermLabelSelectorMatchExpressions
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__822d41b914f479e420f6875d275ba9106843b1ef62f665f216e4e4eed1872169)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "key": key,
            "operator": operator,
        }
        if values is not None:
            self._values["values"] = values

    @builtins.property
    def key(self) -> builtins.str:
        '''key is the label key that the selector applies to.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermLabelSelectorMatchExpressions#key
        '''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def operator(self) -> builtins.str:
        '''operator represents a key's relationship to a set of values.

        Valid operators are In, NotIn, Exists and DoesNotExist.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermLabelSelectorMatchExpressions#operator
        '''
        result = self._values.get("operator")
        assert result is not None, "Required property 'operator' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''values is an array of string values.

        If the operator is In or NotIn,
        the values array must be non-empty. If the operator is Exists or DoesNotExist,
        the values array must be empty. This array is replaced during a strategic
        merge patch.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermLabelSelectorMatchExpressions#values
        '''
        result = self._values.get("values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermLabelSelectorMatchExpressions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iocert-manageracme.ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermNamespaceSelector",
    jsii_struct_bases=[],
    name_mapping={
        "match_expressions": "matchExpressions",
        "match_labels": "matchLabels",
    },
)
class ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermNamespaceSelector:
    def __init__(
        self,
        *,
        match_expressions: typing.Optional[typing.Sequence[typing.Union["ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermNamespaceSelectorMatchExpressions", typing.Dict[builtins.str, typing.Any]]]] = None,
        match_labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''A label query over the set of namespaces that the term applies to.

        The term is applied to the union of the namespaces selected by this field
        and the ones listed in the namespaces field.
        null selector and null or empty namespaces list means "this pod's namespace".
        An empty selector ({}) matches all namespaces.

        :param match_expressions: matchExpressions is a list of label selector requirements. The requirements are ANDed.
        :param match_labels: matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermNamespaceSelector
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a19ba490e46c6abe28e31a4a3329365b55b4233f5376d47eab3085e6a59dddb5)
            check_type(argname="argument match_expressions", value=match_expressions, expected_type=type_hints["match_expressions"])
            check_type(argname="argument match_labels", value=match_labels, expected_type=type_hints["match_labels"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if match_expressions is not None:
            self._values["match_expressions"] = match_expressions
        if match_labels is not None:
            self._values["match_labels"] = match_labels

    @builtins.property
    def match_expressions(
        self,
    ) -> typing.Optional[typing.List["ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermNamespaceSelectorMatchExpressions"]]:
        '''matchExpressions is a list of label selector requirements.

        The requirements are ANDed.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermNamespaceSelector#matchExpressions
        '''
        result = self._values.get("match_expressions")
        return typing.cast(typing.Optional[typing.List["ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermNamespaceSelectorMatchExpressions"]], result)

    @builtins.property
    def match_labels(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''matchLabels is a map of {key,value} pairs.

        A single {key,value} in the matchLabels
        map is equivalent to an element of matchExpressions, whose key field is "key", the
        operator is "In", and the values array contains only "value". The requirements are ANDed.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermNamespaceSelector#matchLabels
        '''
        result = self._values.get("match_labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermNamespaceSelector(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iocert-manageracme.ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermNamespaceSelectorMatchExpressions",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "operator": "operator", "values": "values"},
)
class ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermNamespaceSelectorMatchExpressions:
    def __init__(
        self,
        *,
        key: builtins.str,
        operator: builtins.str,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''A label selector requirement is a selector that contains values, a key, and an operator that relates the key and values.

        :param key: key is the label key that the selector applies to.
        :param operator: operator represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist.
        :param values: values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermNamespaceSelectorMatchExpressions
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0700bf41205c8a58d3606f40af63faaafdf5a99220aad0cd2270cfc0ae7605f2)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "key": key,
            "operator": operator,
        }
        if values is not None:
            self._values["values"] = values

    @builtins.property
    def key(self) -> builtins.str:
        '''key is the label key that the selector applies to.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermNamespaceSelectorMatchExpressions#key
        '''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def operator(self) -> builtins.str:
        '''operator represents a key's relationship to a set of values.

        Valid operators are In, NotIn, Exists and DoesNotExist.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermNamespaceSelectorMatchExpressions#operator
        '''
        result = self._values.get("operator")
        assert result is not None, "Required property 'operator' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''values is an array of string values.

        If the operator is In or NotIn,
        the values array must be non-empty. If the operator is Exists or DoesNotExist,
        the values array must be empty. This array is replaced during a strategic
        merge patch.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermNamespaceSelectorMatchExpressions#values
        '''
        result = self._values.get("values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermNamespaceSelectorMatchExpressions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iocert-manageracme.ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityRequiredDuringSchedulingIgnoredDuringExecution",
    jsii_struct_bases=[],
    name_mapping={
        "topology_key": "topologyKey",
        "label_selector": "labelSelector",
        "match_label_keys": "matchLabelKeys",
        "mismatch_label_keys": "mismatchLabelKeys",
        "namespaces": "namespaces",
        "namespace_selector": "namespaceSelector",
    },
)
class ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityRequiredDuringSchedulingIgnoredDuringExecution:
    def __init__(
        self,
        *,
        topology_key: builtins.str,
        label_selector: typing.Optional[typing.Union["ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityRequiredDuringSchedulingIgnoredDuringExecutionLabelSelector", typing.Dict[builtins.str, typing.Any]]] = None,
        match_label_keys: typing.Optional[typing.Sequence[builtins.str]] = None,
        mismatch_label_keys: typing.Optional[typing.Sequence[builtins.str]] = None,
        namespaces: typing.Optional[typing.Sequence[builtins.str]] = None,
        namespace_selector: typing.Optional[typing.Union["ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityRequiredDuringSchedulingIgnoredDuringExecutionNamespaceSelector", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''Defines a set of pods (namely those matching the labelSelector relative to the given namespace(s)) that this pod should be co-located (affinity) or not co-located (anti-affinity) with, where co-located is defined as running on a node whose value of the label with key  matches that of any node on which a pod of the set of pods is running.

        :param topology_key: This pod should be co-located (affinity) or not co-located (anti-affinity) with the pods matching the labelSelector in the specified namespaces, where co-located is defined as running on a node whose value of the label with key topologyKey matches that of any node on which any of the selected pods is running. Empty topologyKey is not allowed.
        :param label_selector: A label query over a set of resources, in this case pods. If it's null, this PodAffinityTerm matches with no Pods.
        :param match_label_keys: MatchLabelKeys is a set of pod label keys to select which pods will be taken into consideration. The keys are used to lookup values from the incoming pod labels, those key-value labels are merged with ``labelSelector`` as ``key in (value)`` to select the group of existing pods which pods will be taken into consideration for the incoming pod's pod (anti) affinity. Keys that don't exist in the incoming pod labels will be ignored. The default value is empty. The same key is forbidden to exist in both matchLabelKeys and labelSelector. Also, matchLabelKeys cannot be set when labelSelector isn't set. This is a beta field and requires enabling MatchLabelKeysInPodAffinity feature gate (enabled by default).
        :param mismatch_label_keys: MismatchLabelKeys is a set of pod label keys to select which pods will be taken into consideration. The keys are used to lookup values from the incoming pod labels, those key-value labels are merged with ``labelSelector`` as ``key notin (value)`` to select the group of existing pods which pods will be taken into consideration for the incoming pod's pod (anti) affinity. Keys that don't exist in the incoming pod labels will be ignored. The default value is empty. The same key is forbidden to exist in both mismatchLabelKeys and labelSelector. Also, mismatchLabelKeys cannot be set when labelSelector isn't set. This is a beta field and requires enabling MatchLabelKeysInPodAffinity feature gate (enabled by default).
        :param namespaces: namespaces specifies a static list of namespace names that the term applies to. The term is applied to the union of the namespaces listed in this field and the ones selected by namespaceSelector. null or empty namespaces list and null namespaceSelector means "this pod's namespace".
        :param namespace_selector: A label query over the set of namespaces that the term applies to. The term is applied to the union of the namespaces selected by this field and the ones listed in the namespaces field. null selector and null or empty namespaces list means "this pod's namespace". An empty selector ({}) matches all namespaces.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityRequiredDuringSchedulingIgnoredDuringExecution
        '''
        if isinstance(label_selector, dict):
            label_selector = ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityRequiredDuringSchedulingIgnoredDuringExecutionLabelSelector(**label_selector)
        if isinstance(namespace_selector, dict):
            namespace_selector = ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityRequiredDuringSchedulingIgnoredDuringExecutionNamespaceSelector(**namespace_selector)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e57996b1d7410c01ce12a88738aa9506e3b9069a1309440938c64caf1fec5e7c)
            check_type(argname="argument topology_key", value=topology_key, expected_type=type_hints["topology_key"])
            check_type(argname="argument label_selector", value=label_selector, expected_type=type_hints["label_selector"])
            check_type(argname="argument match_label_keys", value=match_label_keys, expected_type=type_hints["match_label_keys"])
            check_type(argname="argument mismatch_label_keys", value=mismatch_label_keys, expected_type=type_hints["mismatch_label_keys"])
            check_type(argname="argument namespaces", value=namespaces, expected_type=type_hints["namespaces"])
            check_type(argname="argument namespace_selector", value=namespace_selector, expected_type=type_hints["namespace_selector"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "topology_key": topology_key,
        }
        if label_selector is not None:
            self._values["label_selector"] = label_selector
        if match_label_keys is not None:
            self._values["match_label_keys"] = match_label_keys
        if mismatch_label_keys is not None:
            self._values["mismatch_label_keys"] = mismatch_label_keys
        if namespaces is not None:
            self._values["namespaces"] = namespaces
        if namespace_selector is not None:
            self._values["namespace_selector"] = namespace_selector

    @builtins.property
    def topology_key(self) -> builtins.str:
        '''This pod should be co-located (affinity) or not co-located (anti-affinity) with the pods matching the labelSelector in the specified namespaces, where co-located is defined as running on a node whose value of the label with key topologyKey matches that of any node on which any of the selected pods is running.

        Empty topologyKey is not allowed.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityRequiredDuringSchedulingIgnoredDuringExecution#topologyKey
        '''
        result = self._values.get("topology_key")
        assert result is not None, "Required property 'topology_key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def label_selector(
        self,
    ) -> typing.Optional["ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityRequiredDuringSchedulingIgnoredDuringExecutionLabelSelector"]:
        '''A label query over a set of resources, in this case pods.

        If it's null, this PodAffinityTerm matches with no Pods.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityRequiredDuringSchedulingIgnoredDuringExecution#labelSelector
        '''
        result = self._values.get("label_selector")
        return typing.cast(typing.Optional["ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityRequiredDuringSchedulingIgnoredDuringExecutionLabelSelector"], result)

    @builtins.property
    def match_label_keys(self) -> typing.Optional[typing.List[builtins.str]]:
        '''MatchLabelKeys is a set of pod label keys to select which pods will be taken into consideration.

        The keys are used to lookup values from the
        incoming pod labels, those key-value labels are merged with ``labelSelector`` as ``key in (value)``
        to select the group of existing pods which pods will be taken into consideration
        for the incoming pod's pod (anti) affinity. Keys that don't exist in the incoming
        pod labels will be ignored. The default value is empty.
        The same key is forbidden to exist in both matchLabelKeys and labelSelector.
        Also, matchLabelKeys cannot be set when labelSelector isn't set.
        This is a beta field and requires enabling MatchLabelKeysInPodAffinity feature gate (enabled by default).

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityRequiredDuringSchedulingIgnoredDuringExecution#matchLabelKeys
        '''
        result = self._values.get("match_label_keys")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def mismatch_label_keys(self) -> typing.Optional[typing.List[builtins.str]]:
        '''MismatchLabelKeys is a set of pod label keys to select which pods will be taken into consideration.

        The keys are used to lookup values from the
        incoming pod labels, those key-value labels are merged with ``labelSelector`` as ``key notin (value)``
        to select the group of existing pods which pods will be taken into consideration
        for the incoming pod's pod (anti) affinity. Keys that don't exist in the incoming
        pod labels will be ignored. The default value is empty.
        The same key is forbidden to exist in both mismatchLabelKeys and labelSelector.
        Also, mismatchLabelKeys cannot be set when labelSelector isn't set.
        This is a beta field and requires enabling MatchLabelKeysInPodAffinity feature gate (enabled by default).

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityRequiredDuringSchedulingIgnoredDuringExecution#mismatchLabelKeys
        '''
        result = self._values.get("mismatch_label_keys")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def namespaces(self) -> typing.Optional[typing.List[builtins.str]]:
        '''namespaces specifies a static list of namespace names that the term applies to.

        The term is applied to the union of the namespaces listed in this field
        and the ones selected by namespaceSelector.
        null or empty namespaces list and null namespaceSelector means "this pod's namespace".

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityRequiredDuringSchedulingIgnoredDuringExecution#namespaces
        '''
        result = self._values.get("namespaces")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def namespace_selector(
        self,
    ) -> typing.Optional["ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityRequiredDuringSchedulingIgnoredDuringExecutionNamespaceSelector"]:
        '''A label query over the set of namespaces that the term applies to.

        The term is applied to the union of the namespaces selected by this field
        and the ones listed in the namespaces field.
        null selector and null or empty namespaces list means "this pod's namespace".
        An empty selector ({}) matches all namespaces.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityRequiredDuringSchedulingIgnoredDuringExecution#namespaceSelector
        '''
        result = self._values.get("namespace_selector")
        return typing.cast(typing.Optional["ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityRequiredDuringSchedulingIgnoredDuringExecutionNamespaceSelector"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityRequiredDuringSchedulingIgnoredDuringExecution(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iocert-manageracme.ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityRequiredDuringSchedulingIgnoredDuringExecutionLabelSelector",
    jsii_struct_bases=[],
    name_mapping={
        "match_expressions": "matchExpressions",
        "match_labels": "matchLabels",
    },
)
class ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityRequiredDuringSchedulingIgnoredDuringExecutionLabelSelector:
    def __init__(
        self,
        *,
        match_expressions: typing.Optional[typing.Sequence[typing.Union["ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityRequiredDuringSchedulingIgnoredDuringExecutionLabelSelectorMatchExpressions", typing.Dict[builtins.str, typing.Any]]]] = None,
        match_labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''A label query over a set of resources, in this case pods.

        If it's null, this PodAffinityTerm matches with no Pods.

        :param match_expressions: matchExpressions is a list of label selector requirements. The requirements are ANDed.
        :param match_labels: matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityRequiredDuringSchedulingIgnoredDuringExecutionLabelSelector
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__88fcd141034e5e8a5f70bdffe1823be15efc53ea470ed5ed436f5c251a491ff6)
            check_type(argname="argument match_expressions", value=match_expressions, expected_type=type_hints["match_expressions"])
            check_type(argname="argument match_labels", value=match_labels, expected_type=type_hints["match_labels"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if match_expressions is not None:
            self._values["match_expressions"] = match_expressions
        if match_labels is not None:
            self._values["match_labels"] = match_labels

    @builtins.property
    def match_expressions(
        self,
    ) -> typing.Optional[typing.List["ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityRequiredDuringSchedulingIgnoredDuringExecutionLabelSelectorMatchExpressions"]]:
        '''matchExpressions is a list of label selector requirements.

        The requirements are ANDed.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityRequiredDuringSchedulingIgnoredDuringExecutionLabelSelector#matchExpressions
        '''
        result = self._values.get("match_expressions")
        return typing.cast(typing.Optional[typing.List["ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityRequiredDuringSchedulingIgnoredDuringExecutionLabelSelectorMatchExpressions"]], result)

    @builtins.property
    def match_labels(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''matchLabels is a map of {key,value} pairs.

        A single {key,value} in the matchLabels
        map is equivalent to an element of matchExpressions, whose key field is "key", the
        operator is "In", and the values array contains only "value". The requirements are ANDed.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityRequiredDuringSchedulingIgnoredDuringExecutionLabelSelector#matchLabels
        '''
        result = self._values.get("match_labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityRequiredDuringSchedulingIgnoredDuringExecutionLabelSelector(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iocert-manageracme.ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityRequiredDuringSchedulingIgnoredDuringExecutionLabelSelectorMatchExpressions",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "operator": "operator", "values": "values"},
)
class ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityRequiredDuringSchedulingIgnoredDuringExecutionLabelSelectorMatchExpressions:
    def __init__(
        self,
        *,
        key: builtins.str,
        operator: builtins.str,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''A label selector requirement is a selector that contains values, a key, and an operator that relates the key and values.

        :param key: key is the label key that the selector applies to.
        :param operator: operator represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist.
        :param values: values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityRequiredDuringSchedulingIgnoredDuringExecutionLabelSelectorMatchExpressions
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6d089adc0a13ef81db73caa1a124194502656b46d958ea845f7c9c78348cdbc9)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "key": key,
            "operator": operator,
        }
        if values is not None:
            self._values["values"] = values

    @builtins.property
    def key(self) -> builtins.str:
        '''key is the label key that the selector applies to.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityRequiredDuringSchedulingIgnoredDuringExecutionLabelSelectorMatchExpressions#key
        '''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def operator(self) -> builtins.str:
        '''operator represents a key's relationship to a set of values.

        Valid operators are In, NotIn, Exists and DoesNotExist.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityRequiredDuringSchedulingIgnoredDuringExecutionLabelSelectorMatchExpressions#operator
        '''
        result = self._values.get("operator")
        assert result is not None, "Required property 'operator' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''values is an array of string values.

        If the operator is In or NotIn,
        the values array must be non-empty. If the operator is Exists or DoesNotExist,
        the values array must be empty. This array is replaced during a strategic
        merge patch.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityRequiredDuringSchedulingIgnoredDuringExecutionLabelSelectorMatchExpressions#values
        '''
        result = self._values.get("values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityRequiredDuringSchedulingIgnoredDuringExecutionLabelSelectorMatchExpressions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iocert-manageracme.ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityRequiredDuringSchedulingIgnoredDuringExecutionNamespaceSelector",
    jsii_struct_bases=[],
    name_mapping={
        "match_expressions": "matchExpressions",
        "match_labels": "matchLabels",
    },
)
class ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityRequiredDuringSchedulingIgnoredDuringExecutionNamespaceSelector:
    def __init__(
        self,
        *,
        match_expressions: typing.Optional[typing.Sequence[typing.Union["ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityRequiredDuringSchedulingIgnoredDuringExecutionNamespaceSelectorMatchExpressions", typing.Dict[builtins.str, typing.Any]]]] = None,
        match_labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''A label query over the set of namespaces that the term applies to.

        The term is applied to the union of the namespaces selected by this field
        and the ones listed in the namespaces field.
        null selector and null or empty namespaces list means "this pod's namespace".
        An empty selector ({}) matches all namespaces.

        :param match_expressions: matchExpressions is a list of label selector requirements. The requirements are ANDed.
        :param match_labels: matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityRequiredDuringSchedulingIgnoredDuringExecutionNamespaceSelector
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__afb631a07dbef3bb9de194e0d35bac91d19f71d9702b1ebfe85b02b6668b884b)
            check_type(argname="argument match_expressions", value=match_expressions, expected_type=type_hints["match_expressions"])
            check_type(argname="argument match_labels", value=match_labels, expected_type=type_hints["match_labels"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if match_expressions is not None:
            self._values["match_expressions"] = match_expressions
        if match_labels is not None:
            self._values["match_labels"] = match_labels

    @builtins.property
    def match_expressions(
        self,
    ) -> typing.Optional[typing.List["ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityRequiredDuringSchedulingIgnoredDuringExecutionNamespaceSelectorMatchExpressions"]]:
        '''matchExpressions is a list of label selector requirements.

        The requirements are ANDed.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityRequiredDuringSchedulingIgnoredDuringExecutionNamespaceSelector#matchExpressions
        '''
        result = self._values.get("match_expressions")
        return typing.cast(typing.Optional[typing.List["ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityRequiredDuringSchedulingIgnoredDuringExecutionNamespaceSelectorMatchExpressions"]], result)

    @builtins.property
    def match_labels(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''matchLabels is a map of {key,value} pairs.

        A single {key,value} in the matchLabels
        map is equivalent to an element of matchExpressions, whose key field is "key", the
        operator is "In", and the values array contains only "value". The requirements are ANDed.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityRequiredDuringSchedulingIgnoredDuringExecutionNamespaceSelector#matchLabels
        '''
        result = self._values.get("match_labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityRequiredDuringSchedulingIgnoredDuringExecutionNamespaceSelector(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iocert-manageracme.ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityRequiredDuringSchedulingIgnoredDuringExecutionNamespaceSelectorMatchExpressions",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "operator": "operator", "values": "values"},
)
class ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityRequiredDuringSchedulingIgnoredDuringExecutionNamespaceSelectorMatchExpressions:
    def __init__(
        self,
        *,
        key: builtins.str,
        operator: builtins.str,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''A label selector requirement is a selector that contains values, a key, and an operator that relates the key and values.

        :param key: key is the label key that the selector applies to.
        :param operator: operator represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist.
        :param values: values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityRequiredDuringSchedulingIgnoredDuringExecutionNamespaceSelectorMatchExpressions
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__46a9dc59ee81a5e31dd81d4401422486e369f0ec7060c1c3532d9dc0f32cab1c)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "key": key,
            "operator": operator,
        }
        if values is not None:
            self._values["values"] = values

    @builtins.property
    def key(self) -> builtins.str:
        '''key is the label key that the selector applies to.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityRequiredDuringSchedulingIgnoredDuringExecutionNamespaceSelectorMatchExpressions#key
        '''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def operator(self) -> builtins.str:
        '''operator represents a key's relationship to a set of values.

        Valid operators are In, NotIn, Exists and DoesNotExist.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityRequiredDuringSchedulingIgnoredDuringExecutionNamespaceSelectorMatchExpressions#operator
        '''
        result = self._values.get("operator")
        assert result is not None, "Required property 'operator' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''values is an array of string values.

        If the operator is In or NotIn,
        the values array must be non-empty. If the operator is Exists or DoesNotExist,
        the values array must be empty. This array is replaced during a strategic
        merge patch.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityRequiredDuringSchedulingIgnoredDuringExecutionNamespaceSelectorMatchExpressions#values
        '''
        result = self._values.get("values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityRequiredDuringSchedulingIgnoredDuringExecutionNamespaceSelectorMatchExpressions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iocert-manageracme.ChallengeSpecSolverHttp01IngressPodTemplateSpecImagePullSecrets",
    jsii_struct_bases=[],
    name_mapping={"name": "name"},
)
class ChallengeSpecSolverHttp01IngressPodTemplateSpecImagePullSecrets:
    def __init__(self, *, name: typing.Optional[builtins.str] = None) -> None:
        '''LocalObjectReference contains enough information to let you locate the referenced object inside the same namespace.

        :param name: Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecImagePullSecrets
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__32a41fbca1e0ee7a0388f7fc90a14cbf957c964182675b9de345a121f798dc44)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name of the referent.

        This field is effectively required, but due to backwards compatibility is
        allowed to be empty. Instances of this type with an empty value here are
        almost certainly wrong.
        More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecImagePullSecrets#name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ChallengeSpecSolverHttp01IngressPodTemplateSpecImagePullSecrets(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iocert-manageracme.ChallengeSpecSolverHttp01IngressPodTemplateSpecSecurityContext",
    jsii_struct_bases=[],
    name_mapping={
        "fs_group": "fsGroup",
        "fs_group_change_policy": "fsGroupChangePolicy",
        "run_as_group": "runAsGroup",
        "run_as_non_root": "runAsNonRoot",
        "run_as_user": "runAsUser",
        "seccomp_profile": "seccompProfile",
        "se_linux_options": "seLinuxOptions",
        "supplemental_groups": "supplementalGroups",
        "sysctls": "sysctls",
    },
)
class ChallengeSpecSolverHttp01IngressPodTemplateSpecSecurityContext:
    def __init__(
        self,
        *,
        fs_group: typing.Optional[jsii.Number] = None,
        fs_group_change_policy: typing.Optional[builtins.str] = None,
        run_as_group: typing.Optional[jsii.Number] = None,
        run_as_non_root: typing.Optional[builtins.bool] = None,
        run_as_user: typing.Optional[jsii.Number] = None,
        seccomp_profile: typing.Optional[typing.Union["ChallengeSpecSolverHttp01IngressPodTemplateSpecSecurityContextSeccompProfile", typing.Dict[builtins.str, typing.Any]]] = None,
        se_linux_options: typing.Optional[typing.Union["ChallengeSpecSolverHttp01IngressPodTemplateSpecSecurityContextSeLinuxOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        supplemental_groups: typing.Optional[typing.Sequence[jsii.Number]] = None,
        sysctls: typing.Optional[typing.Sequence[typing.Union["ChallengeSpecSolverHttp01IngressPodTemplateSpecSecurityContextSysctls", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''If specified, the pod's security context.

        :param fs_group: A special supplemental group that applies to all containers in a pod. Some volume types allow the Kubelet to change the ownership of that volume to be owned by the pod: 1. The owning GID will be the FSGroup 2. The setgid bit is set (new files created in the volume will be owned by FSGroup) 3. The permission bits are OR'd with rw-rw---- If unset, the Kubelet will not modify the ownership and permissions of any volume. Note that this field cannot be set when spec.os.name is windows.
        :param fs_group_change_policy: fsGroupChangePolicy defines behavior of changing ownership and permission of the volume before being exposed inside Pod. This field will only apply to volume types which support fsGroup based ownership(and permissions). It will have no effect on ephemeral volume types such as: secret, configmaps and emptydir. Valid values are "OnRootMismatch" and "Always". If not specified, "Always" is used. Note that this field cannot be set when spec.os.name is windows.
        :param run_as_group: The GID to run the entrypoint of the container process. Uses runtime default if unset. May also be set in SecurityContext. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence for that container. Note that this field cannot be set when spec.os.name is windows.
        :param run_as_non_root: Indicates that the container must run as a non-root user. If true, the Kubelet will validate the image at runtime to ensure that it does not run as UID 0 (root) and fail to start the container if it does. If unset or false, no such validation will be performed. May also be set in SecurityContext. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.
        :param run_as_user: The UID to run the entrypoint of the container process. Defaults to user specified in image metadata if unspecified. May also be set in SecurityContext. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence for that container. Note that this field cannot be set when spec.os.name is windows. Default: user specified in image metadata if unspecified.
        :param seccomp_profile: The seccomp options to use by the containers in this pod. Note that this field cannot be set when spec.os.name is windows.
        :param se_linux_options: The SELinux context to be applied to all containers. If unspecified, the container runtime will allocate a random SELinux context for each container. May also be set in SecurityContext. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence for that container. Note that this field cannot be set when spec.os.name is windows.
        :param supplemental_groups: A list of groups applied to the first process run in each container, in addition to the container's primary GID, the fsGroup (if specified), and group memberships defined in the container image for the uid of the container process. If unspecified, no additional groups are added to any container. Note that group memberships defined in the container image for the uid of the container process are still effective, even if they are not included in this list. Note that this field cannot be set when spec.os.name is windows.
        :param sysctls: Sysctls hold a list of namespaced sysctls used for the pod. Pods with unsupported sysctls (by the container runtime) might fail to launch. Note that this field cannot be set when spec.os.name is windows.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecSecurityContext
        '''
        if isinstance(seccomp_profile, dict):
            seccomp_profile = ChallengeSpecSolverHttp01IngressPodTemplateSpecSecurityContextSeccompProfile(**seccomp_profile)
        if isinstance(se_linux_options, dict):
            se_linux_options = ChallengeSpecSolverHttp01IngressPodTemplateSpecSecurityContextSeLinuxOptions(**se_linux_options)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a1502840d844972e98aea64200d5a094b40bdcbc97c9c1c421975cc1614ba223)
            check_type(argname="argument fs_group", value=fs_group, expected_type=type_hints["fs_group"])
            check_type(argname="argument fs_group_change_policy", value=fs_group_change_policy, expected_type=type_hints["fs_group_change_policy"])
            check_type(argname="argument run_as_group", value=run_as_group, expected_type=type_hints["run_as_group"])
            check_type(argname="argument run_as_non_root", value=run_as_non_root, expected_type=type_hints["run_as_non_root"])
            check_type(argname="argument run_as_user", value=run_as_user, expected_type=type_hints["run_as_user"])
            check_type(argname="argument seccomp_profile", value=seccomp_profile, expected_type=type_hints["seccomp_profile"])
            check_type(argname="argument se_linux_options", value=se_linux_options, expected_type=type_hints["se_linux_options"])
            check_type(argname="argument supplemental_groups", value=supplemental_groups, expected_type=type_hints["supplemental_groups"])
            check_type(argname="argument sysctls", value=sysctls, expected_type=type_hints["sysctls"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if fs_group is not None:
            self._values["fs_group"] = fs_group
        if fs_group_change_policy is not None:
            self._values["fs_group_change_policy"] = fs_group_change_policy
        if run_as_group is not None:
            self._values["run_as_group"] = run_as_group
        if run_as_non_root is not None:
            self._values["run_as_non_root"] = run_as_non_root
        if run_as_user is not None:
            self._values["run_as_user"] = run_as_user
        if seccomp_profile is not None:
            self._values["seccomp_profile"] = seccomp_profile
        if se_linux_options is not None:
            self._values["se_linux_options"] = se_linux_options
        if supplemental_groups is not None:
            self._values["supplemental_groups"] = supplemental_groups
        if sysctls is not None:
            self._values["sysctls"] = sysctls

    @builtins.property
    def fs_group(self) -> typing.Optional[jsii.Number]:
        '''A special supplemental group that applies to all containers in a pod.

        Some volume types allow the Kubelet to change the ownership of that volume
        to be owned by the pod:

        1. The owning GID will be the FSGroup
        2. The setgid bit is set (new files created in the volume will be owned by FSGroup)
        3. The permission bits are OR'd with rw-rw----

        If unset, the Kubelet will not modify the ownership and permissions of any volume.
        Note that this field cannot be set when spec.os.name is windows.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecSecurityContext#fsGroup
        '''
        result = self._values.get("fs_group")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def fs_group_change_policy(self) -> typing.Optional[builtins.str]:
        '''fsGroupChangePolicy defines behavior of changing ownership and permission of the volume before being exposed inside Pod.

        This field will only apply to
        volume types which support fsGroup based ownership(and permissions).
        It will have no effect on ephemeral volume types such as: secret, configmaps
        and emptydir.
        Valid values are "OnRootMismatch" and "Always". If not specified, "Always" is used.
        Note that this field cannot be set when spec.os.name is windows.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecSecurityContext#fsGroupChangePolicy
        '''
        result = self._values.get("fs_group_change_policy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def run_as_group(self) -> typing.Optional[jsii.Number]:
        '''The GID to run the entrypoint of the container process.

        Uses runtime default if unset.
        May also be set in SecurityContext.  If set in both SecurityContext and
        PodSecurityContext, the value specified in SecurityContext takes precedence
        for that container.
        Note that this field cannot be set when spec.os.name is windows.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecSecurityContext#runAsGroup
        '''
        result = self._values.get("run_as_group")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def run_as_non_root(self) -> typing.Optional[builtins.bool]:
        '''Indicates that the container must run as a non-root user.

        If true, the Kubelet will validate the image at runtime to ensure that it
        does not run as UID 0 (root) and fail to start the container if it does.
        If unset or false, no such validation will be performed.
        May also be set in SecurityContext.  If set in both SecurityContext and
        PodSecurityContext, the value specified in SecurityContext takes precedence.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecSecurityContext#runAsNonRoot
        '''
        result = self._values.get("run_as_non_root")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def run_as_user(self) -> typing.Optional[jsii.Number]:
        '''The UID to run the entrypoint of the container process.

        Defaults to user specified in image metadata if unspecified.
        May also be set in SecurityContext.  If set in both SecurityContext and
        PodSecurityContext, the value specified in SecurityContext takes precedence
        for that container.
        Note that this field cannot be set when spec.os.name is windows.

        :default: user specified in image metadata if unspecified.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecSecurityContext#runAsUser
        '''
        result = self._values.get("run_as_user")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def seccomp_profile(
        self,
    ) -> typing.Optional["ChallengeSpecSolverHttp01IngressPodTemplateSpecSecurityContextSeccompProfile"]:
        '''The seccomp options to use by the containers in this pod.

        Note that this field cannot be set when spec.os.name is windows.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecSecurityContext#seccompProfile
        '''
        result = self._values.get("seccomp_profile")
        return typing.cast(typing.Optional["ChallengeSpecSolverHttp01IngressPodTemplateSpecSecurityContextSeccompProfile"], result)

    @builtins.property
    def se_linux_options(
        self,
    ) -> typing.Optional["ChallengeSpecSolverHttp01IngressPodTemplateSpecSecurityContextSeLinuxOptions"]:
        '''The SELinux context to be applied to all containers.

        If unspecified, the container runtime will allocate a random SELinux context for each
        container.  May also be set in SecurityContext.  If set in
        both SecurityContext and PodSecurityContext, the value specified in SecurityContext
        takes precedence for that container.
        Note that this field cannot be set when spec.os.name is windows.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecSecurityContext#seLinuxOptions
        '''
        result = self._values.get("se_linux_options")
        return typing.cast(typing.Optional["ChallengeSpecSolverHttp01IngressPodTemplateSpecSecurityContextSeLinuxOptions"], result)

    @builtins.property
    def supplemental_groups(self) -> typing.Optional[typing.List[jsii.Number]]:
        '''A list of groups applied to the first process run in each container, in addition to the container's primary GID, the fsGroup (if specified), and group memberships defined in the container image for the uid of the container process.

        If unspecified,
        no additional groups are added to any container. Note that group memberships
        defined in the container image for the uid of the container process are still effective,
        even if they are not included in this list.
        Note that this field cannot be set when spec.os.name is windows.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecSecurityContext#supplementalGroups
        '''
        result = self._values.get("supplemental_groups")
        return typing.cast(typing.Optional[typing.List[jsii.Number]], result)

    @builtins.property
    def sysctls(
        self,
    ) -> typing.Optional[typing.List["ChallengeSpecSolverHttp01IngressPodTemplateSpecSecurityContextSysctls"]]:
        '''Sysctls hold a list of namespaced sysctls used for the pod.

        Pods with unsupported
        sysctls (by the container runtime) might fail to launch.
        Note that this field cannot be set when spec.os.name is windows.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecSecurityContext#sysctls
        '''
        result = self._values.get("sysctls")
        return typing.cast(typing.Optional[typing.List["ChallengeSpecSolverHttp01IngressPodTemplateSpecSecurityContextSysctls"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ChallengeSpecSolverHttp01IngressPodTemplateSpecSecurityContext(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iocert-manageracme.ChallengeSpecSolverHttp01IngressPodTemplateSpecSecurityContextSeLinuxOptions",
    jsii_struct_bases=[],
    name_mapping={"level": "level", "role": "role", "type": "type", "user": "user"},
)
class ChallengeSpecSolverHttp01IngressPodTemplateSpecSecurityContextSeLinuxOptions:
    def __init__(
        self,
        *,
        level: typing.Optional[builtins.str] = None,
        role: typing.Optional[builtins.str] = None,
        type: typing.Optional[builtins.str] = None,
        user: typing.Optional[builtins.str] = None,
    ) -> None:
        '''The SELinux context to be applied to all containers.

        If unspecified, the container runtime will allocate a random SELinux context for each
        container.  May also be set in SecurityContext.  If set in
        both SecurityContext and PodSecurityContext, the value specified in SecurityContext
        takes precedence for that container.
        Note that this field cannot be set when spec.os.name is windows.

        :param level: Level is SELinux level label that applies to the container.
        :param role: Role is a SELinux role label that applies to the container.
        :param type: Type is a SELinux type label that applies to the container.
        :param user: User is a SELinux user label that applies to the container.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecSecurityContextSeLinuxOptions
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e46a61acbd13fdeed11939e876e7c3b53c8e69007d8d06183055ff9589a0ebb2)
            check_type(argname="argument level", value=level, expected_type=type_hints["level"])
            check_type(argname="argument role", value=role, expected_type=type_hints["role"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument user", value=user, expected_type=type_hints["user"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if level is not None:
            self._values["level"] = level
        if role is not None:
            self._values["role"] = role
        if type is not None:
            self._values["type"] = type
        if user is not None:
            self._values["user"] = user

    @builtins.property
    def level(self) -> typing.Optional[builtins.str]:
        '''Level is SELinux level label that applies to the container.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecSecurityContextSeLinuxOptions#level
        '''
        result = self._values.get("level")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def role(self) -> typing.Optional[builtins.str]:
        '''Role is a SELinux role label that applies to the container.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecSecurityContextSeLinuxOptions#role
        '''
        result = self._values.get("role")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''Type is a SELinux type label that applies to the container.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecSecurityContextSeLinuxOptions#type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def user(self) -> typing.Optional[builtins.str]:
        '''User is a SELinux user label that applies to the container.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecSecurityContextSeLinuxOptions#user
        '''
        result = self._values.get("user")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ChallengeSpecSolverHttp01IngressPodTemplateSpecSecurityContextSeLinuxOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iocert-manageracme.ChallengeSpecSolverHttp01IngressPodTemplateSpecSecurityContextSeccompProfile",
    jsii_struct_bases=[],
    name_mapping={"type": "type", "localhost_profile": "localhostProfile"},
)
class ChallengeSpecSolverHttp01IngressPodTemplateSpecSecurityContextSeccompProfile:
    def __init__(
        self,
        *,
        type: builtins.str,
        localhost_profile: typing.Optional[builtins.str] = None,
    ) -> None:
        '''The seccomp options to use by the containers in this pod.

        Note that this field cannot be set when spec.os.name is windows.

        :param type: type indicates which kind of seccomp profile will be applied. Valid options are:. Localhost - a profile defined in a file on the node should be used. RuntimeDefault - the container runtime default profile should be used. Unconfined - no profile should be applied.
        :param localhost_profile: localhostProfile indicates a profile defined in a file on the node should be used. The profile must be preconfigured on the node to work. Must be a descending path, relative to the kubelet's configured seccomp profile location. Must be set if type is "Localhost". Must NOT be set for any other type.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecSecurityContextSeccompProfile
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__41eca06f58dece1bb4992cfac597e9b57daeee44a2b049906fbd4050c7f61b8c)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument localhost_profile", value=localhost_profile, expected_type=type_hints["localhost_profile"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "type": type,
        }
        if localhost_profile is not None:
            self._values["localhost_profile"] = localhost_profile

    @builtins.property
    def type(self) -> builtins.str:
        '''type indicates which kind of seccomp profile will be applied. Valid options are:.

        Localhost - a profile defined in a file on the node should be used.
        RuntimeDefault - the container runtime default profile should be used.
        Unconfined - no profile should be applied.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecSecurityContextSeccompProfile#type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def localhost_profile(self) -> typing.Optional[builtins.str]:
        '''localhostProfile indicates a profile defined in a file on the node should be used.

        The profile must be preconfigured on the node to work.
        Must be a descending path, relative to the kubelet's configured seccomp profile location.
        Must be set if type is "Localhost". Must NOT be set for any other type.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecSecurityContextSeccompProfile#localhostProfile
        '''
        result = self._values.get("localhost_profile")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ChallengeSpecSolverHttp01IngressPodTemplateSpecSecurityContextSeccompProfile(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iocert-manageracme.ChallengeSpecSolverHttp01IngressPodTemplateSpecSecurityContextSysctls",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "value": "value"},
)
class ChallengeSpecSolverHttp01IngressPodTemplateSpecSecurityContextSysctls:
    def __init__(self, *, name: builtins.str, value: builtins.str) -> None:
        '''Sysctl defines a kernel parameter to be set.

        :param name: Name of a property to set.
        :param value: Value of a property to set.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecSecurityContextSysctls
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__25f6cbd52a64d6239ffd846f6525fb9cd5e8486ae29b1ac2d6cc264d7b292404)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "value": value,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''Name of a property to set.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecSecurityContextSysctls#name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        '''Value of a property to set.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecSecurityContextSysctls#value
        '''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ChallengeSpecSolverHttp01IngressPodTemplateSpecSecurityContextSysctls(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iocert-manageracme.ChallengeSpecSolverHttp01IngressPodTemplateSpecTolerations",
    jsii_struct_bases=[],
    name_mapping={
        "effect": "effect",
        "key": "key",
        "operator": "operator",
        "toleration_seconds": "tolerationSeconds",
        "value": "value",
    },
)
class ChallengeSpecSolverHttp01IngressPodTemplateSpecTolerations:
    def __init__(
        self,
        *,
        effect: typing.Optional[builtins.str] = None,
        key: typing.Optional[builtins.str] = None,
        operator: typing.Optional[builtins.str] = None,
        toleration_seconds: typing.Optional[jsii.Number] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''The pod this Toleration is attached to tolerates any taint that matches the triple <key,value,effect> using the matching operator .

        :param effect: Effect indicates the taint effect to match. Empty means match all taint effects. When specified, allowed values are NoSchedule, PreferNoSchedule and NoExecute.
        :param key: Key is the taint key that the toleration applies to. Empty means match all taint keys. If the key is empty, operator must be Exists; this combination means to match all values and all keys.
        :param operator: Operator represents a key's relationship to the value. Valid operators are Exists and Equal. Defaults to Equal. Exists is equivalent to wildcard for value, so that a pod can tolerate all taints of a particular category. Default: Equal.
        :param toleration_seconds: TolerationSeconds represents the period of time the toleration (which must be of effect NoExecute, otherwise this field is ignored) tolerates the taint. By default, it is not set, which means tolerate the taint forever (do not evict). Zero and negative values will be treated as 0 (evict immediately) by the system.
        :param value: Value is the taint value the toleration matches to. If the operator is Exists, the value should be empty, otherwise just a regular string.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecTolerations
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f98eb15901a8d2b33cdf610c5770e4235960270776ae3ccbf5fb9e2b54588457)
            check_type(argname="argument effect", value=effect, expected_type=type_hints["effect"])
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
            check_type(argname="argument toleration_seconds", value=toleration_seconds, expected_type=type_hints["toleration_seconds"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if effect is not None:
            self._values["effect"] = effect
        if key is not None:
            self._values["key"] = key
        if operator is not None:
            self._values["operator"] = operator
        if toleration_seconds is not None:
            self._values["toleration_seconds"] = toleration_seconds
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def effect(self) -> typing.Optional[builtins.str]:
        '''Effect indicates the taint effect to match.

        Empty means match all taint effects.
        When specified, allowed values are NoSchedule, PreferNoSchedule and NoExecute.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecTolerations#effect
        '''
        result = self._values.get("effect")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''Key is the taint key that the toleration applies to.

        Empty means match all taint keys.
        If the key is empty, operator must be Exists; this combination means to match all values and all keys.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecTolerations#key
        '''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def operator(self) -> typing.Optional[builtins.str]:
        '''Operator represents a key's relationship to the value.

        Valid operators are Exists and Equal. Defaults to Equal.
        Exists is equivalent to wildcard for value, so that a pod can
        tolerate all taints of a particular category.

        :default: Equal.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecTolerations#operator
        '''
        result = self._values.get("operator")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def toleration_seconds(self) -> typing.Optional[jsii.Number]:
        '''TolerationSeconds represents the period of time the toleration (which must be of effect NoExecute, otherwise this field is ignored) tolerates the taint.

        By default,
        it is not set, which means tolerate the taint forever (do not evict). Zero and
        negative values will be treated as 0 (evict immediately) by the system.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecTolerations#tolerationSeconds
        '''
        result = self._values.get("toleration_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''Value is the taint value the toleration matches to.

        If the operator is Exists, the value should be empty, otherwise just a regular string.

        :schema: ChallengeSpecSolverHttp01IngressPodTemplateSpecTolerations#value
        '''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ChallengeSpecSolverHttp01IngressPodTemplateSpecTolerations(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iocert-manageracme.ChallengeSpecSolverSelector",
    jsii_struct_bases=[],
    name_mapping={
        "dns_names": "dnsNames",
        "dns_zones": "dnsZones",
        "match_labels": "matchLabels",
    },
)
class ChallengeSpecSolverSelector:
    def __init__(
        self,
        *,
        dns_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        dns_zones: typing.Optional[typing.Sequence[builtins.str]] = None,
        match_labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Selector selects a set of DNSNames on the Certificate resource that should be solved using this challenge solver.

        If not specified, the solver will be treated as the 'default' solver
        with the lowest priority, i.e. if any other solver has a more specific
        match, it will be used instead.

        :param dns_names: List of DNSNames that this solver will be used to solve. If specified and a match is found, a dnsNames selector will take precedence over a dnsZones selector. If multiple solvers match with the same dnsNames value, the solver with the most matching labels in matchLabels will be selected. If neither has more matches, the solver defined earlier in the list will be selected.
        :param dns_zones: List of DNSZones that this solver will be used to solve. The most specific DNS zone match specified here will take precedence over other DNS zone matches, so a solver specifying sys.example.com will be selected over one specifying example.com for the domain www.sys.example.com. If multiple solvers match with the same dnsZones value, the solver with the most matching labels in matchLabels will be selected. If neither has more matches, the solver defined earlier in the list will be selected.
        :param match_labels: A label selector that is used to refine the set of certificate's that this challenge solver will apply to.

        :schema: ChallengeSpecSolverSelector
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4b23cc54499bb6a3fb663f4f24d6b5d8847c45075e56778f3ceaa474d6f163fe)
            check_type(argname="argument dns_names", value=dns_names, expected_type=type_hints["dns_names"])
            check_type(argname="argument dns_zones", value=dns_zones, expected_type=type_hints["dns_zones"])
            check_type(argname="argument match_labels", value=match_labels, expected_type=type_hints["match_labels"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if dns_names is not None:
            self._values["dns_names"] = dns_names
        if dns_zones is not None:
            self._values["dns_zones"] = dns_zones
        if match_labels is not None:
            self._values["match_labels"] = match_labels

    @builtins.property
    def dns_names(self) -> typing.Optional[typing.List[builtins.str]]:
        '''List of DNSNames that this solver will be used to solve.

        If specified and a match is found, a dnsNames selector will take
        precedence over a dnsZones selector.
        If multiple solvers match with the same dnsNames value, the solver
        with the most matching labels in matchLabels will be selected.
        If neither has more matches, the solver defined earlier in the list
        will be selected.

        :schema: ChallengeSpecSolverSelector#dnsNames
        '''
        result = self._values.get("dns_names")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def dns_zones(self) -> typing.Optional[typing.List[builtins.str]]:
        '''List of DNSZones that this solver will be used to solve.

        The most specific DNS zone match specified here will take precedence
        over other DNS zone matches, so a solver specifying sys.example.com
        will be selected over one specifying example.com for the domain
        www.sys.example.com.
        If multiple solvers match with the same dnsZones value, the solver
        with the most matching labels in matchLabels will be selected.
        If neither has more matches, the solver defined earlier in the list
        will be selected.

        :schema: ChallengeSpecSolverSelector#dnsZones
        '''
        result = self._values.get("dns_zones")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def match_labels(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''A label selector that is used to refine the set of certificate's that this challenge solver will apply to.

        :schema: ChallengeSpecSolverSelector#matchLabels
        '''
        result = self._values.get("match_labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ChallengeSpecSolverSelector(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="iocert-manageracme.ChallengeSpecType")
class ChallengeSpecType(enum.Enum):
    '''The type of ACME challenge this resource represents.

    One of "HTTP-01" or "DNS-01".

    :schema: ChallengeSpecType
    '''

    HTTP_HYPHEN_01 = "HTTP_HYPHEN_01"
    '''HTTP-01.'''
    DNS_HYPHEN_01 = "DNS_HYPHEN_01"
    '''DNS-01.'''


class Order(
    _cdk8s_d3d9af27.ApiObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="iocert-manageracme.Order",
):
    '''Order is a type to represent an Order with an ACME server.

    :schema: Order
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        metadata: typing.Union[_cdk8s_d3d9af27.ApiObjectMetadata, typing.Dict[builtins.str, typing.Any]],
        spec: typing.Union["OrderSpec", typing.Dict[builtins.str, typing.Any]],
    ) -> None:
        '''Defines a "Order" API object.

        :param scope: the scope in which to define this object.
        :param id: a scope-local name for the object.
        :param metadata: 
        :param spec: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__34bcee1b050f29f7d741f3476b67636108df8a8f593c0584f3c343237e6e2e7e)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = OrderProps(metadata=metadata, spec=spec)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="manifest")
    @builtins.classmethod
    def manifest(
        cls,
        *,
        metadata: typing.Union[_cdk8s_d3d9af27.ApiObjectMetadata, typing.Dict[builtins.str, typing.Any]],
        spec: typing.Union["OrderSpec", typing.Dict[builtins.str, typing.Any]],
    ) -> typing.Any:
        '''Renders a Kubernetes manifest for "Order".

        This can be used to inline resource manifests inside other objects (e.g. as templates).

        :param metadata: 
        :param spec: 
        '''
        props = OrderProps(metadata=metadata, spec=spec)

        return typing.cast(typing.Any, jsii.sinvoke(cls, "manifest", [props]))

    @jsii.member(jsii_name="toJson")
    def to_json(self) -> typing.Any:
        '''Renders the object to Kubernetes JSON.'''
        return typing.cast(typing.Any, jsii.invoke(self, "toJson", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="GVK")
    def GVK(cls) -> _cdk8s_d3d9af27.GroupVersionKind:
        '''Returns the apiVersion and kind for "Order".'''
        return typing.cast(_cdk8s_d3d9af27.GroupVersionKind, jsii.sget(cls, "GVK"))


@jsii.data_type(
    jsii_type="iocert-manageracme.OrderProps",
    jsii_struct_bases=[],
    name_mapping={"metadata": "metadata", "spec": "spec"},
)
class OrderProps:
    def __init__(
        self,
        *,
        metadata: typing.Union[_cdk8s_d3d9af27.ApiObjectMetadata, typing.Dict[builtins.str, typing.Any]],
        spec: typing.Union["OrderSpec", typing.Dict[builtins.str, typing.Any]],
    ) -> None:
        '''Order is a type to represent an Order with an ACME server.

        :param metadata: 
        :param spec: 

        :schema: Order
        '''
        if isinstance(metadata, dict):
            metadata = _cdk8s_d3d9af27.ApiObjectMetadata(**metadata)
        if isinstance(spec, dict):
            spec = OrderSpec(**spec)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d305eba977d638ba7ddcabcd7e0eaac0b639c9d0bc92c822368b502267ef3775)
            check_type(argname="argument metadata", value=metadata, expected_type=type_hints["metadata"])
            check_type(argname="argument spec", value=spec, expected_type=type_hints["spec"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "metadata": metadata,
            "spec": spec,
        }

    @builtins.property
    def metadata(self) -> _cdk8s_d3d9af27.ApiObjectMetadata:
        '''
        :schema: Order#metadata
        '''
        result = self._values.get("metadata")
        assert result is not None, "Required property 'metadata' is missing"
        return typing.cast(_cdk8s_d3d9af27.ApiObjectMetadata, result)

    @builtins.property
    def spec(self) -> "OrderSpec":
        '''
        :schema: Order#spec
        '''
        result = self._values.get("spec")
        assert result is not None, "Required property 'spec' is missing"
        return typing.cast("OrderSpec", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OrderProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iocert-manageracme.OrderSpec",
    jsii_struct_bases=[],
    name_mapping={
        "issuer_ref": "issuerRef",
        "request": "request",
        "common_name": "commonName",
        "dns_names": "dnsNames",
        "duration": "duration",
        "ip_addresses": "ipAddresses",
    },
)
class OrderSpec:
    def __init__(
        self,
        *,
        issuer_ref: typing.Union["OrderSpecIssuerRef", typing.Dict[builtins.str, typing.Any]],
        request: builtins.str,
        common_name: typing.Optional[builtins.str] = None,
        dns_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        duration: typing.Optional[builtins.str] = None,
        ip_addresses: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param issuer_ref: IssuerRef references a properly configured ACME-type Issuer which should be used to create this Order. If the Issuer does not exist, processing will be retried. If the Issuer is not an 'ACME' Issuer, an error will be returned and the Order will be marked as failed.
        :param request: Certificate signing request bytes in DER encoding. This will be used when finalizing the order. This field must be set on the order.
        :param common_name: CommonName is the common name as specified on the DER encoded CSR. If specified, this value must also be present in ``dnsNames`` or ``ipAddresses``. This field must match the corresponding field on the DER encoded CSR.
        :param dns_names: DNSNames is a list of DNS names that should be included as part of the Order validation process. This field must match the corresponding field on the DER encoded CSR.
        :param duration: Duration is the duration for the not after date for the requested certificate. this is set on order creation as pe the ACME spec.
        :param ip_addresses: IPAddresses is a list of IP addresses that should be included as part of the Order validation process. This field must match the corresponding field on the DER encoded CSR.

        :schema: OrderSpec
        '''
        if isinstance(issuer_ref, dict):
            issuer_ref = OrderSpecIssuerRef(**issuer_ref)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b996931a2adb1f4b471e1fd158376a9d51ccc0564a05633d0caa0a7416787d14)
            check_type(argname="argument issuer_ref", value=issuer_ref, expected_type=type_hints["issuer_ref"])
            check_type(argname="argument request", value=request, expected_type=type_hints["request"])
            check_type(argname="argument common_name", value=common_name, expected_type=type_hints["common_name"])
            check_type(argname="argument dns_names", value=dns_names, expected_type=type_hints["dns_names"])
            check_type(argname="argument duration", value=duration, expected_type=type_hints["duration"])
            check_type(argname="argument ip_addresses", value=ip_addresses, expected_type=type_hints["ip_addresses"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "issuer_ref": issuer_ref,
            "request": request,
        }
        if common_name is not None:
            self._values["common_name"] = common_name
        if dns_names is not None:
            self._values["dns_names"] = dns_names
        if duration is not None:
            self._values["duration"] = duration
        if ip_addresses is not None:
            self._values["ip_addresses"] = ip_addresses

    @builtins.property
    def issuer_ref(self) -> "OrderSpecIssuerRef":
        '''IssuerRef references a properly configured ACME-type Issuer which should be used to create this Order.

        If the Issuer does not exist, processing will be retried.
        If the Issuer is not an 'ACME' Issuer, an error will be returned and the
        Order will be marked as failed.

        :schema: OrderSpec#issuerRef
        '''
        result = self._values.get("issuer_ref")
        assert result is not None, "Required property 'issuer_ref' is missing"
        return typing.cast("OrderSpecIssuerRef", result)

    @builtins.property
    def request(self) -> builtins.str:
        '''Certificate signing request bytes in DER encoding.

        This will be used when finalizing the order.
        This field must be set on the order.

        :schema: OrderSpec#request
        '''
        result = self._values.get("request")
        assert result is not None, "Required property 'request' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def common_name(self) -> typing.Optional[builtins.str]:
        '''CommonName is the common name as specified on the DER encoded CSR.

        If specified, this value must also be present in ``dnsNames`` or ``ipAddresses``.
        This field must match the corresponding field on the DER encoded CSR.

        :schema: OrderSpec#commonName
        '''
        result = self._values.get("common_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def dns_names(self) -> typing.Optional[typing.List[builtins.str]]:
        '''DNSNames is a list of DNS names that should be included as part of the Order validation process.

        This field must match the corresponding field on the DER encoded CSR.

        :schema: OrderSpec#dnsNames
        '''
        result = self._values.get("dns_names")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def duration(self) -> typing.Optional[builtins.str]:
        '''Duration is the duration for the not after date for the requested certificate.

        this is set on order creation as pe the ACME spec.

        :schema: OrderSpec#duration
        '''
        result = self._values.get("duration")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ip_addresses(self) -> typing.Optional[typing.List[builtins.str]]:
        '''IPAddresses is a list of IP addresses that should be included as part of the Order validation process.

        This field must match the corresponding field on the DER encoded CSR.

        :schema: OrderSpec#ipAddresses
        '''
        result = self._values.get("ip_addresses")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OrderSpec(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="iocert-manageracme.OrderSpecIssuerRef",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "group": "group", "kind": "kind"},
)
class OrderSpecIssuerRef:
    def __init__(
        self,
        *,
        name: builtins.str,
        group: typing.Optional[builtins.str] = None,
        kind: typing.Optional[builtins.str] = None,
    ) -> None:
        '''IssuerRef references a properly configured ACME-type Issuer which should be used to create this Order.

        If the Issuer does not exist, processing will be retried.
        If the Issuer is not an 'ACME' Issuer, an error will be returned and the
        Order will be marked as failed.

        :param name: Name of the resource being referred to.
        :param group: Group of the resource being referred to.
        :param kind: Kind of the resource being referred to.

        :schema: OrderSpecIssuerRef
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4675758fbb6e921cd2e91de67d2858460cab73f1393b0bfd785f01c9fdeaee6a)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument group", value=group, expected_type=type_hints["group"])
            check_type(argname="argument kind", value=kind, expected_type=type_hints["kind"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
        if group is not None:
            self._values["group"] = group
        if kind is not None:
            self._values["kind"] = kind

    @builtins.property
    def name(self) -> builtins.str:
        '''Name of the resource being referred to.

        :schema: OrderSpecIssuerRef#name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def group(self) -> typing.Optional[builtins.str]:
        '''Group of the resource being referred to.

        :schema: OrderSpecIssuerRef#group
        '''
        result = self._values.get("group")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kind(self) -> typing.Optional[builtins.str]:
        '''Kind of the resource being referred to.

        :schema: OrderSpecIssuerRef#kind
        '''
        result = self._values.get("kind")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OrderSpecIssuerRef(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "Challenge",
    "ChallengeProps",
    "ChallengeSpec",
    "ChallengeSpecIssuerRef",
    "ChallengeSpecSolver",
    "ChallengeSpecSolverDns01",
    "ChallengeSpecSolverDns01AcmeDns",
    "ChallengeSpecSolverDns01AcmeDnsAccountSecretRef",
    "ChallengeSpecSolverDns01Akamai",
    "ChallengeSpecSolverDns01AkamaiAccessTokenSecretRef",
    "ChallengeSpecSolverDns01AkamaiClientSecretSecretRef",
    "ChallengeSpecSolverDns01AkamaiClientTokenSecretRef",
    "ChallengeSpecSolverDns01AzureDns",
    "ChallengeSpecSolverDns01AzureDnsClientSecretSecretRef",
    "ChallengeSpecSolverDns01AzureDnsEnvironment",
    "ChallengeSpecSolverDns01AzureDnsManagedIdentity",
    "ChallengeSpecSolverDns01CloudDns",
    "ChallengeSpecSolverDns01CloudDnsServiceAccountSecretRef",
    "ChallengeSpecSolverDns01Cloudflare",
    "ChallengeSpecSolverDns01CloudflareApiKeySecretRef",
    "ChallengeSpecSolverDns01CloudflareApiTokenSecretRef",
    "ChallengeSpecSolverDns01CnameStrategy",
    "ChallengeSpecSolverDns01Digitalocean",
    "ChallengeSpecSolverDns01DigitaloceanTokenSecretRef",
    "ChallengeSpecSolverDns01Rfc2136",
    "ChallengeSpecSolverDns01Rfc2136TsigSecretSecretRef",
    "ChallengeSpecSolverDns01Route53",
    "ChallengeSpecSolverDns01Route53AccessKeyIdSecretRef",
    "ChallengeSpecSolverDns01Route53Auth",
    "ChallengeSpecSolverDns01Route53AuthKubernetes",
    "ChallengeSpecSolverDns01Route53AuthKubernetesServiceAccountRef",
    "ChallengeSpecSolverDns01Route53SecretAccessKeySecretRef",
    "ChallengeSpecSolverDns01Webhook",
    "ChallengeSpecSolverHttp01",
    "ChallengeSpecSolverHttp01GatewayHttpRoute",
    "ChallengeSpecSolverHttp01GatewayHttpRouteParentRefs",
    "ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplate",
    "ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateMetadata",
    "ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpec",
    "ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinity",
    "ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityNodeAffinity",
    "ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecution",
    "ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecutionPreference",
    "ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecutionPreferenceMatchExpressions",
    "ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecutionPreferenceMatchFields",
    "ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecution",
    "ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionNodeSelectorTerms",
    "ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionNodeSelectorTermsMatchExpressions",
    "ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionNodeSelectorTermsMatchFields",
    "ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAffinity",
    "ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecution",
    "ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTerm",
    "ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermLabelSelector",
    "ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermLabelSelectorMatchExpressions",
    "ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermNamespaceSelector",
    "ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermNamespaceSelectorMatchExpressions",
    "ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAffinityRequiredDuringSchedulingIgnoredDuringExecution",
    "ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAffinityRequiredDuringSchedulingIgnoredDuringExecutionLabelSelector",
    "ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAffinityRequiredDuringSchedulingIgnoredDuringExecutionLabelSelectorMatchExpressions",
    "ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAffinityRequiredDuringSchedulingIgnoredDuringExecutionNamespaceSelector",
    "ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAffinityRequiredDuringSchedulingIgnoredDuringExecutionNamespaceSelectorMatchExpressions",
    "ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAntiAffinity",
    "ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecution",
    "ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTerm",
    "ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermLabelSelector",
    "ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermLabelSelectorMatchExpressions",
    "ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermNamespaceSelector",
    "ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermNamespaceSelectorMatchExpressions",
    "ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAntiAffinityRequiredDuringSchedulingIgnoredDuringExecution",
    "ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAntiAffinityRequiredDuringSchedulingIgnoredDuringExecutionLabelSelector",
    "ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAntiAffinityRequiredDuringSchedulingIgnoredDuringExecutionLabelSelectorMatchExpressions",
    "ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAntiAffinityRequiredDuringSchedulingIgnoredDuringExecutionNamespaceSelector",
    "ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAntiAffinityRequiredDuringSchedulingIgnoredDuringExecutionNamespaceSelectorMatchExpressions",
    "ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecImagePullSecrets",
    "ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecSecurityContext",
    "ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecSecurityContextSeLinuxOptions",
    "ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecSecurityContextSeccompProfile",
    "ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecSecurityContextSysctls",
    "ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecTolerations",
    "ChallengeSpecSolverHttp01Ingress",
    "ChallengeSpecSolverHttp01IngressIngressTemplate",
    "ChallengeSpecSolverHttp01IngressIngressTemplateMetadata",
    "ChallengeSpecSolverHttp01IngressPodTemplate",
    "ChallengeSpecSolverHttp01IngressPodTemplateMetadata",
    "ChallengeSpecSolverHttp01IngressPodTemplateSpec",
    "ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinity",
    "ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinity",
    "ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecution",
    "ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecutionPreference",
    "ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecutionPreferenceMatchExpressions",
    "ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecutionPreferenceMatchFields",
    "ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecution",
    "ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionNodeSelectorTerms",
    "ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionNodeSelectorTermsMatchExpressions",
    "ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionNodeSelectorTermsMatchFields",
    "ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinity",
    "ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecution",
    "ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTerm",
    "ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermLabelSelector",
    "ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermLabelSelectorMatchExpressions",
    "ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermNamespaceSelector",
    "ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermNamespaceSelectorMatchExpressions",
    "ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityRequiredDuringSchedulingIgnoredDuringExecution",
    "ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityRequiredDuringSchedulingIgnoredDuringExecutionLabelSelector",
    "ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityRequiredDuringSchedulingIgnoredDuringExecutionLabelSelectorMatchExpressions",
    "ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityRequiredDuringSchedulingIgnoredDuringExecutionNamespaceSelector",
    "ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityRequiredDuringSchedulingIgnoredDuringExecutionNamespaceSelectorMatchExpressions",
    "ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinity",
    "ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecution",
    "ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTerm",
    "ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermLabelSelector",
    "ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermLabelSelectorMatchExpressions",
    "ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermNamespaceSelector",
    "ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermNamespaceSelectorMatchExpressions",
    "ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityRequiredDuringSchedulingIgnoredDuringExecution",
    "ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityRequiredDuringSchedulingIgnoredDuringExecutionLabelSelector",
    "ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityRequiredDuringSchedulingIgnoredDuringExecutionLabelSelectorMatchExpressions",
    "ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityRequiredDuringSchedulingIgnoredDuringExecutionNamespaceSelector",
    "ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityRequiredDuringSchedulingIgnoredDuringExecutionNamespaceSelectorMatchExpressions",
    "ChallengeSpecSolverHttp01IngressPodTemplateSpecImagePullSecrets",
    "ChallengeSpecSolverHttp01IngressPodTemplateSpecSecurityContext",
    "ChallengeSpecSolverHttp01IngressPodTemplateSpecSecurityContextSeLinuxOptions",
    "ChallengeSpecSolverHttp01IngressPodTemplateSpecSecurityContextSeccompProfile",
    "ChallengeSpecSolverHttp01IngressPodTemplateSpecSecurityContextSysctls",
    "ChallengeSpecSolverHttp01IngressPodTemplateSpecTolerations",
    "ChallengeSpecSolverSelector",
    "ChallengeSpecType",
    "Order",
    "OrderProps",
    "OrderSpec",
    "OrderSpecIssuerRef",
]

publication.publish()

def _typecheckingstub__c9e7b67fe7fc10175a4d7deaeb248d18de0bbb75e0cf47708d0c404c856d36b1(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    metadata: typing.Union[_cdk8s_d3d9af27.ApiObjectMetadata, typing.Dict[builtins.str, typing.Any]],
    spec: typing.Union[ChallengeSpec, typing.Dict[builtins.str, typing.Any]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__21a9e1c772a1f0da2500f29eb767b45f194ed7c8956f6d35cb170c541e735509(
    *,
    metadata: typing.Union[_cdk8s_d3d9af27.ApiObjectMetadata, typing.Dict[builtins.str, typing.Any]],
    spec: typing.Union[ChallengeSpec, typing.Dict[builtins.str, typing.Any]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__207844d086707968e4012edfc78d0e652f5f4892740dd9d1a5f633a1d1324d45(
    *,
    authorization_url: builtins.str,
    dns_name: builtins.str,
    issuer_ref: typing.Union[ChallengeSpecIssuerRef, typing.Dict[builtins.str, typing.Any]],
    key: builtins.str,
    solver: typing.Union[ChallengeSpecSolver, typing.Dict[builtins.str, typing.Any]],
    token: builtins.str,
    type: ChallengeSpecType,
    url: builtins.str,
    wildcard: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bf94af1aaabe5ad431383ca2c1cbc6c63dc368710c72420f2fa90004b3da78b0(
    *,
    name: builtins.str,
    group: typing.Optional[builtins.str] = None,
    kind: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7fe91530e269d0e86c228348f7893c1cf5e61f7789b2dca4a58b181c4e324211(
    *,
    dns01: typing.Optional[typing.Union[ChallengeSpecSolverDns01, typing.Dict[builtins.str, typing.Any]]] = None,
    http01: typing.Optional[typing.Union[ChallengeSpecSolverHttp01, typing.Dict[builtins.str, typing.Any]]] = None,
    selector: typing.Optional[typing.Union[ChallengeSpecSolverSelector, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__142c470983c47888a0ad07b89f6066e68870d25c918279cc3c2bce30dd25f04c(
    *,
    acme_dns: typing.Optional[typing.Union[ChallengeSpecSolverDns01AcmeDns, typing.Dict[builtins.str, typing.Any]]] = None,
    akamai: typing.Optional[typing.Union[ChallengeSpecSolverDns01Akamai, typing.Dict[builtins.str, typing.Any]]] = None,
    azure_dns: typing.Optional[typing.Union[ChallengeSpecSolverDns01AzureDns, typing.Dict[builtins.str, typing.Any]]] = None,
    cloud_dns: typing.Optional[typing.Union[ChallengeSpecSolverDns01CloudDns, typing.Dict[builtins.str, typing.Any]]] = None,
    cloudflare: typing.Optional[typing.Union[ChallengeSpecSolverDns01Cloudflare, typing.Dict[builtins.str, typing.Any]]] = None,
    cname_strategy: typing.Optional[ChallengeSpecSolverDns01CnameStrategy] = None,
    digitalocean: typing.Optional[typing.Union[ChallengeSpecSolverDns01Digitalocean, typing.Dict[builtins.str, typing.Any]]] = None,
    rfc2136: typing.Optional[typing.Union[ChallengeSpecSolverDns01Rfc2136, typing.Dict[builtins.str, typing.Any]]] = None,
    route53: typing.Optional[typing.Union[ChallengeSpecSolverDns01Route53, typing.Dict[builtins.str, typing.Any]]] = None,
    webhook: typing.Optional[typing.Union[ChallengeSpecSolverDns01Webhook, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__21db0ea3ffdfe07fd48344501eb8ce6530983242b8be2bf699e0d915a0129fda(
    *,
    account_secret_ref: typing.Union[ChallengeSpecSolverDns01AcmeDnsAccountSecretRef, typing.Dict[builtins.str, typing.Any]],
    host: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__986030aa12ea799599fe8422f90cd82f8530e8664e66be261f1333fdcb063ba2(
    *,
    name: builtins.str,
    key: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__734e95330244f4212829fe485864844bf3a43524b395afbdb7a074350d789b00(
    *,
    access_token_secret_ref: typing.Union[ChallengeSpecSolverDns01AkamaiAccessTokenSecretRef, typing.Dict[builtins.str, typing.Any]],
    client_secret_secret_ref: typing.Union[ChallengeSpecSolverDns01AkamaiClientSecretSecretRef, typing.Dict[builtins.str, typing.Any]],
    client_token_secret_ref: typing.Union[ChallengeSpecSolverDns01AkamaiClientTokenSecretRef, typing.Dict[builtins.str, typing.Any]],
    service_consumer_domain: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__257e1438acbbc299ef2d6df55ccc7d2078ad4e13ead5c6d41b4fd0ecd2718a61(
    *,
    name: builtins.str,
    key: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e70693cc55de32af0b3ab9b24c3832c94eba49113cc0925dc71952ca1c01db42(
    *,
    name: builtins.str,
    key: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__776d36f7cda6b157c5d5a3f65e67ff629861adda10f1ec45ccc09c44caaa01be(
    *,
    name: builtins.str,
    key: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0c9f416728c3596e733c1b71ae04174983e3a388ddfd6d382db4fc61d5fd910a(
    *,
    resource_group_name: builtins.str,
    subscription_id: builtins.str,
    client_id: typing.Optional[builtins.str] = None,
    client_secret_secret_ref: typing.Optional[typing.Union[ChallengeSpecSolverDns01AzureDnsClientSecretSecretRef, typing.Dict[builtins.str, typing.Any]]] = None,
    environment: typing.Optional[ChallengeSpecSolverDns01AzureDnsEnvironment] = None,
    hosted_zone_name: typing.Optional[builtins.str] = None,
    managed_identity: typing.Optional[typing.Union[ChallengeSpecSolverDns01AzureDnsManagedIdentity, typing.Dict[builtins.str, typing.Any]]] = None,
    tenant_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__81efc815086edcc6e2a218249043f32bae8c25dc3499f00b976be78f97b297e3(
    *,
    name: builtins.str,
    key: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__75354e7c5ed12ae459903b20162ed781424cb666f5ffc8055d8454b256d9d047(
    *,
    client_id: typing.Optional[builtins.str] = None,
    resource_id: typing.Optional[builtins.str] = None,
    tenant_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__819643347ab362ace9c9e97d35cc6222cc568953d39007b282b7cc242a1a9075(
    *,
    project: builtins.str,
    hosted_zone_name: typing.Optional[builtins.str] = None,
    service_account_secret_ref: typing.Optional[typing.Union[ChallengeSpecSolverDns01CloudDnsServiceAccountSecretRef, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b2ef723db7f6487468dee108aff10a8190c97f734b1c32b82407ac1ba86477e6(
    *,
    name: builtins.str,
    key: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__18354a1c6f09f77d8ee3e6b15f576df12059d0e4e4b1bfa6211982da44e87d14(
    *,
    api_key_secret_ref: typing.Optional[typing.Union[ChallengeSpecSolverDns01CloudflareApiKeySecretRef, typing.Dict[builtins.str, typing.Any]]] = None,
    api_token_secret_ref: typing.Optional[typing.Union[ChallengeSpecSolverDns01CloudflareApiTokenSecretRef, typing.Dict[builtins.str, typing.Any]]] = None,
    email: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5436bd913867de2bc24a3933fe356518fd6c5e4243d1bcdc163bc2dfcf10cb06(
    *,
    name: builtins.str,
    key: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9a75677ce3e59cb343bbbaa112e9c83f123ceb805a0c4dcbaf92c339dce4c80e(
    *,
    name: builtins.str,
    key: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c9e736a96f44fcedb899e4f053b97f9aadf82bdc61f987147f813d3eb5253edd(
    *,
    token_secret_ref: typing.Union[ChallengeSpecSolverDns01DigitaloceanTokenSecretRef, typing.Dict[builtins.str, typing.Any]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__01f2c57e77addbe75dc86b4d371f50e479a6f9dc8aa791934442a075d6bfe5da(
    *,
    name: builtins.str,
    key: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__158fe4c810428e7ad9d57f33d26355d668258cf3c182eadd6959722c45eaaf6f(
    *,
    nameserver: builtins.str,
    tsig_algorithm: typing.Optional[builtins.str] = None,
    tsig_key_name: typing.Optional[builtins.str] = None,
    tsig_secret_secret_ref: typing.Optional[typing.Union[ChallengeSpecSolverDns01Rfc2136TsigSecretSecretRef, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aaae4e30208cda828258ac55090d346880712829510d2a7afecd39687c000996(
    *,
    name: builtins.str,
    key: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f2ce54f74f48a04e478bd66fba9cfbb31158b769cdf7f9177d19878c8a130b15(
    *,
    access_key_id: typing.Optional[builtins.str] = None,
    access_key_id_secret_ref: typing.Optional[typing.Union[ChallengeSpecSolverDns01Route53AccessKeyIdSecretRef, typing.Dict[builtins.str, typing.Any]]] = None,
    auth: typing.Optional[typing.Union[ChallengeSpecSolverDns01Route53Auth, typing.Dict[builtins.str, typing.Any]]] = None,
    hosted_zone_id: typing.Optional[builtins.str] = None,
    region: typing.Optional[builtins.str] = None,
    role: typing.Optional[builtins.str] = None,
    secret_access_key_secret_ref: typing.Optional[typing.Union[ChallengeSpecSolverDns01Route53SecretAccessKeySecretRef, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9b8062c5dc050e665f953dfc20f85c0b0c3ea44178dc696d17442d86f39cfa60(
    *,
    name: builtins.str,
    key: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d8142270d4ff247e957ac2eccae2a3bbb9c605f7402c5037b65872d3cba552c(
    *,
    kubernetes: typing.Union[ChallengeSpecSolverDns01Route53AuthKubernetes, typing.Dict[builtins.str, typing.Any]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e950406ddb9dde980e95eec152441496b970ad499cff6fb3b151822b5eaf010b(
    *,
    service_account_ref: typing.Union[ChallengeSpecSolverDns01Route53AuthKubernetesServiceAccountRef, typing.Dict[builtins.str, typing.Any]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5366db8305705ed9e7c4fc89f220afa5ebdfd36b335bd6df7449a72c5fcfcd48(
    *,
    name: builtins.str,
    audiences: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6b260ed8f11172bdeb2d478d0f0917d5a3b8237600d2c4f3c3235bf505ec0dff(
    *,
    name: builtins.str,
    key: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__37000b3447a23ae5e8b634d74fa2ffae23402a83f8a90df74b5e1b307303006f(
    *,
    group_name: builtins.str,
    solver_name: builtins.str,
    config: typing.Any = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7e9169fc4dabcd2e9e67f308a34cada555025d0f8cf0bafdec1f75a9f59f27f8(
    *,
    gateway_http_route: typing.Optional[typing.Union[ChallengeSpecSolverHttp01GatewayHttpRoute, typing.Dict[builtins.str, typing.Any]]] = None,
    ingress: typing.Optional[typing.Union[ChallengeSpecSolverHttp01Ingress, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__67eb71473fe7bcb8103baad885c5d62bd34367e424399142abb055efebfa2c1a(
    *,
    labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    parent_refs: typing.Optional[typing.Sequence[typing.Union[ChallengeSpecSolverHttp01GatewayHttpRouteParentRefs, typing.Dict[builtins.str, typing.Any]]]] = None,
    pod_template: typing.Optional[typing.Union[ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplate, typing.Dict[builtins.str, typing.Any]]] = None,
    service_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7e20cdceec1388053ef677a629fa0ab843e3f28ae32b3301382869b5d5c0c736(
    *,
    name: builtins.str,
    group: typing.Optional[builtins.str] = None,
    kind: typing.Optional[builtins.str] = None,
    namespace: typing.Optional[builtins.str] = None,
    port: typing.Optional[jsii.Number] = None,
    section_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2170caad41c1ea3d466134b6fa2dc16589aba28cc876249b884c7efcf2920731(
    *,
    metadata: typing.Optional[typing.Union[ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateMetadata, typing.Dict[builtins.str, typing.Any]]] = None,
    spec: typing.Optional[typing.Union[ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpec, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4fa9766367c3825852fad4e60091ddeb21795ac5a36842381f9972cd35dedb46(
    *,
    annotations: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a8bcf60fa559acd074963cffaa8da5d4b55540e82d07fb32fd0309d430ef6de9(
    *,
    affinity: typing.Optional[typing.Union[ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinity, typing.Dict[builtins.str, typing.Any]]] = None,
    image_pull_secrets: typing.Optional[typing.Sequence[typing.Union[ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecImagePullSecrets, typing.Dict[builtins.str, typing.Any]]]] = None,
    node_selector: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    priority_class_name: typing.Optional[builtins.str] = None,
    security_context: typing.Optional[typing.Union[ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecSecurityContext, typing.Dict[builtins.str, typing.Any]]] = None,
    service_account_name: typing.Optional[builtins.str] = None,
    tolerations: typing.Optional[typing.Sequence[typing.Union[ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecTolerations, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__29e71ab8ec2bc758e9486a82bbe9f80bde371959649b92fea23cd9cb8c401ef5(
    *,
    node_affinity: typing.Optional[typing.Union[ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityNodeAffinity, typing.Dict[builtins.str, typing.Any]]] = None,
    pod_affinity: typing.Optional[typing.Union[ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAffinity, typing.Dict[builtins.str, typing.Any]]] = None,
    pod_anti_affinity: typing.Optional[typing.Union[ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAntiAffinity, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__795d8af6cb5c20c20fc3bb10d70ecc9bfcf91506cda07402c9e9ed95e3646004(
    *,
    preferred_during_scheduling_ignored_during_execution: typing.Optional[typing.Sequence[typing.Union[ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecution, typing.Dict[builtins.str, typing.Any]]]] = None,
    required_during_scheduling_ignored_during_execution: typing.Optional[typing.Union[ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecution, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2cc393d624fc77e432aea3f0093aa885bceed517b6e5d8be1383ef207a2db1b0(
    *,
    preference: typing.Union[ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecutionPreference, typing.Dict[builtins.str, typing.Any]],
    weight: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__62b588fd6a3409b2b40309210b10f24c524e5df01d16cd5b026b93d7572c7096(
    *,
    match_expressions: typing.Optional[typing.Sequence[typing.Union[ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecutionPreferenceMatchExpressions, typing.Dict[builtins.str, typing.Any]]]] = None,
    match_fields: typing.Optional[typing.Sequence[typing.Union[ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecutionPreferenceMatchFields, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0098e3bbe9cc056fef987159f88e9563f7b5714b1588e94195c33f0a6e5a1f4a(
    *,
    key: builtins.str,
    operator: builtins.str,
    values: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__646d9b5516e80c7bb7753ac9a9e54a545cb137aa7a2f6a4da01739e77a3f8c17(
    *,
    key: builtins.str,
    operator: builtins.str,
    values: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__74cb1280f62c99f848d6543a528900668ec769966fcb0657c8cc495491177faa(
    *,
    node_selector_terms: typing.Sequence[typing.Union[ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionNodeSelectorTerms, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3ccbf453c628c14ef4e41deb4f8c2c87966fbe1eda076107596587738cd86177(
    *,
    match_expressions: typing.Optional[typing.Sequence[typing.Union[ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionNodeSelectorTermsMatchExpressions, typing.Dict[builtins.str, typing.Any]]]] = None,
    match_fields: typing.Optional[typing.Sequence[typing.Union[ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionNodeSelectorTermsMatchFields, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__80e0f14fc3a9f8a109f8187cf59be5bfa20a08fa5fa4cbe9db6f93ee2b02a95e(
    *,
    key: builtins.str,
    operator: builtins.str,
    values: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d5e485057f380eafea0393fc8c6d8ff975433ddf4622886bb65e808a15570c4d(
    *,
    key: builtins.str,
    operator: builtins.str,
    values: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__33b10d922b1a76975d3df2760ea198d948c1a6da497b852fa641491023c4a950(
    *,
    preferred_during_scheduling_ignored_during_execution: typing.Optional[typing.Sequence[typing.Union[ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecution, typing.Dict[builtins.str, typing.Any]]]] = None,
    required_during_scheduling_ignored_during_execution: typing.Optional[typing.Sequence[typing.Union[ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAffinityRequiredDuringSchedulingIgnoredDuringExecution, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__67f53537ce0524556f6febea3e39abcc9998a8a6cd9a5b23be72153f201e06fe(
    *,
    pod_affinity_term: typing.Union[ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTerm, typing.Dict[builtins.str, typing.Any]],
    weight: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__59bac6e6f124245bf9dc813ceb6d089aa3f3574cb85ad97edc5edc4c48b00453(
    *,
    topology_key: builtins.str,
    label_selector: typing.Optional[typing.Union[ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermLabelSelector, typing.Dict[builtins.str, typing.Any]]] = None,
    match_label_keys: typing.Optional[typing.Sequence[builtins.str]] = None,
    mismatch_label_keys: typing.Optional[typing.Sequence[builtins.str]] = None,
    namespaces: typing.Optional[typing.Sequence[builtins.str]] = None,
    namespace_selector: typing.Optional[typing.Union[ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermNamespaceSelector, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b4c32c657c3245e1f11a50ee06ae58c382b71871f98c5a99c5a96ae82f4c6225(
    *,
    match_expressions: typing.Optional[typing.Sequence[typing.Union[ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermLabelSelectorMatchExpressions, typing.Dict[builtins.str, typing.Any]]]] = None,
    match_labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__de0c97d9dff0c2c2d2c2587a6a7b2f3fa7794d4e9379ca59079608c798168500(
    *,
    key: builtins.str,
    operator: builtins.str,
    values: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b678c9f015deab9cd50fcc1b91511f7ba8d45ef2355b983fe50c590136fb9a82(
    *,
    match_expressions: typing.Optional[typing.Sequence[typing.Union[ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermNamespaceSelectorMatchExpressions, typing.Dict[builtins.str, typing.Any]]]] = None,
    match_labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8ae3833d224068fda7617d873ea8b79f95b81bced9f6999ef1ece4589a886e22(
    *,
    key: builtins.str,
    operator: builtins.str,
    values: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3ce9f181986eb8f42bfa4cbdbe2f2a431316064988311bdca7206ee529efdf50(
    *,
    topology_key: builtins.str,
    label_selector: typing.Optional[typing.Union[ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAffinityRequiredDuringSchedulingIgnoredDuringExecutionLabelSelector, typing.Dict[builtins.str, typing.Any]]] = None,
    match_label_keys: typing.Optional[typing.Sequence[builtins.str]] = None,
    mismatch_label_keys: typing.Optional[typing.Sequence[builtins.str]] = None,
    namespaces: typing.Optional[typing.Sequence[builtins.str]] = None,
    namespace_selector: typing.Optional[typing.Union[ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAffinityRequiredDuringSchedulingIgnoredDuringExecutionNamespaceSelector, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1cde2a7027ae8f0384b9d9f345ed8dc62c025be1fac7357251307c84f1c367db(
    *,
    match_expressions: typing.Optional[typing.Sequence[typing.Union[ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAffinityRequiredDuringSchedulingIgnoredDuringExecutionLabelSelectorMatchExpressions, typing.Dict[builtins.str, typing.Any]]]] = None,
    match_labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6f7a74a2a9316f44df5b278fd9cc43d7538a613f15acd3c0c2baa46dfcbcfe4f(
    *,
    key: builtins.str,
    operator: builtins.str,
    values: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d008cfffcc49a81208480db0ac6b715f38dd6090afbf1fc5e313de9c16a5be6f(
    *,
    match_expressions: typing.Optional[typing.Sequence[typing.Union[ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAffinityRequiredDuringSchedulingIgnoredDuringExecutionNamespaceSelectorMatchExpressions, typing.Dict[builtins.str, typing.Any]]]] = None,
    match_labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fddaf38947b6fd41b382e5a972df5b2a31da5d5fb6acc791cc01a38d0ba79909(
    *,
    key: builtins.str,
    operator: builtins.str,
    values: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ab821dd2a088e090fd858a740965c376402052b2c8587ac3dfb937cf89c3eefc(
    *,
    preferred_during_scheduling_ignored_during_execution: typing.Optional[typing.Sequence[typing.Union[ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecution, typing.Dict[builtins.str, typing.Any]]]] = None,
    required_during_scheduling_ignored_during_execution: typing.Optional[typing.Sequence[typing.Union[ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAntiAffinityRequiredDuringSchedulingIgnoredDuringExecution, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__caf64271ddf4c65ce163505f701aae487abf905c8be5402aa19837ef861506e3(
    *,
    pod_affinity_term: typing.Union[ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTerm, typing.Dict[builtins.str, typing.Any]],
    weight: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__efea315c17146562a7f2d978d5b23be4a6f09632f6586a75fade75848fe13e76(
    *,
    topology_key: builtins.str,
    label_selector: typing.Optional[typing.Union[ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermLabelSelector, typing.Dict[builtins.str, typing.Any]]] = None,
    match_label_keys: typing.Optional[typing.Sequence[builtins.str]] = None,
    mismatch_label_keys: typing.Optional[typing.Sequence[builtins.str]] = None,
    namespaces: typing.Optional[typing.Sequence[builtins.str]] = None,
    namespace_selector: typing.Optional[typing.Union[ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermNamespaceSelector, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a3258a46b4863c0aae4b2e584094c63f36c1155c4e7b7177eaeb2e0037f27d64(
    *,
    match_expressions: typing.Optional[typing.Sequence[typing.Union[ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermLabelSelectorMatchExpressions, typing.Dict[builtins.str, typing.Any]]]] = None,
    match_labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__da3c5c9e940a92a70700ce6652dfc1df28b6234bc6bd9c87468832e1c6cf7fc2(
    *,
    key: builtins.str,
    operator: builtins.str,
    values: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1dafa47e3ae28aa2e49438db504569e19ff0353bf20b48d9b358f76152ede14e(
    *,
    match_expressions: typing.Optional[typing.Sequence[typing.Union[ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermNamespaceSelectorMatchExpressions, typing.Dict[builtins.str, typing.Any]]]] = None,
    match_labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__22676c608c81dfc67ddc1ba10dfef17466834dc5487cd8ee9552020a48000a8b(
    *,
    key: builtins.str,
    operator: builtins.str,
    values: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d64c6177fb32631798d50ded8740d04b67729a8cefeac433bdaec79ab1704df8(
    *,
    topology_key: builtins.str,
    label_selector: typing.Optional[typing.Union[ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAntiAffinityRequiredDuringSchedulingIgnoredDuringExecutionLabelSelector, typing.Dict[builtins.str, typing.Any]]] = None,
    match_label_keys: typing.Optional[typing.Sequence[builtins.str]] = None,
    mismatch_label_keys: typing.Optional[typing.Sequence[builtins.str]] = None,
    namespaces: typing.Optional[typing.Sequence[builtins.str]] = None,
    namespace_selector: typing.Optional[typing.Union[ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAntiAffinityRequiredDuringSchedulingIgnoredDuringExecutionNamespaceSelector, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5c0d04ab4767ae5d7bc00b0f6356530fff84c0c6b1cc2e8a7f27dafefa5f30cf(
    *,
    match_expressions: typing.Optional[typing.Sequence[typing.Union[ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAntiAffinityRequiredDuringSchedulingIgnoredDuringExecutionLabelSelectorMatchExpressions, typing.Dict[builtins.str, typing.Any]]]] = None,
    match_labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__605f7a2e21f1815bdadc0b035cc430154ac81373f1b08a942aa87c8f9982b068(
    *,
    key: builtins.str,
    operator: builtins.str,
    values: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d615d9445aa34aff5d26ef06f5f0ddcd4fda89fab861a2738a18e7b6e261731(
    *,
    match_expressions: typing.Optional[typing.Sequence[typing.Union[ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecAffinityPodAntiAffinityRequiredDuringSchedulingIgnoredDuringExecutionNamespaceSelectorMatchExpressions, typing.Dict[builtins.str, typing.Any]]]] = None,
    match_labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eaec30274d71aff89fdefaa7c67360fc2bc6c75c119a89fbaec725f5b42833d0(
    *,
    key: builtins.str,
    operator: builtins.str,
    values: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9859fd882b5ec21ed3095e5a77d3d6269e1d3ee77a6a9dd962a9ab622821dd27(
    *,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3382d5a17213e2c85657b289a3d23b9fe837b85499a1b07653bcf473e3edd021(
    *,
    fs_group: typing.Optional[jsii.Number] = None,
    fs_group_change_policy: typing.Optional[builtins.str] = None,
    run_as_group: typing.Optional[jsii.Number] = None,
    run_as_non_root: typing.Optional[builtins.bool] = None,
    run_as_user: typing.Optional[jsii.Number] = None,
    seccomp_profile: typing.Optional[typing.Union[ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecSecurityContextSeccompProfile, typing.Dict[builtins.str, typing.Any]]] = None,
    se_linux_options: typing.Optional[typing.Union[ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecSecurityContextSeLinuxOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    supplemental_groups: typing.Optional[typing.Sequence[jsii.Number]] = None,
    sysctls: typing.Optional[typing.Sequence[typing.Union[ChallengeSpecSolverHttp01GatewayHttpRoutePodTemplateSpecSecurityContextSysctls, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ad6a87b1e8b45aa3e93ec6c6f6663bae7834255f279f1e579f41c481583ea512(
    *,
    level: typing.Optional[builtins.str] = None,
    role: typing.Optional[builtins.str] = None,
    type: typing.Optional[builtins.str] = None,
    user: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__250f1451ce2065546eec63696a776116347bad21687392234bb8c9f701600e43(
    *,
    type: builtins.str,
    localhost_profile: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d1f2e562b7329e2c6ba925c5bb2f341d0ec701ee3528a722df6cab2003e646d(
    *,
    name: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3b197938ebc537eff86a92974f545e4f535fbe1e79f01cdfa97fcfbe8b797657(
    *,
    effect: typing.Optional[builtins.str] = None,
    key: typing.Optional[builtins.str] = None,
    operator: typing.Optional[builtins.str] = None,
    toleration_seconds: typing.Optional[jsii.Number] = None,
    value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__408732626e682c629a101bb800fe202e2f00a46a57820a3b4a379d59f996eb25(
    *,
    class_: typing.Optional[builtins.str] = None,
    ingress_class_name: typing.Optional[builtins.str] = None,
    ingress_template: typing.Optional[typing.Union[ChallengeSpecSolverHttp01IngressIngressTemplate, typing.Dict[builtins.str, typing.Any]]] = None,
    name: typing.Optional[builtins.str] = None,
    pod_template: typing.Optional[typing.Union[ChallengeSpecSolverHttp01IngressPodTemplate, typing.Dict[builtins.str, typing.Any]]] = None,
    service_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e3e7fc9ed653a05e7787d3a770b22522625722d61652450d252dcd22dcc878db(
    *,
    metadata: typing.Optional[typing.Union[ChallengeSpecSolverHttp01IngressIngressTemplateMetadata, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0e064f5873f9bd1176ec8fe22b1734b5db2747a93d1f4354ff953eb33f40f701(
    *,
    annotations: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d69d3251d18e75d85c237247ddf685a9af0fa179ff6e1cad64c1fa285f48355(
    *,
    metadata: typing.Optional[typing.Union[ChallengeSpecSolverHttp01IngressPodTemplateMetadata, typing.Dict[builtins.str, typing.Any]]] = None,
    spec: typing.Optional[typing.Union[ChallengeSpecSolverHttp01IngressPodTemplateSpec, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b09908dbff5bd2f918117323927331cb51af2e6a0076610db1b1dce8b9157684(
    *,
    annotations: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c55b1852a0ce8beedd77943df68f0f11832ef840acf01cb6da63966fae9cfcf4(
    *,
    affinity: typing.Optional[typing.Union[ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinity, typing.Dict[builtins.str, typing.Any]]] = None,
    image_pull_secrets: typing.Optional[typing.Sequence[typing.Union[ChallengeSpecSolverHttp01IngressPodTemplateSpecImagePullSecrets, typing.Dict[builtins.str, typing.Any]]]] = None,
    node_selector: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    priority_class_name: typing.Optional[builtins.str] = None,
    security_context: typing.Optional[typing.Union[ChallengeSpecSolverHttp01IngressPodTemplateSpecSecurityContext, typing.Dict[builtins.str, typing.Any]]] = None,
    service_account_name: typing.Optional[builtins.str] = None,
    tolerations: typing.Optional[typing.Sequence[typing.Union[ChallengeSpecSolverHttp01IngressPodTemplateSpecTolerations, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e4725fc235dbf7a8a04ea9bc8552fbda04f11532609b62223dc12b3ce1cfc890(
    *,
    node_affinity: typing.Optional[typing.Union[ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinity, typing.Dict[builtins.str, typing.Any]]] = None,
    pod_affinity: typing.Optional[typing.Union[ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinity, typing.Dict[builtins.str, typing.Any]]] = None,
    pod_anti_affinity: typing.Optional[typing.Union[ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinity, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1f5b9eddd3e77b4926a363d5fff196640cebb824cccaa09e005aded4073b508c(
    *,
    preferred_during_scheduling_ignored_during_execution: typing.Optional[typing.Sequence[typing.Union[ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecution, typing.Dict[builtins.str, typing.Any]]]] = None,
    required_during_scheduling_ignored_during_execution: typing.Optional[typing.Union[ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecution, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__46f7952cde067868c2b74413c601e3a91c0574bb4fcd5db8a424d552d033a047(
    *,
    preference: typing.Union[ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecutionPreference, typing.Dict[builtins.str, typing.Any]],
    weight: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fd8289b175672663b8617afe183d823b765fdbc317bd817d4dddefef7714236c(
    *,
    match_expressions: typing.Optional[typing.Sequence[typing.Union[ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecutionPreferenceMatchExpressions, typing.Dict[builtins.str, typing.Any]]]] = None,
    match_fields: typing.Optional[typing.Sequence[typing.Union[ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecutionPreferenceMatchFields, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3db3beed886a79a61590ea1dc6f3ba8a17ae215c05e802628e2d0bc5dab95c11(
    *,
    key: builtins.str,
    operator: builtins.str,
    values: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__795b6506b645f122ce26f5df4f33c5305a512cc4287b2e88611b07a3fe81d766(
    *,
    key: builtins.str,
    operator: builtins.str,
    values: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__161051c4f4dd22a6804aaa5a717f810d1bc6a9623f9b80215cd98626da6170bf(
    *,
    node_selector_terms: typing.Sequence[typing.Union[ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionNodeSelectorTerms, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b744f19a967cad64d04088cea822de7b5236126d5b57c0961e26cb1d21bcdce7(
    *,
    match_expressions: typing.Optional[typing.Sequence[typing.Union[ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionNodeSelectorTermsMatchExpressions, typing.Dict[builtins.str, typing.Any]]]] = None,
    match_fields: typing.Optional[typing.Sequence[typing.Union[ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionNodeSelectorTermsMatchFields, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6983dcff128ed3db81d6133320b7ab2bce7a7d2d9b0eca6033a4c057659d2eec(
    *,
    key: builtins.str,
    operator: builtins.str,
    values: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec159c62ca76f76cd8fee949b1ba7bc2f20c4ffa2206f2385331a25e79aa8c6a(
    *,
    key: builtins.str,
    operator: builtins.str,
    values: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eb2c0c7fa056016c7433535606c9091ee315abf2497dcd74dcd1cd9e1db0353a(
    *,
    preferred_during_scheduling_ignored_during_execution: typing.Optional[typing.Sequence[typing.Union[ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecution, typing.Dict[builtins.str, typing.Any]]]] = None,
    required_during_scheduling_ignored_during_execution: typing.Optional[typing.Sequence[typing.Union[ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityRequiredDuringSchedulingIgnoredDuringExecution, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__02b63a56c28d75f58aaa104f0e3f3907fd21e796c71bbba401591c1d5c53b4a8(
    *,
    pod_affinity_term: typing.Union[ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTerm, typing.Dict[builtins.str, typing.Any]],
    weight: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__14510f593855c5c591882bd8aa55dcc3d74603e3aee3f5eb618c657e5137d3cf(
    *,
    topology_key: builtins.str,
    label_selector: typing.Optional[typing.Union[ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermLabelSelector, typing.Dict[builtins.str, typing.Any]]] = None,
    match_label_keys: typing.Optional[typing.Sequence[builtins.str]] = None,
    mismatch_label_keys: typing.Optional[typing.Sequence[builtins.str]] = None,
    namespaces: typing.Optional[typing.Sequence[builtins.str]] = None,
    namespace_selector: typing.Optional[typing.Union[ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermNamespaceSelector, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bab4a4fb78540135a5cb25eed199cb74e21a4985c3806c1519aeda545c5344d3(
    *,
    match_expressions: typing.Optional[typing.Sequence[typing.Union[ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermLabelSelectorMatchExpressions, typing.Dict[builtins.str, typing.Any]]]] = None,
    match_labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__860f489daa83128689d6f48e3dc5ff1ff727b5c14e3648855eb6dd6c7738d97b(
    *,
    key: builtins.str,
    operator: builtins.str,
    values: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1e9b1c1ba3f72820af01ef8d576bcbce7940bafdab42d3dd675b6c936c1d8cfc(
    *,
    match_expressions: typing.Optional[typing.Sequence[typing.Union[ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermNamespaceSelectorMatchExpressions, typing.Dict[builtins.str, typing.Any]]]] = None,
    match_labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__043f465ff0ebd6f84d1aa6be27ecaec09d22ae38d6e2e55ca7175e3c95e3ce08(
    *,
    key: builtins.str,
    operator: builtins.str,
    values: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__922594031745af5710f4997ce6758f019a75edb530bc7195bd558b71fc280418(
    *,
    topology_key: builtins.str,
    label_selector: typing.Optional[typing.Union[ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityRequiredDuringSchedulingIgnoredDuringExecutionLabelSelector, typing.Dict[builtins.str, typing.Any]]] = None,
    match_label_keys: typing.Optional[typing.Sequence[builtins.str]] = None,
    mismatch_label_keys: typing.Optional[typing.Sequence[builtins.str]] = None,
    namespaces: typing.Optional[typing.Sequence[builtins.str]] = None,
    namespace_selector: typing.Optional[typing.Union[ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityRequiredDuringSchedulingIgnoredDuringExecutionNamespaceSelector, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9378ba8a7b53c4f919d4882ae1278e31734324fc6e3ec7cc9b485ffe4b5f31d7(
    *,
    match_expressions: typing.Optional[typing.Sequence[typing.Union[ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityRequiredDuringSchedulingIgnoredDuringExecutionLabelSelectorMatchExpressions, typing.Dict[builtins.str, typing.Any]]]] = None,
    match_labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ba23b47efb96d237c5b3540a82a4c9205457e0500ed1090e766570d8f7973b30(
    *,
    key: builtins.str,
    operator: builtins.str,
    values: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7e0de58859c9cd5be5f9fc24ca1433f8950542e5eaffc2af6582f958616c0a04(
    *,
    match_expressions: typing.Optional[typing.Sequence[typing.Union[ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAffinityRequiredDuringSchedulingIgnoredDuringExecutionNamespaceSelectorMatchExpressions, typing.Dict[builtins.str, typing.Any]]]] = None,
    match_labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bce77446c5edcba3f047d7e98cf05bfcdb22b07c83faa44338ef002a9848a7bd(
    *,
    key: builtins.str,
    operator: builtins.str,
    values: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2e3ef9df9d1f4bbc9dfda4479d18531323273cd91822ff6570c15b646ca5ae6e(
    *,
    preferred_during_scheduling_ignored_during_execution: typing.Optional[typing.Sequence[typing.Union[ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecution, typing.Dict[builtins.str, typing.Any]]]] = None,
    required_during_scheduling_ignored_during_execution: typing.Optional[typing.Sequence[typing.Union[ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityRequiredDuringSchedulingIgnoredDuringExecution, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__155ee19c3e7f0489156b102f27150e749c596f8955b60a1a6d79c4569d6d8073(
    *,
    pod_affinity_term: typing.Union[ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTerm, typing.Dict[builtins.str, typing.Any]],
    weight: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ace66bc55b30573a6c9bcb8ead82e91f877f68addf011d52c4b4f30cffb50afe(
    *,
    topology_key: builtins.str,
    label_selector: typing.Optional[typing.Union[ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermLabelSelector, typing.Dict[builtins.str, typing.Any]]] = None,
    match_label_keys: typing.Optional[typing.Sequence[builtins.str]] = None,
    mismatch_label_keys: typing.Optional[typing.Sequence[builtins.str]] = None,
    namespaces: typing.Optional[typing.Sequence[builtins.str]] = None,
    namespace_selector: typing.Optional[typing.Union[ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermNamespaceSelector, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__944085c3fc4b87f3f9bd37e2bb5cd2f98be5e92ba1e8d0efb81aa103f8c044d8(
    *,
    match_expressions: typing.Optional[typing.Sequence[typing.Union[ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermLabelSelectorMatchExpressions, typing.Dict[builtins.str, typing.Any]]]] = None,
    match_labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__822d41b914f479e420f6875d275ba9106843b1ef62f665f216e4e4eed1872169(
    *,
    key: builtins.str,
    operator: builtins.str,
    values: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a19ba490e46c6abe28e31a4a3329365b55b4233f5376d47eab3085e6a59dddb5(
    *,
    match_expressions: typing.Optional[typing.Sequence[typing.Union[ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecutionPodAffinityTermNamespaceSelectorMatchExpressions, typing.Dict[builtins.str, typing.Any]]]] = None,
    match_labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0700bf41205c8a58d3606f40af63faaafdf5a99220aad0cd2270cfc0ae7605f2(
    *,
    key: builtins.str,
    operator: builtins.str,
    values: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e57996b1d7410c01ce12a88738aa9506e3b9069a1309440938c64caf1fec5e7c(
    *,
    topology_key: builtins.str,
    label_selector: typing.Optional[typing.Union[ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityRequiredDuringSchedulingIgnoredDuringExecutionLabelSelector, typing.Dict[builtins.str, typing.Any]]] = None,
    match_label_keys: typing.Optional[typing.Sequence[builtins.str]] = None,
    mismatch_label_keys: typing.Optional[typing.Sequence[builtins.str]] = None,
    namespaces: typing.Optional[typing.Sequence[builtins.str]] = None,
    namespace_selector: typing.Optional[typing.Union[ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityRequiredDuringSchedulingIgnoredDuringExecutionNamespaceSelector, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__88fcd141034e5e8a5f70bdffe1823be15efc53ea470ed5ed436f5c251a491ff6(
    *,
    match_expressions: typing.Optional[typing.Sequence[typing.Union[ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityRequiredDuringSchedulingIgnoredDuringExecutionLabelSelectorMatchExpressions, typing.Dict[builtins.str, typing.Any]]]] = None,
    match_labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d089adc0a13ef81db73caa1a124194502656b46d958ea845f7c9c78348cdbc9(
    *,
    key: builtins.str,
    operator: builtins.str,
    values: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__afb631a07dbef3bb9de194e0d35bac91d19f71d9702b1ebfe85b02b6668b884b(
    *,
    match_expressions: typing.Optional[typing.Sequence[typing.Union[ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinityPodAntiAffinityRequiredDuringSchedulingIgnoredDuringExecutionNamespaceSelectorMatchExpressions, typing.Dict[builtins.str, typing.Any]]]] = None,
    match_labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__46a9dc59ee81a5e31dd81d4401422486e369f0ec7060c1c3532d9dc0f32cab1c(
    *,
    key: builtins.str,
    operator: builtins.str,
    values: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__32a41fbca1e0ee7a0388f7fc90a14cbf957c964182675b9de345a121f798dc44(
    *,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a1502840d844972e98aea64200d5a094b40bdcbc97c9c1c421975cc1614ba223(
    *,
    fs_group: typing.Optional[jsii.Number] = None,
    fs_group_change_policy: typing.Optional[builtins.str] = None,
    run_as_group: typing.Optional[jsii.Number] = None,
    run_as_non_root: typing.Optional[builtins.bool] = None,
    run_as_user: typing.Optional[jsii.Number] = None,
    seccomp_profile: typing.Optional[typing.Union[ChallengeSpecSolverHttp01IngressPodTemplateSpecSecurityContextSeccompProfile, typing.Dict[builtins.str, typing.Any]]] = None,
    se_linux_options: typing.Optional[typing.Union[ChallengeSpecSolverHttp01IngressPodTemplateSpecSecurityContextSeLinuxOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    supplemental_groups: typing.Optional[typing.Sequence[jsii.Number]] = None,
    sysctls: typing.Optional[typing.Sequence[typing.Union[ChallengeSpecSolverHttp01IngressPodTemplateSpecSecurityContextSysctls, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e46a61acbd13fdeed11939e876e7c3b53c8e69007d8d06183055ff9589a0ebb2(
    *,
    level: typing.Optional[builtins.str] = None,
    role: typing.Optional[builtins.str] = None,
    type: typing.Optional[builtins.str] = None,
    user: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__41eca06f58dece1bb4992cfac597e9b57daeee44a2b049906fbd4050c7f61b8c(
    *,
    type: builtins.str,
    localhost_profile: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__25f6cbd52a64d6239ffd846f6525fb9cd5e8486ae29b1ac2d6cc264d7b292404(
    *,
    name: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f98eb15901a8d2b33cdf610c5770e4235960270776ae3ccbf5fb9e2b54588457(
    *,
    effect: typing.Optional[builtins.str] = None,
    key: typing.Optional[builtins.str] = None,
    operator: typing.Optional[builtins.str] = None,
    toleration_seconds: typing.Optional[jsii.Number] = None,
    value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4b23cc54499bb6a3fb663f4f24d6b5d8847c45075e56778f3ceaa474d6f163fe(
    *,
    dns_names: typing.Optional[typing.Sequence[builtins.str]] = None,
    dns_zones: typing.Optional[typing.Sequence[builtins.str]] = None,
    match_labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__34bcee1b050f29f7d741f3476b67636108df8a8f593c0584f3c343237e6e2e7e(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    metadata: typing.Union[_cdk8s_d3d9af27.ApiObjectMetadata, typing.Dict[builtins.str, typing.Any]],
    spec: typing.Union[OrderSpec, typing.Dict[builtins.str, typing.Any]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d305eba977d638ba7ddcabcd7e0eaac0b639c9d0bc92c822368b502267ef3775(
    *,
    metadata: typing.Union[_cdk8s_d3d9af27.ApiObjectMetadata, typing.Dict[builtins.str, typing.Any]],
    spec: typing.Union[OrderSpec, typing.Dict[builtins.str, typing.Any]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b996931a2adb1f4b471e1fd158376a9d51ccc0564a05633d0caa0a7416787d14(
    *,
    issuer_ref: typing.Union[OrderSpecIssuerRef, typing.Dict[builtins.str, typing.Any]],
    request: builtins.str,
    common_name: typing.Optional[builtins.str] = None,
    dns_names: typing.Optional[typing.Sequence[builtins.str]] = None,
    duration: typing.Optional[builtins.str] = None,
    ip_addresses: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4675758fbb6e921cd2e91de67d2858460cab73f1393b0bfd785f01c9fdeaee6a(
    *,
    name: builtins.str,
    group: typing.Optional[builtins.str] = None,
    kind: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
