import unittest

from net_flow_opt.sampling import GroupingStructureSampling
from net_flow_opt.model import DiscreteModel
from net_flow_opt.utils import structure, components
from net_flow_opt.network import System


class TestGroupSampling(unittest.TestCase):

    def setUp(self) -> None:
        self.system = System(structure, components)

    def test_group_sampling(self):
        problem = DiscreteModel(system=self.system, resources=4)
        sampling = GroupingStructureSampling()
        X = sampling(problem, 10).get("x")

