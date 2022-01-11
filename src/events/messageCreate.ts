import discord from 'discord.js';
import { badWordCheck } from '../utils/badWordCheck';
import { copyPastaCheck } from '../utils/copyPastaCheck';
import { RedisClientType } from 'redis';

let redis: RedisClientType;

module.exports = {
	name: 'messageCreate',
	async execute(message: discord.Message) {
		console.log("Message sent");
		const badwords = await badWordCheck(message.content, true);
    const copyPastas = await copyPastaCheck(message.content);
    
	},
  setRedis: function(redis: RedisClientType) {
    redis = redis;
  }
};