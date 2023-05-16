# sudo User hinzufügen

=== "Debian/Ubuntu"

    ``` bash
    sudo usermod -aG sudo john
    ```

=== "Amazon Linux 2"

    ``` bash
    sudo usermod -aG wheel john
    ```