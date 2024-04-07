from problem import Problem

import random


class LocalSearchStrategy:
    
    def random_restart_hill_climbing(problem, num_trial):
        best_path = None
        
        return best_path
    
    def simulated_annealing_search(problem, schedule):
        best_path = None
        
        return best_path
    
    def local_beam_search(problem, k):
        best_path = None
        
        return best_path
    
    def run_algorithm(algorithm_name):
        problem = Problem('monalisa.jpg')
        
        if algorithm_name == 'RRH':
            num_trials = 0
            best_path = LocalSearchStrategy.random_restart_hill_climbing(problem, num_trials)
            problem.draw_path(best_path)
            
        elif algorithm_name == 'SAS':
            schedule = 0
            best_path = LocalSearchStrategy.simulated_annealing_search(problem, schedule)
            problem.draw_path(best_path)
            
        elif algorithm_name == 'LBS':
            k = 0
            best_path = LocalSearchStrategy.local_beam_search(problem, k)
            problem.draw_path(best_path)

            
        