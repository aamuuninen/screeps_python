from defs import *

__pragma__('noalias', 'name')
__pragma__('noalias', 'undefined')
__pragma__('noalias', 'Infinity')
__pragma__('noalias', 'keys')
__pragma__('noalias', 'get')
__pragma__('noalias', 'set')
__pragma__('noalias', 'type')
__pragma__('noalias', 'update')


def run_upgrader(creep):
    """
    Runs a creep as a generic upgrader.
    :param creep: The creep to run
    """
    if creep.carry.energy == 0:
        if creep.withdraw(Game.spawns.aamuuninenspawner, RESOURCE_ENERGY) == ERR_NOT_IN_RANGE:
            creep.moveTo(Game.spawns.aamuuninenspawner)
    else:
        #if sites are available, move to the nearest one
        sites = creep.room.find(FIND_MY_CONSTRUCTION_SITES)
        if len(sites) > 0 :
            if creep.build(sites[0])== ERR_NOT_IN_RANGE:
                creep.moveTo(sites[0])
        else:
            if creep.upgradeController() == ERR_NOT_IN_RANGE:
                creep.moveTo(creep.room.controller)
