--[[
    Written by 6Ex.
    Part of the banning system from a discord bot.
    Sorry for the messy code, I'm a relatively new coder.
    Thanks, 6Ex.
]]
local HttpService = game:GetService("HttpService")
game.Players.PlayerAdded:Connect(
    function(plr)
        local name = plr.Name
        local id = plr.UserId
        local database = HttpService:GetAsync("") --Put the direct url to the bannedplayers.txt file on your PHP Web Server (In  Server [PHP])

        if string.find(database, tostring(id)) then
            print("A banned player attempted to join the game!\nUsername : " .. name .. "")
            plr:Kick("You've been banned from this game!")
        else
            print("A player joined the game!\nUsername : " .. name .. "")
        end
    end
)
