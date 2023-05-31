import org.bukkit.Location;
import org.bukkit.Material;
import org.bukkit.World;
import org.bukkit.entity.Player;
import org.bukkit.event.EventHandler;
import org.bukkit.event.Listener;
import org.bukkit.event.player.PlayerInteractEvent;
import org.bukkit.inventory.ItemStack;
import org.bukkit.inventory.meta.ItemMeta;
import org.bukkit.plugin.java.JavaPlugin;
import org.bukkit.scheduler.BukkitRunnable;
import org.bukkit.inventory.Inventory;
import org.bukkit.inventory.ItemStack;
import org.bukkit.inventory.meta.ItemMeta;

public class MyPlugin extends JavaPlugin implements Listener {

    @Override
    public void onEnable() {
        getServer().getPluginManager().registerEvents(this, this);
    }

    @EventHandler
    public void onSnowballThrow(PlayerInteractEvent event) {
        if (event.getAction().toString().contains("LEFT_CLICK") && event.getItem() != null && event.getItem().getType() == Material.SNOWBALL) {
            Player player = event.getPlayer();
            showMenu(player);
        }
    }

    public void showMenu(Player player) {
        Inventory menu = getServer().createInventory(null, 9, "Snowball Menu");

        ItemStack teleportItem = new ItemStack(Material.CHEST);
        ItemMeta teleportItemMeta = teleportItem.getItemMeta();
        teleportItemMeta.setDisplayName("Teleport to Spawn");
        teleportItem.setItemMeta(teleportItemMeta);

        ItemStack noActionItem = new ItemStack(Material.STICK);
        ItemMeta noActionItemMeta = noActionItem.getItemMeta();
        noActionItemMeta.setDisplayName("No Action");
        noActionItem.setItemMeta(noActionItemMeta);

        menu.setItem(3, teleportItem);
        menu.setItem(5, noActionItem);

        player.openInventory(menu);
    }

    @EventHandler
    public void onMenuClick(PlayerInteractEvent event) {
        if (event.getAction().toString().contains("RIGHT_CLICK") && event.getItem() != null && event.getItem().getType() == Material.CHEST) {
            Player player = event.getPlayer();
            teleportToSpawn(player);
            event.setCancelled(true);
        } else if (event.getAction().toString().contains("RIGHT_CLICK") && event.getItem() != null && event.getItem().getType() == Material.STICK) {
            event.setCancelled(true);
        }
    }

    public void teleportToSpawn(Player player) {
        World world = player.getWorld();
        Location spawnLocation = world.getSpawnLocation();
        
        new BukkitRunnable() {
            @Override
            public void run() {
                player.teleport(spawnLocation);
            }
        }.runTaskLater(this, 5);
    }
}
