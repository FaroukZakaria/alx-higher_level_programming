#!/usr/bin/node

import { argv } from 'node:process';

argv.forEach((val, index) => {
	  console.log(`${index}: ${val}`);
});

const args = argv.slice(2);

if (args.length === 0)
{
	  console.log('No argument');
} else if (args.length === 1)
{
	  console.log('Argument found');
} else
{
	  console.log('Arguments found');
}
