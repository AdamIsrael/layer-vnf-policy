from charmhelpers.core.hookenv import (
    action_get,
    action_fail,
    action_set,
    status_set,
    log,
)

from charms.reactive import (
    clear_flag,
    set_flag,
    when,
    when_not,
)


@when_not('vnf-policy.installed')
def install_vnf_b():
    set_flag('vnf-policy.installed')
    status_set('active', 'Ready!')


@when('actions.set-policy')
def action_set_policy():
    """Set the policy for a given user.

    Sets the policy (bw and qos) for the specified user_id
    """
    err = ''
    updated = False
    try:
        user_id = action_get('user_id')
        bw = action_get('bw')
        qos = action_get('qos')

        # If this were a functional vnf, you would perform your operation here
        # and may return a value to indicate success or failure.
        updated = True

    except Exception as err:
        action_fail(str(err))
    else:
        action_set({'updated': updated})
    finally:
        clear_flag('actions.set-policy')
