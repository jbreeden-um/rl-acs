load time.42
load RL.42

momentum = RL(:,1:3);
angles = RL(:,4:6);
actuators = RL(:,7:9);

figure(1); clf;
plot(time, momentum);
xlabel 'Time (s)'; ylabel 'N-m';
title 'Internal Momentum';

figure(2); clf;
plot(time, rad2deg(angles));
xlabel 'Time (s)'; ylabel 'deg';
legend \nu \Theta \beta
title 'Simplified Position';

figure(3); clf;
plot(time, actuators);
xlabel 'Time (s)'; ylabel 'A-m^2';
title 'Control Inputs';