# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import flipt_pb2 as flipt__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


class FliptStub(object):
    """Missing associated documentation comment in .proto file"""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Evaluate = channel.unary_unary(
                '/flipt.Flipt/Evaluate',
                request_serializer=flipt__pb2.EvaluationRequest.SerializeToString,
                response_deserializer=flipt__pb2.EvaluationResponse.FromString,
                )
        self.GetFlag = channel.unary_unary(
                '/flipt.Flipt/GetFlag',
                request_serializer=flipt__pb2.GetFlagRequest.SerializeToString,
                response_deserializer=flipt__pb2.Flag.FromString,
                )
        self.ListFlags = channel.unary_unary(
                '/flipt.Flipt/ListFlags',
                request_serializer=flipt__pb2.ListFlagRequest.SerializeToString,
                response_deserializer=flipt__pb2.FlagList.FromString,
                )
        self.CreateFlag = channel.unary_unary(
                '/flipt.Flipt/CreateFlag',
                request_serializer=flipt__pb2.CreateFlagRequest.SerializeToString,
                response_deserializer=flipt__pb2.Flag.FromString,
                )
        self.UpdateFlag = channel.unary_unary(
                '/flipt.Flipt/UpdateFlag',
                request_serializer=flipt__pb2.UpdateFlagRequest.SerializeToString,
                response_deserializer=flipt__pb2.Flag.FromString,
                )
        self.DeleteFlag = channel.unary_unary(
                '/flipt.Flipt/DeleteFlag',
                request_serializer=flipt__pb2.DeleteFlagRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.CreateVariant = channel.unary_unary(
                '/flipt.Flipt/CreateVariant',
                request_serializer=flipt__pb2.CreateVariantRequest.SerializeToString,
                response_deserializer=flipt__pb2.Variant.FromString,
                )
        self.UpdateVariant = channel.unary_unary(
                '/flipt.Flipt/UpdateVariant',
                request_serializer=flipt__pb2.UpdateVariantRequest.SerializeToString,
                response_deserializer=flipt__pb2.Variant.FromString,
                )
        self.DeleteVariant = channel.unary_unary(
                '/flipt.Flipt/DeleteVariant',
                request_serializer=flipt__pb2.DeleteVariantRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.GetRule = channel.unary_unary(
                '/flipt.Flipt/GetRule',
                request_serializer=flipt__pb2.GetRuleRequest.SerializeToString,
                response_deserializer=flipt__pb2.Rule.FromString,
                )
        self.ListRules = channel.unary_unary(
                '/flipt.Flipt/ListRules',
                request_serializer=flipt__pb2.ListRuleRequest.SerializeToString,
                response_deserializer=flipt__pb2.RuleList.FromString,
                )
        self.OrderRules = channel.unary_unary(
                '/flipt.Flipt/OrderRules',
                request_serializer=flipt__pb2.OrderRulesRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.CreateRule = channel.unary_unary(
                '/flipt.Flipt/CreateRule',
                request_serializer=flipt__pb2.CreateRuleRequest.SerializeToString,
                response_deserializer=flipt__pb2.Rule.FromString,
                )
        self.UpdateRule = channel.unary_unary(
                '/flipt.Flipt/UpdateRule',
                request_serializer=flipt__pb2.UpdateRuleRequest.SerializeToString,
                response_deserializer=flipt__pb2.Rule.FromString,
                )
        self.DeleteRule = channel.unary_unary(
                '/flipt.Flipt/DeleteRule',
                request_serializer=flipt__pb2.DeleteRuleRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.CreateDistribution = channel.unary_unary(
                '/flipt.Flipt/CreateDistribution',
                request_serializer=flipt__pb2.CreateDistributionRequest.SerializeToString,
                response_deserializer=flipt__pb2.Distribution.FromString,
                )
        self.UpdateDistribution = channel.unary_unary(
                '/flipt.Flipt/UpdateDistribution',
                request_serializer=flipt__pb2.UpdateDistributionRequest.SerializeToString,
                response_deserializer=flipt__pb2.Distribution.FromString,
                )
        self.DeleteDistribution = channel.unary_unary(
                '/flipt.Flipt/DeleteDistribution',
                request_serializer=flipt__pb2.DeleteDistributionRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.GetSegment = channel.unary_unary(
                '/flipt.Flipt/GetSegment',
                request_serializer=flipt__pb2.GetSegmentRequest.SerializeToString,
                response_deserializer=flipt__pb2.Segment.FromString,
                )
        self.ListSegments = channel.unary_unary(
                '/flipt.Flipt/ListSegments',
                request_serializer=flipt__pb2.ListSegmentRequest.SerializeToString,
                response_deserializer=flipt__pb2.SegmentList.FromString,
                )
        self.CreateSegment = channel.unary_unary(
                '/flipt.Flipt/CreateSegment',
                request_serializer=flipt__pb2.CreateSegmentRequest.SerializeToString,
                response_deserializer=flipt__pb2.Segment.FromString,
                )
        self.UpdateSegment = channel.unary_unary(
                '/flipt.Flipt/UpdateSegment',
                request_serializer=flipt__pb2.UpdateSegmentRequest.SerializeToString,
                response_deserializer=flipt__pb2.Segment.FromString,
                )
        self.DeleteSegment = channel.unary_unary(
                '/flipt.Flipt/DeleteSegment',
                request_serializer=flipt__pb2.DeleteSegmentRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.CreateConstraint = channel.unary_unary(
                '/flipt.Flipt/CreateConstraint',
                request_serializer=flipt__pb2.CreateConstraintRequest.SerializeToString,
                response_deserializer=flipt__pb2.Constraint.FromString,
                )
        self.UpdateConstraint = channel.unary_unary(
                '/flipt.Flipt/UpdateConstraint',
                request_serializer=flipt__pb2.UpdateConstraintRequest.SerializeToString,
                response_deserializer=flipt__pb2.Constraint.FromString,
                )
        self.DeleteConstraint = channel.unary_unary(
                '/flipt.Flipt/DeleteConstraint',
                request_serializer=flipt__pb2.DeleteConstraintRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )


class FliptServicer(object):
    """Missing associated documentation comment in .proto file"""

    def Evaluate(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetFlag(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListFlags(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateFlag(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateFlag(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteFlag(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateVariant(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateVariant(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteVariant(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetRule(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListRules(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def OrderRules(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateRule(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateRule(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteRule(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateDistribution(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateDistribution(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteDistribution(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetSegment(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListSegments(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateSegment(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateSegment(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteSegment(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateConstraint(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateConstraint(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteConstraint(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_FliptServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Evaluate': grpc.unary_unary_rpc_method_handler(
                    servicer.Evaluate,
                    request_deserializer=flipt__pb2.EvaluationRequest.FromString,
                    response_serializer=flipt__pb2.EvaluationResponse.SerializeToString,
            ),
            'GetFlag': grpc.unary_unary_rpc_method_handler(
                    servicer.GetFlag,
                    request_deserializer=flipt__pb2.GetFlagRequest.FromString,
                    response_serializer=flipt__pb2.Flag.SerializeToString,
            ),
            'ListFlags': grpc.unary_unary_rpc_method_handler(
                    servicer.ListFlags,
                    request_deserializer=flipt__pb2.ListFlagRequest.FromString,
                    response_serializer=flipt__pb2.FlagList.SerializeToString,
            ),
            'CreateFlag': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateFlag,
                    request_deserializer=flipt__pb2.CreateFlagRequest.FromString,
                    response_serializer=flipt__pb2.Flag.SerializeToString,
            ),
            'UpdateFlag': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateFlag,
                    request_deserializer=flipt__pb2.UpdateFlagRequest.FromString,
                    response_serializer=flipt__pb2.Flag.SerializeToString,
            ),
            'DeleteFlag': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteFlag,
                    request_deserializer=flipt__pb2.DeleteFlagRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'CreateVariant': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateVariant,
                    request_deserializer=flipt__pb2.CreateVariantRequest.FromString,
                    response_serializer=flipt__pb2.Variant.SerializeToString,
            ),
            'UpdateVariant': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateVariant,
                    request_deserializer=flipt__pb2.UpdateVariantRequest.FromString,
                    response_serializer=flipt__pb2.Variant.SerializeToString,
            ),
            'DeleteVariant': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteVariant,
                    request_deserializer=flipt__pb2.DeleteVariantRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'GetRule': grpc.unary_unary_rpc_method_handler(
                    servicer.GetRule,
                    request_deserializer=flipt__pb2.GetRuleRequest.FromString,
                    response_serializer=flipt__pb2.Rule.SerializeToString,
            ),
            'ListRules': grpc.unary_unary_rpc_method_handler(
                    servicer.ListRules,
                    request_deserializer=flipt__pb2.ListRuleRequest.FromString,
                    response_serializer=flipt__pb2.RuleList.SerializeToString,
            ),
            'OrderRules': grpc.unary_unary_rpc_method_handler(
                    servicer.OrderRules,
                    request_deserializer=flipt__pb2.OrderRulesRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'CreateRule': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateRule,
                    request_deserializer=flipt__pb2.CreateRuleRequest.FromString,
                    response_serializer=flipt__pb2.Rule.SerializeToString,
            ),
            'UpdateRule': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateRule,
                    request_deserializer=flipt__pb2.UpdateRuleRequest.FromString,
                    response_serializer=flipt__pb2.Rule.SerializeToString,
            ),
            'DeleteRule': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteRule,
                    request_deserializer=flipt__pb2.DeleteRuleRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'CreateDistribution': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateDistribution,
                    request_deserializer=flipt__pb2.CreateDistributionRequest.FromString,
                    response_serializer=flipt__pb2.Distribution.SerializeToString,
            ),
            'UpdateDistribution': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateDistribution,
                    request_deserializer=flipt__pb2.UpdateDistributionRequest.FromString,
                    response_serializer=flipt__pb2.Distribution.SerializeToString,
            ),
            'DeleteDistribution': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteDistribution,
                    request_deserializer=flipt__pb2.DeleteDistributionRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'GetSegment': grpc.unary_unary_rpc_method_handler(
                    servicer.GetSegment,
                    request_deserializer=flipt__pb2.GetSegmentRequest.FromString,
                    response_serializer=flipt__pb2.Segment.SerializeToString,
            ),
            'ListSegments': grpc.unary_unary_rpc_method_handler(
                    servicer.ListSegments,
                    request_deserializer=flipt__pb2.ListSegmentRequest.FromString,
                    response_serializer=flipt__pb2.SegmentList.SerializeToString,
            ),
            'CreateSegment': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateSegment,
                    request_deserializer=flipt__pb2.CreateSegmentRequest.FromString,
                    response_serializer=flipt__pb2.Segment.SerializeToString,
            ),
            'UpdateSegment': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateSegment,
                    request_deserializer=flipt__pb2.UpdateSegmentRequest.FromString,
                    response_serializer=flipt__pb2.Segment.SerializeToString,
            ),
            'DeleteSegment': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteSegment,
                    request_deserializer=flipt__pb2.DeleteSegmentRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'CreateConstraint': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateConstraint,
                    request_deserializer=flipt__pb2.CreateConstraintRequest.FromString,
                    response_serializer=flipt__pb2.Constraint.SerializeToString,
            ),
            'UpdateConstraint': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateConstraint,
                    request_deserializer=flipt__pb2.UpdateConstraintRequest.FromString,
                    response_serializer=flipt__pb2.Constraint.SerializeToString,
            ),
            'DeleteConstraint': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteConstraint,
                    request_deserializer=flipt__pb2.DeleteConstraintRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'flipt.Flipt', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Flipt(object):
    """Missing associated documentation comment in .proto file"""

    @staticmethod
    def Evaluate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/flipt.Flipt/Evaluate',
            flipt__pb2.EvaluationRequest.SerializeToString,
            flipt__pb2.EvaluationResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetFlag(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/flipt.Flipt/GetFlag',
            flipt__pb2.GetFlagRequest.SerializeToString,
            flipt__pb2.Flag.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListFlags(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/flipt.Flipt/ListFlags',
            flipt__pb2.ListFlagRequest.SerializeToString,
            flipt__pb2.FlagList.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateFlag(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/flipt.Flipt/CreateFlag',
            flipt__pb2.CreateFlagRequest.SerializeToString,
            flipt__pb2.Flag.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateFlag(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/flipt.Flipt/UpdateFlag',
            flipt__pb2.UpdateFlagRequest.SerializeToString,
            flipt__pb2.Flag.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteFlag(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/flipt.Flipt/DeleteFlag',
            flipt__pb2.DeleteFlagRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateVariant(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/flipt.Flipt/CreateVariant',
            flipt__pb2.CreateVariantRequest.SerializeToString,
            flipt__pb2.Variant.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateVariant(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/flipt.Flipt/UpdateVariant',
            flipt__pb2.UpdateVariantRequest.SerializeToString,
            flipt__pb2.Variant.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteVariant(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/flipt.Flipt/DeleteVariant',
            flipt__pb2.DeleteVariantRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetRule(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/flipt.Flipt/GetRule',
            flipt__pb2.GetRuleRequest.SerializeToString,
            flipt__pb2.Rule.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListRules(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/flipt.Flipt/ListRules',
            flipt__pb2.ListRuleRequest.SerializeToString,
            flipt__pb2.RuleList.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def OrderRules(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/flipt.Flipt/OrderRules',
            flipt__pb2.OrderRulesRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateRule(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/flipt.Flipt/CreateRule',
            flipt__pb2.CreateRuleRequest.SerializeToString,
            flipt__pb2.Rule.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateRule(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/flipt.Flipt/UpdateRule',
            flipt__pb2.UpdateRuleRequest.SerializeToString,
            flipt__pb2.Rule.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteRule(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/flipt.Flipt/DeleteRule',
            flipt__pb2.DeleteRuleRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateDistribution(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/flipt.Flipt/CreateDistribution',
            flipt__pb2.CreateDistributionRequest.SerializeToString,
            flipt__pb2.Distribution.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateDistribution(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/flipt.Flipt/UpdateDistribution',
            flipt__pb2.UpdateDistributionRequest.SerializeToString,
            flipt__pb2.Distribution.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteDistribution(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/flipt.Flipt/DeleteDistribution',
            flipt__pb2.DeleteDistributionRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetSegment(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/flipt.Flipt/GetSegment',
            flipt__pb2.GetSegmentRequest.SerializeToString,
            flipt__pb2.Segment.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListSegments(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/flipt.Flipt/ListSegments',
            flipt__pb2.ListSegmentRequest.SerializeToString,
            flipt__pb2.SegmentList.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateSegment(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/flipt.Flipt/CreateSegment',
            flipt__pb2.CreateSegmentRequest.SerializeToString,
            flipt__pb2.Segment.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateSegment(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/flipt.Flipt/UpdateSegment',
            flipt__pb2.UpdateSegmentRequest.SerializeToString,
            flipt__pb2.Segment.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteSegment(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/flipt.Flipt/DeleteSegment',
            flipt__pb2.DeleteSegmentRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateConstraint(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/flipt.Flipt/CreateConstraint',
            flipt__pb2.CreateConstraintRequest.SerializeToString,
            flipt__pb2.Constraint.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateConstraint(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/flipt.Flipt/UpdateConstraint',
            flipt__pb2.UpdateConstraintRequest.SerializeToString,
            flipt__pb2.Constraint.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteConstraint(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/flipt.Flipt/DeleteConstraint',
            flipt__pb2.DeleteConstraintRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)