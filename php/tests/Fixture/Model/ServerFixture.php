<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use DateTime;
use Prefabcortex\Hetzner\Model\Architecture;
use Prefabcortex\Hetzner\Model\CreatedFrom;
use Prefabcortex\Hetzner\Model\DeprecationInfo;
use Prefabcortex\Hetzner\Model\DnsPtr;
use Prefabcortex\Hetzner\Model\Image;
use Prefabcortex\Hetzner\Model\ImageStatus;
use Prefabcortex\Hetzner\Model\ImageType;
use Prefabcortex\Hetzner\Model\Iso;
use Prefabcortex\Hetzner\Model\IsoType;
use Prefabcortex\Hetzner\Model\Location;
use Prefabcortex\Hetzner\Model\LocationPrice;
use Prefabcortex\Hetzner\Model\OsFlavor;
use Prefabcortex\Hetzner\Model\Price;
use Prefabcortex\Hetzner\Model\Protection;
use Prefabcortex\Hetzner\Model\Server;
use Prefabcortex\Hetzner\Model\ServerPrivateNetItem;
use Prefabcortex\Hetzner\Model\ServerProtection;
use Prefabcortex\Hetzner\Model\ServerPublicNet;
use Prefabcortex\Hetzner\Model\ServerPublicNetIpv4;
use Prefabcortex\Hetzner\Model\ServerPublicNetIpv6;
use Prefabcortex\Hetzner\Model\ServerStatus;
use Prefabcortex\Hetzner\Model\ServerType;
use Prefabcortex\Hetzner\Model\ServerTypeCpuType;
use Prefabcortex\Hetzner\Model\ServerTypeLocationsItem;
use Prefabcortex\Hetzner\Model\ServerTypeStorageType;
use Prefabcortex\Hetzner\Validator\ServerConstraint;
use Symfony\Component\Validator\Constraint;

final class ServerFixture
{
    public static function build(): Server
    {
        $ipv4 = ServerPublicNetIpv4::builder(
            // ip
            '1.2.3.4',
            // blocked
            false,
            // dnsPtr
            'server01.example.com',
        )
            ->setId(42)
            ->build();
        $dnsPtr = DnsPtr::builder(
            // ip
            '2001:db8::1',
            // dnsPtr
            'server.example.com',
        )->build();
        $ipv6 = ServerPublicNetIpv6::builder(
            // ip
            '2001:db8::/64',
            // blocked
            false,
            // dnsPtr
            [$dnsPtr],
        )
            ->setId(42)
            ->build();
        $publicNet = ServerPublicNet::builder(
            // ipv4
            $ipv4,
            // ipv6
            $ipv6,
            // floatingIps
            [478],
        )->build();
        $serverPrivateNetItem = ServerPrivateNetItem::builder()
            ->setNetwork(4711)
            ->setIp('10.0.0.2')
            ->setAliasIps(['10.0.0.3', '10.0.0.4'])
            ->setMacAddress('86:00:ff:2a:7d:e1')
            ->build();
        $priceHourly = Price::builder(
            // net
            '1.0000',
            // gross
            '1.1900',
        )->build();
        $priceMonthly = Price::builder(
            // net
            '1.0000',
            // gross
            '1.1900',
        )->build();
        $pricePerTbTraffic = Price::builder(
            // net
            '1.0000',
            // gross
            '1.1900',
        )->build();
        $locationPrice = LocationPrice::builder(
            // location
            'fsn1',
            // priceHourly
            $priceHourly,
            // priceMonthly
            $priceMonthly,
            // includedTraffic
            654321,
            // pricePerTbTraffic
            $pricePerTbTraffic,
        )->build();
        $deprecation = DeprecationInfo::builder(
            // unavailableAfter
            new DateTime('2024-01-01'),
            // announced
            new DateTime('2024-01-01'),
        )->build();
        $serverTypeLocationsItem = ServerTypeLocationsItem::builder(
            // id
            42,
            // name
            'fsn1',
            // deprecation
            $deprecation,
            // recommended
            false,
            // available
            true,
        )->build();
        $serverType = ServerType::builder(
            // id
            1,
            // name
            'cpx22',
            // description
            'CPX22',
            // cores
            2,
            // memory
            4.0,
            // disk
            80.0,
            // deprecated
            false,
            // prices
            [$locationPrice],
            // storageType
            ServerTypeStorageType::local,
            // cpuType
            ServerTypeCpuType::shared,
            // architecture
            Architecture::x86,
            // locations
            [$serverTypeLocationsItem],
        )
            ->setCategory('Shared vCPU')
            ->build();
        $location = Location::builder(
            // id
            42,
            // name
            'fsn1',
            // description
            'Falkenstein DC Park 1',
            // country
            'DE',
            // city
            'Falkenstein',
            // latitude
            50.47612,
            // longitude
            12.370071,
            // networkZone
            'eu-central',
        )->build();
        $createdFrom = CreatedFrom::builder(
            // id
            1,
            // name
            'Server',
        )->build();
        $protection = Protection::builder(false)->build();
        $deprecation_1 = DeprecationInfo::builder(
            // unavailableAfter
            new DateTime('2024-01-01'),
            // announced
            new DateTime('2024-01-01'),
        )->build();
        $image = Image::builder(
            // id
            42,
            // type
            ImageType::system,
            // status
            ImageStatus::available,
            // name
            'ubuntu-24.04',
            // description
            'Ubuntu 24.04 Standard 64 bit',
            // imageSize
            2.3,
            // diskSize
            10.0,
            // created
            new DateTime('2024-01-01'),
            // createdFrom
            $createdFrom,
            // boundTo
            0,
            // osFlavor
            OsFlavor::ubuntu,
            // osVersion
            '24.04',
            // protection
            $protection,
            // deprecated
            new DateTime('2024-01-01'),
            // deprecation
            $deprecation_1,
            // deleted
            'REPLACE_ME',
            // labels
            [],
            // architecture
            Architecture::x86,
        )
            ->setRapidDeploy(false)
            ->build();
        $deprecation_2 = DeprecationInfo::builder(
            // unavailableAfter
            new DateTime('2024-01-01'),
            // announced
            new DateTime('2024-01-01'),
        )->build();
        $iso = Iso::builder(
            // id
            42,
            // name
            'FreeBSD-11.0-RELEASE-amd64-dvd1',
            // description
            'FreeBSD 11.0 x64',
            // type
            IsoType::public,
            // deprecation
            $deprecation_2,
            // architecture
            Architecture::x86,
        )->build();
        $protection_1 = ServerProtection::builder(
            // delete
            false,
            // rebuild
            false,
        )->build();

        return Server::builder(
            // id
            42,
            // name
            'my-resource',
            // status
            ServerStatus::running,
            // created
            new DateTime('2024-01-01'),
            // publicNet
            $publicNet,
            // privateNet
            [$serverPrivateNetItem],
            // serverType
            $serverType,
            // location
            $location,
            // image
            $image,
            // iso
            $iso,
            // rescueEnabled
            false,
            // locked
            false,
            // backupWindow
            '22-02',
            // outgoingTraffic
            123456,
            // ingoingTraffic
            123456,
            // includedTraffic
            654321,
            // protection
            $protection_1,
            // labels
            [],
            // primaryDiskSize
            50.0,
        )->build();
    }

    /** @return callable(array<int|string, mixed>): Server */
    public static function reader(): callable
    {
        return Server::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return ServerConstraint::constraints();
    }
}
