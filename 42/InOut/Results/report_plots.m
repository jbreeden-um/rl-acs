RLlin = load('RL_pid_F180_A70_Long.42');

timeL = RLlin(:,1)/5554;
momentumL = RLlin(:,3:5);
actuatorsL = RLlin(:,9:11);

figure(1); clf;
plot(timeL, momentumL);
xlabel 'Orbit'; ylabel 'N-m';
title 'Internal Momentum under u_{nom}';
reward = -mean(vecnorm(momentumL,2,2))
legend x y z Location NorthWest

%%
RLbest = load('RL_cqlStochpidDouble2000Ep40_F180_A70.42');

timeB = RLbest(:,1)/5554;
momentumB = RLbest(:,3:5);
actuatorsB = RLbest(:,9:11);

figure(2); clf;
plot(timeB, momentumB);
xlabel 'Orbit'; ylabel 'N-m';
title 'Internal Momentum under case 20';
legend x y z Location NorthWest

%%
RLover = load('RL_cqlStochpid2000Ep40_F180_A70.42');

timeO = RLover(:,1)/5554;
momentumO = RLover(:,3:5);
actuatorOB = RLover(:,9:11);

figure(3); clf;
plot(timeO, momentumO);
xlabel 'Orbit'; ylabel 'N-m';
title 'Internal Momentum under case 15';
legend x y z Location SouthWest

%%
figure(4); clf;
l1 = plot(timeL(1:27771), actuatorsL(1:27771,1)); hold on;
l2 = plot(timeL(1:27771), actuatorsL(1:27771,2));
l3 = plot(timeL(1:27771), actuatorsL(1:27771,3));
plot(timeB, actuatorsB(:,1), '--', 'Color', l1.Color);
plot(timeB, actuatorsB(:,2), '--', 'Color', l2.Color);
plot(timeB, actuatorsB(:,3), '--', 'Color', l3.Color);
xlabel 'Orbit'; ylabel 'A-m^2';
title 'Control Inputs';
legend u_{x,nom} u_{y,nom} u_{z,nom} u_{x,20} u_{y,20} u_{z,20} Location NorthWest
