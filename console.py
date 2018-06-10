#!/usr/bin/env python3
''' Contains console '''

import cmd
import models
from import_classes import *


class HBNBCommand(cmd.Cmd):
        ''' Console / command interpreter '''

        def do_quit(self, args):
                '''Quit command to exit the program '''
                raise SystemExit

        def do_EOF(self, args):
                '''Quit command to exit the program '''
                raise SystemExit

        def do_create(self, args):
                '''Creates a new instance '''
                args = args.split()
                if len(args) == 0:
                        print('** class name missing **')
                elif args[0] not in my_classes:
                        print('** class doesn\'t exist **')
                else:
                        eval('{}()'.format(args[0]))

        def do_show(self, args):
                '''Prints an instance '''
                args = args.split()
                if len(args) == 0:
                        print('** class name missing **')
                elif args[0] not in my_classes:
                        print('** class doesn\'t exist **')
                        return

                if len(args) == 1:
                        print('** instance id missing **')
                        return

                for (key, value) in models.storage.all().items():
                        if key == args[0] + '.' + args[1]:
                                print(value)
                                return
                print('** no instance found **')

        def do_destroy(self, args):
                '''Destroy an instance '''
                args = args.split()
                if len(args) == 0:
                        print('** class name missing **')
                elif args[0] not in my_classes:
                        print('** class doesn\'t exist **')
                        return

                if len(args) == 1:
                        print('** instance id missing **')
                        return

                obj_dict = models.storage.all()
                for (key, value) in obj_dict.items():
                        if key == args[0] + '.' + args[1]:
                                models.storage.delete(key)
                                return
                print('** no instance found **')

        def do_all(self, args):
                '''Prints all instances of a class or all classes '''
                args = args.split()
                instance_list = []
                for instance in args:
                        if args[0] not in my_classes:
                                print('** class doesn\'t exist **')

                if len(args) > 0:
                        for instance in models.storage.all().values():
                                if instance.__class__.__name__ in args:
                                        instance_list.append(instance)
                else:
                        for instance in models.storage.all().values():
                                instance_list.append(instance)
                print(instance_list)

        def do_update(self, args):
                '''Updates an instance '''
                args = args.split()
                if len(args) == 0:
                        print('** class name missing **')
                        return
                if args[0] not in my_classes:
                        print('** class doesn\'t exist **')
                        return
                if len(args) == 1:
                        print('** instance id missing **')
                        return
                for (key, value) in models.storage.all().items():
                        if key == args[0] + '.' + args[1]:
                                if len(args) == 2:
                                        print('** attribute name missing **')
                                        return
                                if len(args) == 3:
                                        print('** value missing **')
                                        return
                                models.storage.update(key, args[2], args[3])
                                '''value.__dict__[args[2]] = args[3]'''
                                return
                print('** no instance found **')

        def emptyline(self):
                ''' Does not repeat prev command on empty line '''
                pass

        def precmd(self, line):
                ''' parses line if line has . syntax '''
                if line.endswith(')'):
                        line = list(line.rpartition('.'))
                        parameters = list(line[2].partition('('))[2]
                        parameters = parameters.rstrip(')')
                        parameters = parameters.split(', ')
                        parameters = ' '.join(parameters)
                        line[2] = (line[2].partition('('))[0]
                        return line[2] + ' ' + line[0] + ' ' + parameters
                return line


if __name__ == '__main__':
        hbnb_console = HBNBCommand()
        hbnb_console.prompt = '(hbnb) '
        hbnb_console.cmdloop()
