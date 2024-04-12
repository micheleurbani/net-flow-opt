import numpy as np

from pymoo.core.sampling import Sampling


class GroupingStructureSampling(Sampling):

    def _do(self, problem, n_samples, **kwargs):
        r = problem.r
        N = problem.system.N
        val = np.zeros((n_samples, N), dtype=int)
        for ind in val:
            g_id = 1
            # print(np.sum(val[i] == 0))
            while np.sum(ind == 0) > r:
                # sample group size
                g_size = np.random.randint(r)
                to_be_assigned = np.arange(N)[ind == 0]
                assigned = np.random.choice(to_be_assigned, g_size, replace=False)
                # assigned sampled items to a group
                ind[assigned] = g_id
                g_id += 1
        return val


if __name__ == "__main__":
    pass
