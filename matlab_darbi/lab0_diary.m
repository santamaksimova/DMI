format compact
pi
ans =
    3.1416
%% izveidosim matricu
A = [1 2 3 4 5 6 ; 7 8 9 10 11 12]
A =
     1     2     3     4     5     6
     7     8     9    10    11    12
%% Uzzīmēsim grafiku
% zīmēsim 2.kārtas polinomu
C = [2 4 6];
x = -6:2:6;
y = C(1)*x^2+C(2)*x+C(3)
{??? Error using ==> mpower
Matrix must be square.
} 
y = C(1)*x.^2+C(2)*x+C(3)
y =
    54    22     6     6    22    54   102
plot(x,y)% funkcija plot zīmē grafiku
%samazināsim soli
x2 = -6:0.01:6;
y2 = C(1)*x2.^2+C(2)*x2+C(3);
shg
% vairāki grafiki uz vienām asīm
plot(x,y,x2,y2)
% līnijas izskata maiņa (1)
plot(x,y)
plot(x,y,'o')
plot(x,y,'g')
plot(x,y,':')
plot(x,y,'og:')

plot(x,y,'yd--')
plot(x,y,'kh:')

plot(x,y,'m*;')
{??? Error using ==> plot
Error in color/linetype argument
} 
plot(x,y,'m*:')
% vairāki grafiki uz vienām asīm (papildinājums)
plot(x,y,'o',x2,y2)
% citas grafiskās funkcijas
steam(x,y)
{??? Undefined function or method 'steam' for input arguments of type 'double'.
} 
stem(x,y)
stairs(x,y)
%% vairāki grafiki uz vienām asīm (2)
t = 0:0.01:1
t =
  Columns 1 through 8
         0    0.0100    0.0200    0.0300    0.0400    0.0500    0.0600    0.0700
  Columns 9 through 16
    0.0800    0.0900    0.1000    0.1100    0.1200    0.1300    0.1400    0.1500
  Columns 17 through 24
    0.1600    0.1700    0.1800    0.1900    0.2000    0.2100    0.2200    0.2300
  Columns 25 through 32
    0.2400    0.2500    0.2600    0.2700    0.2800    0.2900    0.3000    0.3100
  Columns 33 through 40
    0.3200    0.3300    0.3400    0.3500    0.3600    0.3700    0.3800    0.3900
  Columns 41 through 48
    0.4000    0.4100    0.4200    0.4300    0.4400    0.4500    0.4600    0.4700
  Columns 49 through 56
    0.4800    0.4900    0.5000    0.5100    0.5200    0.5300    0.5400    0.5500
  Columns 57 through 64
    0.5600    0.5700    0.5800    0.5900    0.6000    0.6100    0.6200    0.6300
  Columns 65 through 72
    0.6400    0.6500    0.6600    0.6700    0.6800    0.6900    0.7000    0.7100
  Columns 73 through 80
    0.7200    0.7300    0.7400    0.7500    0.7600    0.7700    0.7800    0.7900
  Columns 81 through 88
    0.8000    0.8100    0.8200    0.8300    0.8400    0.8500    0.8600    0.8700
  Columns 89 through 96
    0.8800    0.8900    0.9000    0.9100    0.9200    0.9300    0.9400    0.9500
  Columns 97 through 101
    0.9600    0.9700    0.9800    0.9900    1.0000
fl=1;f2 = 1
f2 =
     1
y1 = sin(2*pi*f*t);
{??? Undefined function or variable 'f'.
} 
y1 = sin(2*pi*f1*t);
{??? Undefined function or variable 'f1'.
} 
y1 = sin(2*pi*f1*t);
{??? Undefined function or variable 'f1'.
} 
fl=1;
y1 = sin(2*pi*f1*t);
{??? Undefined function or variable 'f1'.
} 
f1=1;
y1 = sin(2*pi*f1*t);
y2 = sin(2*pi*f2*t);
stairs(t,y1,'k')
hold on % iesaldēt asis
stairs(t,y2,'r')
hold off % izslēgt iesaldēšanu
xlabel('t,s')
ylabel('U,V')
grid
title('Mans pirmais grafiks')
legend('sinusoīda','kosinusoīda')
gtext('teksts, ko ieliksim ar peles palīdzību')
% datu nolasīšana
ginput(2)
ans =
    0.4528   -0.2273
    0.4528   -0.2273
% interaktīva grafika maiņa
hold on % iesaldēt asis
stairs(t,y1,'k')
y2 = cos(2*pi*f2*t);
stairs(t,y2,'r')
mans_grafiks(t,y1,y2)
{??? Index exceeds matrix dimensions.

Error in ==> <a href="matlab: opentoline('/home/user/matlab_darbi/mans_grafiks.m',24,0)">mans_grafiks at 24</a>
set(stairs1(2),'Color',[1 0 0],'DisplayName','kosinusoīda');
} 
mans_grafiks(t,y1,y2)
{??? Index exceeds matrix dimensions.

Error in ==> <a href="matlab: opentoline('/home/user/matlab_darbi/mans_grafiks.m',24,0)">mans_grafiks at 24</a>
set(stairs1(2),'Color',[1 0 0],'DisplayName','kosinusoīda');
} 
%% Lisažu figūras
edit
lisazu
lisazu
lisazu
hold off
lisazu
lisazu(6,7)
{??? Attempt to execute SCRIPT lisazu as a function:
/home/user/matlab_darbi/lisazu.m
} 
lisazu2(6,7)
{??? Attempt to execute SCRIPT lisazu2 as a function:
/home/user/matlab_darbi/lisazu2.m
} 
lisazu2(4,5)
{??? Attempt to execute SCRIPT lisazu2 as a function:
/home/user/matlab_darbi/lisazu2.m
} 
lisazu2(4,5)
lisazu2(4,8)
help lisazu2
  šī ir funkcija
  to izsauc tikai no
  komandlog
  ar komandu lisazu(2,3)
  ar run tā nestrādās

lisazu3(2,3)
lisazu3(2,3)
uiopen('/home/user/matlab_darbi/lisazu3.m',1)
lisazu3(2,3)
diary off
