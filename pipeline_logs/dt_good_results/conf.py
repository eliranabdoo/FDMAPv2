import os


class Delegator(type):
    def __getattribute__(self, item):
        try:
            return getattr(Config, item)
        except:
            return object.__getattribute__(self, item)


class Config(object):
    team_precision = 1
    sa_precision = 0.5
    num_traces = 150
    resources_dir = os.path.join(os.path.dirname(__file__), "Resources")
    solvers_dir = os.path.join(os.path.dirname(__file__), "CPPSolvers")

    cygwin_bash_path = os.path.join("D://Softwares//Cygwin//bin//bash.exe")

    problems_dir = os.path.join(resources_dir, "problems")
    traces_dir = os.path.join(resources_dir, "traces")
    graphs_dir = os.path.join(resources_dir, "graphs")
    logs_dir = os.path.join(resources_dir, "logs")

    problem_kind = "DecTiger"

    trace_format = '.trace'
    problem_format = '.pomdpx'
    graph_format = ".dot"

    sarsop_dir = os.path.join(solvers_dir, "sarsop", "src")
    sarsop_solve_team = os.path.join(sarsop_dir, "solve_team.txt")
    # sarsop_solve_single = os.path.join(sarsop_dir, "solve_single.txt")
    sarsop_solve_single = os.path.join(sarsop_dir, "solve_single_no_depth_limit.txt")

    projector = os.path.join(os.path.dirname(__file__), "TeamProblemProjector", "Projector.py")
    aligner = os.path.join(os.path.dirname(__file__), "GraphAlignment", "GraphAligner.py")
    simulations_dir = os.path.join(os.path.dirname(__file__), "DecPOMDPSimulator", "simulations")

    simulation_problems_dir = os.path.join(simulations_dir, "problems")
    simulation_policies_dir = os.path.join(simulations_dir, "policy_graphs")

    # manual pipeline run params
    problem_name = "DT-2x1_2A"

    # orchestrator params
    num_processes = 4
    pipeline_logs_dir_name = 'pipeline_logs'
    pipeline_team_problem_name_to_kind = {
        'BP-3x3_2A_2H_1L_TEAM': problem_kind,
        'BP-3x2_3A_0H_3L_TEAM': problem_kind

    }

    # pipeline flags
    SOLVE_TEAM = 1
    PROJECT = 1
    SOLVE_SINGLE = 1
    ALIGN = 1
    SIMULATE = 1

    # team and single timeout
    TIMEOUT = 3600

    # simulation params
    HORIZONS = [i for i in range(1, 50)]
    NUM_RUNS = 1000
    SIMULATIONS = ['sim_all']
