from problem import Problem
import math
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
        current = problem.generate_start_state()
        best = current
        best_path = [current]  # Khởi tạo đường đi với trạng thái bắt đầu
        time = 0
        
        while True:
            T = schedule(time)
            if T <= 0:
                break
            next_state = random.choice(problem.get_neighbors(current))
            delta_e = problem.get_evaluation(next_state) - problem.get_evaluation(current)
            
            if delta_e > 0:
                current = next_state
                if problem.get_evaluation(current) > problem.get_evaluation(best):
                    best = current
                    if current in best_path:
                        best_path = best_path[:best_path.index(current) + 1]  # Cập nhật đường đi tốt nhất
                    else:
                        best_path.append(current)
                if current not in best_path:  # Make sure current is always in best_path
                    best_path.append(current)
            elif random.random() < math.exp(delta_e / T):
                current = next_state
                if current not in best_path:  # Make sure current is always in best_path
                    best_path.append(current)
            
            time += 1
        
        return best_path
    
    def exponential_schedule(t, k=20, lam=0.005, limit=1000):
        return k * math.exp(-lam * t) if t < limit else 0
    
    def local_beam_search(problem, k):
        current_states = [problem.generate_start_state() for _ in range(k)]
        best_path = []
        
        while True:
            next_states = []
            for state in current_states:
                neighbors = problem.get_neighbors(state)
                next_states.extend(neighbors)
        
            next_states.sort(key=lambda x: problem.get_evaluation(x), reverse=True)
            current_states = next_states[:k]

            if (len(best_path) == 0):
                best_path.append(current_states[0])
            elif (current_states[0] not in best_path) and ((problem.get_evaluation(current_states[0]) >= problem.get_evaluation(state)) for state in best_path):
                best_path.append(current_states[0])
            else:
                break
        
        return best_path
    
    def run_algorithm(algorithm_name):
        problem = Problem('monalisa.jpg')
                
        if algorithm_name == 'RRH':
            num_trial = 10
            best_path = LocalSearchStrategy.random_restart_hill_climbing(problem, num_trial)
            problem.draw_path(best_path)
            
        elif algorithm_name == 'SAS':
            schedule = LocalSearchStrategy.exponential_schedule # Sử dụng hàm schedule đã định nghĩa
            best_path = LocalSearchStrategy.simulated_annealing_search(problem, schedule)
            problem.draw_path(best_path)
            
        elif algorithm_name == 'LBS':
            k = 3
            best_path = LocalSearchStrategy.local_beam_search(problem, k)
            problem.draw_path(best_path)

            
        