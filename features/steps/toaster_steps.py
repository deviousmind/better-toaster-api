from behave import *

from src.device_wrangler import DeviceWrangler
from src.toaster import Toaster, ToasterStatus
from src.device_pool import DevicePool

import uuid


@given("the toaster is online")
def step_impl(context):
    context.toaster_id = uuid.uuid4()
    toaster = Toaster(context.toaster_id)
    pool = DevicePool()
    pool.add(toaster)
    context.device_wrangler = DeviceWrangler(pool)


@when("it receives a request for {bread_type} bread at level {toast_level:d}")
def step_impl(context, bread_type, toast_level):
    context.device_wrangler.send(context.toaster_id, bread_type=bread_type, toast_level=toast_level)


@then("the toaster is in wait mode")
def step_impl(context):
    toaster_status = context.device_wrangler.get_status(context.toaster_id)
    expected_status = ToasterStatus.WAIT_MODE
    assert toaster_status is expected_status


@step("the toaster is in wait mode")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And the toaster is in wait mode')


@then("a wait response is sent")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then a wait response is sent')


@step("it receives a request for wheat bread at level 3")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And it receives a request for wheat bread at level 3')


@when("it completes toasting")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: When it completes toasting')


@then("a toast ready response is sent")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then a toast ready response is sent')


@given("the toaster is offline")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Given the toaster is offline')


@then("an offline response is sent")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then an offline response is sent')