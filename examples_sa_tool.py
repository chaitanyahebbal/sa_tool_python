from sa_tool import sa_tool
import networkx as nx

if __name__ == '__main__' :
    B = nx.Graph(name=" youbot platform")
#    B.add_nodes_from(['h', 'h_dot', 'q_i', 'q_o'], bipartite=0, color='r', type='unknown') # Add the node attribute "bipartite"
#    B.add_nodes_from(['u', 'y'], bipartite=0, color='r', type='known') # Add the node attribute "bipartite"
#    B.add_nodes_from(['c1','c2','c3', 'c4', 'c5', 'c6'], bipartite=1, color='b')
#    B.add_edges_from([('u','c2'),('u','c5')])
#    B.add_edges_from([('h_dot','c1'),('h_dot','c6') ])
#    B.add_edges_from([('h','c6'),('h','c3'),('h','c4') ])
#    B.add_edges_from([('h', 'c6')], derivative_casuality=True)
#    B.add_edges_from([('q_i','c1'),('q_i','c2')])
#    B.add_edges_from([('q_o','c3'),('q_o','c1')])
#    B.add_edges_from([('y','c5'),('y','c4')])
    B.add_nodes_from(['theta1', 'theta2', 'theta3', 'theta4',
                      'p1_dot', 'p2_dot', 'p3_dot', 'p4_dot','p1', 'p2', 'p3', 'p4'], bipartite=0, color='r', type='unknown') # Add the node attribute "bipartite"
    B.add_nodes_from(['theta1_dot', 'theta2_dot', 'theta3_dot', 'theta4_dot'
                      ], bipartite=0, color='r', type='known') # Add the node attribute "bipartite"
    B.add_nodes_from(['c1','c2','c3', 'c4', 'c5', 'c6',
                      'c7','c8','c9', 'c10', 'c11', 'c12',
                      'c13','c14','c15', 'c16'], bipartite=1, color='b')

    B.add_edges_from([('p1','c9'),('p1','c2')])
    B.add_edges_from([('p1', 'c9')], derivative_casuality=True)
    B.add_edges_from([('p2','c4'),('p2','c11')])
    B.add_edges_from([('p2', 'c11')], derivative_casuality=True)
    B.add_edges_from([('p3','c6'),('p3','c13')])
    B.add_edges_from([('p3', 'c13')], derivative_casuality=True)
    B.add_edges_from([('p4','c8'),('p4','c15')])
    B.add_edges_from([('p4', 'c15')], derivative_casuality=True)
    
    #B.add_edges_from([('p1', 'c9')], derivative_casuality=True)
                    

    B.add_edges_from([('p1_dot','c9'),('p1_dot','c10')])
    B.add_edges_from([('p2_dot','c11'),('p2_dot','c12')])
    B.add_edges_from([('p3_dot','c13'),('p3_dot','c14')])
    B.add_edges_from([('p4_dot','c15'),('p4_dot','c16')])    
    

    
    B.add_edges_from([('theta1','c1')])
    B.add_edges_from([('theta1', 'c1')], derivative_casuality=True)
    B.add_edges_from([('theta2','c3')])
    #B.add_edges_from([('theta2', 'c3')], derivative_casuality=True)
    B.add_edges_from([('theta3','c5')])
    #B.add_edges_from([('theta3', 'c5')], derivative_casuality=True)
    B.add_edges_from([('theta4','c7')])
    #B.add_edges_from([('theta4', 'c7')], derivative_casuality=True)
    
    B.add_edges_from([('theta1_dot','c1'),('theta1_dot','c2'),
                      ('theta1_dot','c4'),('theta1_dot','c6'),
                      ('theta1_dot','c8'),('theta1_dot','c10')])
    B.add_edges_from([('theta2_dot','c2'),('theta2_dot','c3'),
                      ('theta2_dot','c4'),('theta2_dot','c6'),
                      ('theta2_dot','c8'),('theta2_dot','c12')])
    B.add_edges_from([('theta3_dot','c2'),('theta3_dot','c4'),
                      ('theta3_dot','c5'),('theta3_dot','c6'),
                      ('theta3_dot','c8'),('theta3_dot','c14')])
    B.add_edges_from([('theta4_dot','c2'),('theta4_dot','c4'),
                      ('theta4_dot','c6'),('theta4_dot','c7'),
                      ('theta4_dot','c8'),('theta4_dot','c16')])

    print (B.edges())
    
    sa1 = sa_tool.SATool(B)
    #sa1.calculate_maximum_matching_max_flow_algorithm()
    sa1.visualize_bipartite()
    #sa1.calculate_maximum_matching()
    sa1.calculate_matching_ranking_constraints()
    sa1.visualize_bipartite(with_matching=True)
    sa1.visualize_bipartite(with_orientation=True)
    
