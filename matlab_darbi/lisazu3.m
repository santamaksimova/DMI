function lisazu2(f1,f2)
% animētā Lisažu figūra
% šī ir funkcija
% to izsauc tikai no
% komandlog
% ar komandu lisazu(2,3)
% ar run tā nestrādās
t = 0:0.01:1;
%f1 = 7; f2 = 8;
shg
for faze = 0:pi/100:2*pi
x = cos(2*pi*f1*t+faze);
y = sin(2*pi*f2*t);
plot(x,y)
pause(0.02)
end