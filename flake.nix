{
	description = "Ansible system development";
	inputs = {
		stable.url = "github:NixOS/nixpkgs/nixos-21.11";
	};

	outputs = {stable, ...}@inputs:
	let
		system = "x86_64-linux";
		pkgs = stable.legacyPackages."${system}";
	in {
		devShell."${system}" = with pkgs; pkgs.mkShell {
			buildInputs = [
				ansible
				python39Packages.tox
				vagrant
				podman
			];
		};
	};
}
