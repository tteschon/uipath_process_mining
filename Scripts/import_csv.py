import os
import pandas as pd
import pm4py

def import_csv(file_path):
    event_log = pm4py.format_dataframe(pd.read_csv(file_path, sep=';'), case_id='case_id', activity_key='activity',timestamp_key='timestamp')
    #current_dir = os.path.abspath(os.getcwd())
    #current_dir = str(current_dir).replace('\\','/') + '/'
    xes_file = os.path.abspath(file_path).replace('.csv','.xes')
    pm4py.write_xes(event_log, xes_file)
    event_log = pm4py.read_xes(xes_file)
    return event_log

def import_file(file_path):
    root, ext = os.path.splitext(file_path)
    if ext == '.csv':
        return import_csv(file_path)
    elif ext == '.xes':
        return pm4py.read_xes(file_path)
    else:
        return 'File type not supported'

def num_of_events(file_path):
    event_log = import_file(file_path)
    num_events = len(event_log)
    return num_events

def num_of_cases(file_path):
    event_log = import_file(file_path)
    num_cases = len(event_log.case_id.unique())
    return num_cases

def start_activities(file_path):
    event_log = import_file(file_path)
    start_act = pm4py.get_start_activities(event_log)
    return start_act

def end_activities(file_path):
    event_log = import_file(file_path)
    end_act = pm4py.get_end_activities(event_log)
    return end_act

def generate_bpmn(file_path):
    event_log = import_file(file_path)
    #event_log = pm4py.read_xes(file_path)
    process_tree = pm4py.discover_tree_inductive(event_log)
    bpmn_model = pm4py.convert_to_bpmn(process_tree)
    return pm4py.view_bpmn(bpmn_model)

def generate_process_tree(file_path):
    event_log = import_file(file_path)
    process_tree = pm4py.discover_tree_inductive(event_log)
    return pm4py.view_process_tree(process_tree)

def generate_process_map(file_path):
    event_log = import_file(file_path)
    dfg, start_activities, end_activities = pm4py.discover_dfg(event_log)
    return pm4py.view_dfg(dfg, start_activities, end_activities)

def generate_heruistics_map(file_path):
    event_log = import_file(file_path)
    #event_log = pm4py.read_xes(file_path)
    map = pm4py.discover_heuristics_net(event_log)
    return pm4py.view_heuristics_net(map)