from problem import Problem

import random


class LocalSearchStrategy:
    def random_restart_hill_climbing(problem, num_trial):
        best_path = []
        
        if num_trial > 0:
            for _ in range(num_trial):
                current_state = problem.generate_start_state()
                while True:
                    neighbors = problem.get_neighbors(current_state)
                    next_state = max(neighbors, key=problem.get_evaluation)
                    if problem.get_evaluation(next_state) >= problem.get_evaluation(current_state):
                        best_path.append(next_state)
                        break
                        
                    current_state = next_state
        else:
            print("ERROR!!!")
            
        return best_path
    
    def simulated_annealing_search(problem, schedule):
        best_path = None
        
        return best_path
    
    def local_beam_search(problem, k):
        current_states = [problem.generate_start_state() for _ in range(k)]
        best_states = []
        
        while True:
            next_states = []
            for state in current_states:
                neighbors = problem.get_neighbors(state)
                next_states.extend(neighbors)
        
            next_states.sort(key=lambda x: problem.get_evaluation(x), reverse=True)
            current_states = next_states[:k]

            if (len(best_states) == 0):
                best_states.append(current_states[0])
            elif (current_states[0] not in best_states) and ((current_states[0][2] >= state[2]) for state in best_states):
                
                best_states.append(current_states[0])
            else:
                break
        
        return best_states
    
    def run_algorithm(algorithm_name):
        problem = Problem('monalisa.jpg')
                
        if algorithm_name == 'RRH':
            num_trial = 10
            best_path = LocalSearchStrategy.random_restart_hill_climbing(problem, num_trial)
            problem.draw_path(best_path)
            
        elif algorithm_name == 'SAS':
            schedule = 0
            best_path = LocalSearchStrategy.simulated_annealing_search(problem, schedule)
            problem.draw_path(best_path)
            
        elif algorithm_name == 'LBS':
            k = 3
            best_path = LocalSearchStrategy.local_beam_search(problem, k)
            problem.draw_path(best_path)

            
        