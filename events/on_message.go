package events

import (
	"fmt"
	"github.com/bwmarrin/discordgo"
	"ploxy/timings"
)

func OnMessage(client *discordgo.Session, message *discordgo.MessageCreate) {
	if message.Author.ID == client.State.User.ID {
		return
	}

	analysis, err := timings.TimingsAnalysis(message.Content)
	if err != nil {
		fmt.Println(err)
		return
	}
	fmt.Println(analysis)
	if len(analysis) >= 1 {
		// get the first 20 resulsts
		if len(analysis) > 20 {
			analysis = analysis[:20]
		}
		// create a string of the results

		embed := &discordgo.MessageEmbed{
			Title:       "Timings Analysis",
			Description: "Here's what I found:",
			Color:       0x00ff00, // Green
			Fields:      []*discordgo.MessageEmbedField{},
		}

		for _, result := range analysis {
			embed.Fields = append(embed.Fields, &discordgo.MessageEmbedField{
				Name:   result.Name,
				Value:  result.Value,
				Inline: result.Inline,
			})
		}

		_, err = client.ChannelMessageSendEmbed(message.ChannelID, embed)
		if err != nil {
			fmt.Println(err)
			return
		}

	}

}
