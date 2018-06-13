#!/usr/bin/env python3
''' Contains console '''

import cmd
import shlex
import models
import datetime
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
                args = shlex.split(args)
                if len(args) == 0:
                        print('** class name missing **')
                elif args[0] not in my_classes:
                        print('** class doesn\'t exist **')
                else:
                        eval('{}()'.format(args[0]))

        def do_show(self, args):
                '''Prints an instance '''
                args = shlex.split(args)
                if len(args) == 0:
                        print('** class name missing **')
                        return
                elif args[0] not in my_classes:
                        print('** class doesn\'t exist **')
                        return

                if len(args) == 1:
                        print('** instance id missing **')
                        return

                obj_dict = models.storage.all()
                key = args[0] + '.' + args[1]
                if key in obj_dict.keys():
                        print(obj_dict[key])
                        return

                print('** no instance found **')

        def do_destroy(self, args):
                '''Destroy an instance '''
                args = shlex.split(args)
                if len(args) == 0:
                        print('** class name missing **')
                        return
                elif args[0] not in my_classes:
                        print('** class doesn\'t exist **')
                        return

                if len(args) == 1:
                        print('** instance id missing **')
                        return

                obj_dict = models.storage.all()
                key = args[0] + '.' + args[1]
                if key in obj_dict.keys():
                        models.storage.delete(key)
                        return

                print('** no instance found **')

        def do_all(self, args):
                '''Prints all instances of a class or all classes '''
                args = shlex.split(args)
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
                args = shlex.split(args)

                if len(args) == 0:
                        print('** class name missing **')
                        return
                if args[0] not in my_classes:
                        print('** class doesn\'t exist **')
                        return
                if len(args) == 1:
                        print('** instance id missing **')
                        return

                key = args[0] + '.' + args[1]
                if key not in models.storage.all().keys():
                        print('** no instance found **')
                        return

                if len(args) == 2:
                        print('** attribute name missing **')
                        return
                for i in range(2, len(args), 2):
                        if i + 1 >= len(args):
                                print('** value missing **')
                                return
                        models.storage.update(key, args[i], args[i + 1])

        def emptyline(self):
                ''' Does not repeat prev command on empty line '''
                pass

        def precmd(self, line):
                ''' parses line if line has . syntax '''
                if line.endswith(')'):
                        line = list(line.partition('.'))
                        parameters = (line[2].partition)('(')[2]
                        parameters = parameters.rstrip(')')
                        line[2] = line[2].partition('(')[0]

                        split_params = shlex.split(parameters)

                        if (len(split_params) >= 2 and
                           split_params[1].startswith('{')):
                                parameters = parameters.partition('{')
                                obj_id = shlex.split(parameters[0])[0]
                                obj_id = obj_id[:-1]
                                parameters = parameters[1] + parameters[2]

                                parameters = eval(parameters)
                                if type(parameters) is not dict:
                                        print('** no sets **')
                                        return

                                new_str = ''
                                for (key, value) in parameters.items():
                                        pair = repr(key) + ' ' + repr(value)
                                        new_str = ' '.join([new_str, pair])
                                parameters = obj_id + ' ' + new_str
                        else:
                                for i in range(len(split_params) - 1):
                                        split_params[i] = split_params[i][:-1]

                                parameters = ' '.join(
                                             [repr(x) for x in split_params])

                        return ' '.join([line[2], line[0], parameters])

                return line


if __name__ == '__main__':
        hbnb_console = HBNBCommand()
        hbnb_console.prompt = '(hbnb) '
        hbnb_console.cmdloop()
