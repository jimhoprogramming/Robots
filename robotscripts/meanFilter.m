## Copyright (C) 2016 Administrator
## 
## This program is free software; you can redistribute it and/or modify it
## under the terms of the GNU General Public License as published by
## the Free Software Foundation; either version 3 of the License, or
## (at your option) any later version.
## 
## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.
## 
## You should have received a copy of the GNU General Public License
## along with this program.  If not, see <http://www.gnu.org/licenses/>.

## -*- texinfo -*- 
## @deftypefn {Function File} {@var{retval} =} meanFilter (@var{input1}, @var{input2})
##
## @seealso{}
## @end deftypefn

## Author: Administrator <Administrator@PC-XP>
## Created: 2016-05-22

function Ip= meanFilter (M,N,I)
  dpi=size(I);
  Ip=zeros(dpi);
  for x=1:dpi(1)
    for y=1:dpi(2)
      x1=x-fix(M/2);
      x2=x+fix(M/2);
      y1=y-fix(N/2);
      y2=y+fix(N/2);    
      if (x1<=0)
        x1=1;
      endif
      if (x2>=dpi(1))
        x2=dpi(1);
      endif
      if (y1<=0)
        y1=1;
      endif
      if (y2>=dpi(2))
        y2=dpi(2);
      endif           
      temp=I(x1:x2,y1:y2);
      Ip(x,y)=mean(mean(temp));
     endfor
   endfor
endfunction
