% load time.42
load RL.42

time = RL(:,1);
momentum = RL(:,3:5);
angles = RL(:,6:8);
actuators = RL(:,9:11);

%%
figure(1); clf;
plot(time, momentum);
xlabel 'Time (s)'; ylabel 'N-m';
title 'Internal Momentum';
hold on;
plot(time, .05*ones(size(time)), 'r--')

figure(2); clf;
plot(time, rad2deg(angles));
xlabel 'Time (s)'; ylabel 'deg';
legend \nu \Theta \beta
title 'Simplified Position';

figure(3); clf;
plot(time, actuators);
xlabel 'Time (s)'; ylabel 'A-m^2';
title 'Control Inputs';