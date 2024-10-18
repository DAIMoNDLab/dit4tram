from simulation.sim import Simulation

if __name__ == "__main__":

    # Runs test of bordeaux scenario w default tl logic
    sim = Simulation()

    sim.start("./simulation/bordeaux/bordeaux.sumocfg", gui=True)

    while sim.is_running():
        sim_data = sim.step_through()