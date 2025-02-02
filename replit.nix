{ pkgs }: {
  deps = [
    pkgs.python38
    pkgs.python38Packages.flask
    pkgs.python38Packages.torch
    pkgs.python38Packages.transformers
  ];
}